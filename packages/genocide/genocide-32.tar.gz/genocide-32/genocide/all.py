# This file is placed in the Public Domain

"all modules"

from gcd.krn import Kernel

import genocide.req
import genocide.slg
import genocide.trt
import genocide.wsd

Kernel.addmod(genocide.req)
Kernel.addmod(genocide.slg)
Kernel.addmod(genocide.trt)
Kernel.addmod(genocide.wsd)
