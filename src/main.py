import mpu6050
import time

mpu6050 = mpu6050.mpu6050(0x68)

def readSensorData():
    accelData = mpu6050.get_accel_data()

    gyroData = mpu6050.get_gyro_data()

    temp = mpu6050.get_temp()

    return accelData, gyroData, temp


while True:

    accelData, gyroData, temp = readSensorData()

    print(f"Accelerometer Data: {accelData}")
    print(f"Gyroscope Data: {gyroData}")
    print(f"Temperature Data: {temp}")

    time.sleep(1)