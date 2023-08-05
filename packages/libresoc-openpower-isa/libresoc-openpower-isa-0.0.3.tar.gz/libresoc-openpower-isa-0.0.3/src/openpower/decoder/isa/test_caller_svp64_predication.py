from nmigen import Module, Signal
from nmigen.back.pysim import Simulator, Delay, Settle
from nmutil.formaltest import FHDLTestCase
import unittest
from openpower.decoder.isa.caller import ISACaller
from openpower.decoder.power_decoder import (create_pdecode)
from openpower.decoder.power_decoder2 import (PowerDecode2)
from openpower.simulator.program import Program
from openpower.decoder.isa.caller import ISACaller, SVP64State, CRFields
from openpower.decoder.selectable_int import SelectableInt
from openpower.decoder.orderedset import OrderedSet
from openpower.decoder.isa.all import ISA
from openpower.decoder.isa.test_caller import Register, run_tst
from openpower.sv.trans.svp64 import SVP64Asm
from openpower.consts import SVP64CROffs
from copy import deepcopy

class DecoderTestCase(FHDLTestCase):

    def _check_regs(self, sim, expected):
        for i in range(32):
            self.assertEqual(sim.gpr(i), SelectableInt(expected[i], 64))

    def tst_sv_load_store(self):
        lst = SVP64Asm(["addi 1, 0, 0x0010",
                        "addi 2, 0, 0x0008",
                        "addi 5, 0, 0x1234",
                        "addi 6, 0, 0x1235",
                        "sv.stw 5.v, 0(1.v)",
                        "sv.lwz 9.v, 0(1.v)"])
        lst = list(lst)

        # SVSTATE (in this case, VL=2)
        svstate = SVP64State()
        svstate.vl[0:7] = 2 # VL
        svstate.maxvl[0:7] = 2 # MAXVL
        print ("SVSTATE", bin(svstate.spr.asint()))

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, svstate=svstate)
            print(sim.gpr(1))
            self.assertEqual(sim.gpr(9), SelectableInt(0x1234, 64))
            self.assertEqual(sim.gpr(10), SelectableInt(0x1235, 64))

    def test_sv_extsw_intpred(self):
        # extsb, integer twin-pred mask: source is ~r3 (0b01), dest r3 (0b10)
        # works as follows, where any zeros indicate "skip element"
        #       - sources are 9 and 10
        #       - dests are 5 and 6
        #       - source mask says "pick first element from source (5)
        #       - dest mask says "pick *second* element from dest (10)
        #
        # therefore the operation that's carried out is:
        #       GPR(10) = extsb(GPR(5))
        #
        # this is a type of back-to-back VREDUCE and VEXPAND but it applies
        # to *operations*, not just MVs like in traditional Vector ISAs
        # ascii graphic:
        #
        #   reg num        0 1 2 3 4 5 6 7 8 9 10
        #   src ~r3=0b01                     Y N
        #                                    |
        #                              +-----+
        #                              |
        #   dest r3=0b10             N Y

        isa = SVP64Asm(['sv.extsb/sm=~r3/dm=r3 5.v, 9.v'
                       ])
        lst = list(isa)
        print ("listing", lst)

        # initial values in GPR regfile
        initial_regs = [0] * 32
        initial_regs[3] = 0b10   # predicate mask
        initial_regs[9] = 0x91   # source ~r3 is 0b01 so this will be used
        initial_regs[10] = 0x90  # this gets skipped
        # SVSTATE (in this case, VL=2)
        svstate = SVP64State()
        svstate.vl[0:7] = 2 # VL
        svstate.maxvl[0:7] = 2 # MAXVL
        print ("SVSTATE", bin(svstate.spr.asint()))
        # copy before running
        expected_regs = deepcopy(initial_regs)
        expected_regs[5] = 0x0                   # dest r3 is 0b10: skip
        expected_regs[6] = 0xffff_ffff_ffff_ff91 # 2nd bit of r3 is 1

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, initial_regs, svstate)
            self._check_regs(sim, expected_regs)

    def test_sv_extsw_intpred_dz(self):
        # extsb, integer twin-pred mask: dest is r3 (0b01), zeroing on dest
        isa = SVP64Asm(['sv.extsb/dm=r3/dz 5.v, 9.v'
                       ])
        lst = list(isa)
        print ("listing", lst)

        # initial values in GPR regfile
        initial_regs = [0] * 32
        initial_regs[3] = 0b01   # predicate mask (dest)
        initial_regs[5] = 0xfeed # going to be overwritten
        initial_regs[6] = 0xbeef # going to be overwritten (with zero)
        initial_regs[9] = 0x91   # dest r3 is 0b01 so this will be used
        initial_regs[10] = 0x90  # this gets read but the output gets zero'd
        # SVSTATE (in this case, VL=2)
        svstate = SVP64State()
        svstate.vl[0:7] = 2 # VL
        svstate.maxvl[0:7] = 2 # MAXVL
        print ("SVSTATE", bin(svstate.spr.asint()))
        # copy before running
        expected_regs = deepcopy(initial_regs)
        expected_regs[5] = 0xffff_ffff_ffff_ff91 # dest r3 is 0b01: store
        expected_regs[6] = 0                     # 2nd bit of r3 is 1: zero

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, initial_regs, svstate)
            self._check_regs(sim, expected_regs)

    def test_sv_add_intpred(self):
        # adds, integer predicated mask r3=0b10
        #       1 = 5 + 9   => not to be touched (skipped)
        #       2 = 6 + 10  => 0x3334 = 0x2223+0x1111
        isa = SVP64Asm(['sv.add/m=r3 1.v, 5.v, 9.v'
                       ])
        lst = list(isa)
        print ("listing", lst)

        # initial values in GPR regfile
        initial_regs = [0] * 32
        initial_regs[1] = 0xbeef   # not to be altered
        initial_regs[3] = 0b10   # predicate mask
        initial_regs[9] = 0x1234
        initial_regs[10] = 0x1111
        initial_regs[5] = 0x4321
        initial_regs[6] = 0x2223
        # SVSTATE (in this case, VL=2)
        svstate = SVP64State()
        svstate.vl[0:7] = 2 # VL
        svstate.maxvl[0:7] = 2 # MAXVL
        print ("SVSTATE", bin(svstate.spr.asint()))
        # copy before running
        expected_regs = deepcopy(initial_regs)
        expected_regs[1] = 0xbeef
        expected_regs[2] = 0x3334

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, initial_regs, svstate)
            self._check_regs(sim, expected_regs)

    def test_sv_add_cr_pred(self):
        # adds, CR predicated mask CR4.eq = 1, CR5.eq = 0, invert (ne)
        #       1 = 5 + 9   => not to be touched (skipped)
        #       2 = 6 + 10  => 0x3334 = 0x2223+0x1111
        isa = SVP64Asm(['sv.add/m=ne 1.v, 5.v, 9.v'
                       ])
        lst = list(isa)
        print ("listing", lst)

        # initial values in GPR regfile
        initial_regs = [0] * 32
        initial_regs[1] = 0xbeef   # not to be altered
        initial_regs[9] = 0x1234
        initial_regs[10] = 0x1111
        initial_regs[5] = 0x4321
        initial_regs[6] = 0x2223
        # SVSTATE (in this case, VL=2)
        svstate = SVP64State()
        svstate.vl[0:7] = 2 # VL
        svstate.maxvl[0:7] = 2 # MAXVL
        print ("SVSTATE", bin(svstate.spr.asint()))
        # copy before running
        expected_regs = deepcopy(initial_regs)
        expected_regs[1] = 0xbeef
        expected_regs[2] = 0x3334

        # set up CR predicate - CR4.eq=1 and CR5.eq=0
        cr = (0b0010) << ((7-4)*4) # CR4.eq (we hope)

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, initial_regs, svstate,
                                       initial_cr=cr)
            self._check_regs(sim, expected_regs)

    def test_intpred_vcompress(self):
        #   reg num        0 1 2 3 4 5 6 7 8 9 10 11
        #   src r3=0b101                     Y  N  Y
        #                                    |     |
        #                            +-------+     |
        #                            | +-----------+
        #                            | |
        #   dest always              Y Y Y

        isa = SVP64Asm(['sv.extsb/sm=r3 5.v, 9.v'])
        lst = list(isa)
        print("listing", lst)

        # initial values in GPR regfile
        initial_regs = [0] * 32
        initial_regs[3] = 0b101  # predicate mask
        initial_regs[9] = 0x90   # source r3 is 0b101 so this will be used
        initial_regs[10] = 0x91  # this gets skipped
        initial_regs[11] = 0x92  # source r3 is 0b101 so this will be used
        # SVSTATE (in this case, VL=3)
        svstate = SVP64State()
        svstate.vl[0:7] = 3  # VL
        svstate.maxvl[0:7] = 3  # MAXVL
        print("SVSTATE", bin(svstate.spr.asint()))
        # copy before running
        expected_regs = deepcopy(initial_regs)
        expected_regs[5] = 0xffff_ffff_ffff_ff90  # (from r9)
        expected_regs[6] = 0xffff_ffff_ffff_ff92  # (from r11)
        expected_regs[7] = 0x0  # (VL loop runs out before we can use it)

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, initial_regs, svstate)
            self._check_regs(sim, expected_regs)

    def test_intpred_vexpand(self):
        #   reg num        0 1 2 3 4 5 6 7 8 9 10 11
        #   src always                       Y  Y  Y
        #                                    |  |
        #                            +-------+  |
        #                            |   +------+
        #                            |   |
        #   dest r3=0b101            Y N Y

        isa = SVP64Asm(['sv.extsb/dm=r3 5.v, 9.v'])
        lst = list(isa)
        print("listing", lst)

        # initial values in GPR regfile
        initial_regs = [0] * 32
        initial_regs[3] = 0b101  # predicate mask
        initial_regs[9] = 0x90   # source is "always", so this will be used
        initial_regs[10] = 0x91  # likewise
        initial_regs[11] = 0x92  # the VL loop runs out before we can use it
        # SVSTATE (in this case, VL=3)
        svstate = SVP64State()
        svstate.vl[0:7] = 3  # VL
        svstate.maxvl[0:7] = 3  # MAXVL
        print("SVSTATE", bin(svstate.spr.asint()))
        # copy before running
        expected_regs = deepcopy(initial_regs)
        expected_regs[5] = 0xffff_ffff_ffff_ff90  # 1st bit of r3 is 1
        expected_regs[6] = 0x0  # skip
        expected_regs[7] = 0xffff_ffff_ffff_ff91  # 3nd bit of r3 is 1

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, initial_regs, svstate)
            self._check_regs(sim, expected_regs)

    def test_intpred_twinpred(self):
        #   reg num        0 1 2 3 4 5 6 7 8 9 10 11
        #   src r3=0b101                     Y  N  Y
        #                                    |
        #                              +-----+
        #                              |
        #   dest ~r3=0b010           N Y N

        isa = SVP64Asm(['sv.extsb/sm=r3/dm=~r3 5.v, 9.v'])
        lst = list(isa)
        print("listing", lst)

        # initial values in GPR regfile
        initial_regs = [0] * 32
        initial_regs[3] = 0b101  # predicate mask
        initial_regs[9] = 0x90   # source r3 is 0b101 so this will be used
        initial_regs[10] = 0x91  # this gets skipped
        initial_regs[11] = 0x92  # VL loop runs out before we can use it
        # SVSTATE (in this case, VL=3)
        svstate = SVP64State()
        svstate.vl[0:7] = 3  # VL
        svstate.maxvl[0:7] = 3  # MAXVL
        print("SVSTATE", bin(svstate.spr.asint()))
        # copy before running
        expected_regs = deepcopy(initial_regs)
        expected_regs[5] = 0x0  # dest ~r3 is 0b010: skip
        expected_regs[6] = 0xffff_ffff_ffff_ff90  # 2nd bit of ~r3 is 1
        expected_regs[7] = 0x0  # dest ~r3 is 0b010: skip

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, initial_regs, svstate)
            self._check_regs(sim, expected_regs)

    # checks that we are able to resume in the middle of a VL loop,
    # after an interrupt, or after the user has updated src/dst step
    # let's assume the user has prepared src/dst step before running this
    # vector instruction
    def test_intpred_reentrant(self):
        #   reg num        0 1 2 3 4 5 6 7 8 9 10 11 12
        #   srcstep=1                           v
        #   src r3=0b0101                    Y  N  Y  N
        #                                    :     |
        #                              + - - +     |
        #                              :   +-------+
        #                              :   |
        #   dest ~r3=0b1010          N Y N Y
        #   dststep=2                    ^

        isa = SVP64Asm(['sv.extsb/sm=r3/dm=~r3 5.v, 9.v'])
        lst = list(isa)
        print("listing", lst)

        # initial values in GPR regfile
        initial_regs = [0] * 32
        initial_regs[3] = 0b0101  # mask
        initial_regs[9] = 0x90   # srcstep starts at 2, so this gets skipped
        initial_regs[10] = 0x91  # skip
        initial_regs[11] = 0x92  # this will be used
        initial_regs[12] = 0x93  # skip

        # SVSTATE (in this case, VL=4)
        svstate = SVP64State()
        svstate.vl[0:7] = 4  # VL
        svstate.maxvl[0:7] = 4  # MAXVL
        # set src/dest step on the middle of the loop
        svstate.srcstep[0:7] = 1
        svstate.dststep[0:7] = 2
        print("SVSTATE", bin(svstate.spr.asint()))
        # copy before running
        expected_regs = deepcopy(initial_regs)
        expected_regs[5] = 0x0  # skip
        expected_regs[6] = 0x0  # dststep starts at 3, so this gets skipped
        expected_regs[7] = 0x0  # skip
        expected_regs[8] = 0xffff_ffff_ffff_ff92  # this will be used

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, initial_regs, svstate)
            self._check_regs(sim, expected_regs)

    def test_shift_one_by_r3_dest(self):
        #   reg num        0 1 2 3 4 5 6 7 8 9 10 11
        #   src r30=0b100                    N  N  Y
        #                                          |
        #                              +-----------+
        #                              |
        #   dest r3=1: 1<<r3=0b010   N Y N

        isa = SVP64Asm(['sv.extsb/dm=1<<r3/sm=r30 5.v, 9.v'])
        lst = list(isa)
        print("listing", lst)

        # initial values in GPR regfile
        initial_regs = [0] * 32
        initial_regs[3] = 1  # dest mask = 1<<r3 = 0b010
        initial_regs[30] = 0b100  # source mask
        initial_regs[9] = 0x90   # skipped
        initial_regs[10] = 0x91  # skipped
        initial_regs[11] = 0x92  # 3rd bit of r30 is 1
        # SVSTATE (in this case, VL=3)
        svstate = SVP64State()
        svstate.vl[0:7] = 3  # VL
        svstate.maxvl[0:7] = 3  # MAXVL
        print("SVSTATE", bin(svstate.spr.asint()))
        # copy before running
        expected_regs = deepcopy(initial_regs)
        expected_regs[5] = 0x0  # skip
        expected_regs[6] = 0xffff_ffff_ffff_ff92  # r3 is 1, so this is used
        expected_regs[7] = 0x0  # skip

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, initial_regs, svstate)
            self._check_regs(sim, expected_regs)

    def test_shift_one_by_r3_source(self):
        #   reg num        0 1 2 3 4 5 6 7 8 9 10 11
        #   src r3=2: 1<<r3=0b100            N  N  Y
        #                                          |
        #                              +-----------+
        #                              |
        #   dest r30=0b010           N Y N

        isa = SVP64Asm(['sv.extsb/sm=1<<r3/dm=r30 5.v, 9.v'])
        lst = list(isa)
        print("listing", lst)

        # initial values in GPR regfile
        initial_regs = [0] * 32
        initial_regs[3] = 2  # source mask = 1<<r3 = 0b100
        initial_regs[30] = 0b010  # dest mask
        initial_regs[9] = 0x90   # skipped
        initial_regs[10] = 0x91  # skipped
        initial_regs[11] = 0x92  # r3 is 2, so this will be used
        # SVSTATE (in this case, VL=3)
        svstate = SVP64State()
        svstate.vl[0:7] = 3  # VL
        svstate.maxvl[0:7] = 3  # MAXVL
        print("SVSTATE", bin(svstate.spr.asint()))
        # copy before running
        expected_regs = deepcopy(initial_regs)
        expected_regs[5] = 0x0  # skip
        expected_regs[6] = 0xffff_ffff_ffff_ff92  # 2nd bit of r30 is 1
        expected_regs[7] = 0x0  # skip

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, initial_regs, svstate)
            self._check_regs(sim, expected_regs)

    # checks reentrant CR predication
    def test_crpred_reentrant(self):
        #   reg num        0 1 2 3 4 5 6 7 8 9 10 11 12
        #   srcstep=1                           v
        #   src cr4.eq=1                     Y  N  Y  N
        #       cr6.eq=1                     :     |
        #                              + - - +     |
        #                              :   +-------+
        #   dest cr5.lt=1              :   |
        #        cr7.lt=1            N Y N Y
        #   dststep=2                    ^

        isa = SVP64Asm(['sv.extsb/sm=eq/dm=lt 5.v, 9.v'])
        lst = list(isa)
        print("listing", lst)

        # initial values in GPR regfile
        initial_regs = [0] * 32
        initial_regs[9] = 0x90  # srcstep starts at 2, so this gets skipped
        initial_regs[10] = 0x91  # skip
        initial_regs[11] = 0x92  # this will be used
        initial_regs[12] = 0x93  # skip

        cr = CRFields()
        # set up CR predicate
        # CR4.eq=1 and CR6.eq=1
        cr.crl[4][CRFields.EQ] = 1
        cr.crl[6][CRFields.EQ] = 1
        # CR5.lt=1 and CR7.lt=1
        cr.crl[5][CRFields.LT] = 1
        cr.crl[7][CRFields.LT] = 1
        # SVSTATE (in this case, VL=4)
        svstate = SVP64State()
        svstate.vl[0:7] = 4  # VL
        svstate.maxvl[0:7] = 4  # MAXVL
        # set src/dest step on the middle of the loop
        svstate.srcstep[0:7] = 1
        svstate.dststep[0:7] = 2
        print("SVSTATE", bin(svstate.spr.asint()))
        # copy before running
        expected_regs = deepcopy(initial_regs)
        expected_regs[5] = 0x0  # skip
        expected_regs[6] = 0x0  # dststep starts at 3, so this gets skipped
        expected_regs[7] = 0x0  # skip
        expected_regs[8] = 0xffff_ffff_ffff_ff92  # this will be used

        with Program(lst, bigendian=False) as program:
            sim = self.run_tst_program(program, initial_regs, svstate,
                                       initial_cr=cr.cr.asint())
            self._check_regs(sim, expected_regs)

    def run_tst_program(self, prog, initial_regs=None,
                              svstate=None,
                              initial_cr=0):
        if initial_regs is None:
            initial_regs = [0] * 32
        simulator = run_tst(prog, initial_regs, svstate=svstate,
                            initial_cr=initial_cr)
        simulator.gpr.dump()
        return simulator


if __name__ == "__main__":
    unittest.main()
