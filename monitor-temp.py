#monitor-temp
#Monitor the temperature of your Raspberry Pi!
#Tested on a Raspberry Pi 3B+ running Ubuntu Mate 18
#github.com/smcclennon
import os
import time
startTime=time.time()
while True:
    elapsedTime=time.time()-startTime
    temp=os.popen("vcgencmd  measure_temp").readline()
    print('[Elapsed: '+str(round(elapsedTime)).replace(".0", "")+'] Current Temperature: '+str(temp.replace("temp=", "").replace("'", "*")))
    time.sleep(1)
