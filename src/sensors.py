# Responsible for interacting with all sensors on the vehicle
import mpu6050

class Sensors:
    def __init__(self):
        # TODO: Make I2C address changeable at some point
        imu = mpu6050.mpu6050(0x68)

    # Gets accelerometer data from the IMU
    # Afaik returns in m/s^2
    # TODO: Double check the above
    def getAccelData(self):
        return self.imu.get_accel_data()
    
    def getTempData(self):
        return self.imu.get_temp()

    # Returns deg/s
    def getGyroData(self):
        return self.imu.get_gyro_data()

if __name__ == "__main__":
    print("ERROR: You're trying to run a library")
