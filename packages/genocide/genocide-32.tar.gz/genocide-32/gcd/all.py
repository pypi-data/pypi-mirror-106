# This file is placed in the Public Domain

"all modules"

from gcd.krn import Kernel

import gcd.cms
import gcd.fnd
import gcd.hdl
import gcd.irc
import gcd.krn
import gcd.log
import gcd.obj

Kernel.addmod(gcd.cms)
Kernel.addmod(gcd.fnd)
Kernel.addmod(gcd.hdl)
Kernel.addmod(gcd.irc)
Kernel.addmod(gcd.krn)
Kernel.addmod(gcd.log)
Kernel.addmod(gcd.obj)
