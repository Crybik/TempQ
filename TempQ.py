# script Coded by crybik
#github : https://github.com/crybik
print ("script coded by cryibk \n Github : https://github.com/crybik")
import wmi
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
for sensor in temperature_infos:
    if sensor.SensorType==u'Temperature':
        print(sensor.Name)
        print(sensor.Value)
