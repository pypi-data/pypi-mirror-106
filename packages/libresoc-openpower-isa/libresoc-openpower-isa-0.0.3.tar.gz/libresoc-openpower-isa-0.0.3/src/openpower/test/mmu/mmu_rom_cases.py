from openpower.simulator.program import Program
from openpower.endian import bigendian
from openpower.test.common import (TestAccumulatorBase, skip_case)
from openpower.consts import MSR


def b(x):
    return int.from_bytes(x.to_bytes(8, byteorder='little'),
                          byteorder='big', signed=False)


default_mem = { 0x10000:    # PARTITION_TABLE_2
                       # PATB_GR=1 PRTB=0x1000 PRTS=0xb
                b(0x800000000100000b),

                0x30000:     # RADIX_ROOT_PTE
                        # V = 1 L = 0 NLB = 0x400 NLS = 9
                b(0x8000000000040009),

                0x40000:     # RADIX_SECOND_LEVEL
                        # 	   V = 1 L = 1 SW = 0 RPN = 0
                           # R = 1 C = 1 ATT = 0 EAA 0x7
                b(0xc000000000000187),

                0x1000000:   # PROCESS_TABLE_3
                       # RTS1 = 0x2 RPDB = 0x300 RTS2 = 0x5 RPDS = 13
                b(0x40000000000300ad),
            }


class MMUTestCaseROM(TestAccumulatorBase):
    # MMU on microwatt handles MTSPR, MFSPR, DCBZ and TLBIE.
    # libre-soc has own SPR unit
    # libre-soc MMU supports MTSPR and MFSPR but **ONLY** for the subset
    # of SPRs it actually does.
    # other instructions here -> must be load/store

    def case_mmu_ldst(self):
        lst = [
                #"mtspr 720, 1", # XXX do not execute unsupported instructions
                "lhz 3, 0(1)"      # load some data
              ]

        initial_regs = [0] * 32
        
        # set process table
        prtbl = 0x1000000
        initial_regs[1] = prtbl
        
        initial_msr = 1 << MSR.PR # must set "problem" state for virtual memory
        initial_sprs = {'DSISR': 0, 'DAR': 0,
                         720: 0}
        self.add_case(Program(lst, bigendian),
                      initial_regs, initial_sprs,
                      initial_msr=initial_msr)


