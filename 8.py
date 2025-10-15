# 8. Time Module – Execution Time

import time
s = 0

starttime = time.time()

for i in range(1000000):
    s += i

endtime = time.time()

totaltime = endtime - starttime

print(f'Execusion time : {totaltime}')