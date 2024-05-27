import time
from sensors import Sensors

imu = Sensors
currVelDat={}
prevVelDat={'x': 0, 'y': 0, 'z': 0}
cycleTime=0
timeStamp=time.time()


while True:
    accelData = imu.getAccelData()
    cycleTime = timeStamp - time.time()
    for axis in accelData:
        currVelDat[axis] = prevVelDat[axis] + accelData[axis]*(cycleTime)
    prevVelDat = currVelDat.copy()
    print(f"Current velocity: {currVelDat}")
    time.sleep(.1)
    timeStamp = time.time()