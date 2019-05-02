import time as B,json
from kraken.core.profiler import Profiler as C
A=C()
B.sleep(0.15)
A.push('fn1')
B.sleep(0.05)
A.push('fn2')
B.sleep(0.01)
A.pop()
A.generateReport()