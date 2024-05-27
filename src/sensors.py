# Responsible for interacting with all sensors on the vehicle
# Kinda useless right now, mostly just a wrapper.
# TODO: add on filters later
import mpu6050

class Sensors:
    def __init__(self):
        # TODO: Make I2C address changeable at some point
        imu = mpu6050.mpu6050(0x68)

    # Gets accelerometer data from the IMU
    # Returns in m/s^2. NOTE: the get_accel_data() function can have a 
    # g=True argument passed to return accel data in gs
    def getAccelData(self):
        return self.imu.get_accel_data()
    
    def getTempData(self):
        return self.imu.get_temp()

    # Returns deg/s
    def getGyroData(self):
        return self.imu.get_gyro_data()

if __name__ == "__main__":
    print("ERROR: You're trying to run a library")
