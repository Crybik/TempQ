# Script Coded by crybik
# GitHub: https://github.com/crybik

import wmi
from colorama import init, Fore, Style

def get_temperature_info(sensor):
    if sensor.SensorType == 'Temperature':
        return sensor.Name, sensor.Value
    return None, None

def main():
    init()  # Initialize colorama for colored output
    
    print("Script coded by crybik\nGitHub: https://github.com/crybik")
    
    try:
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        
        temperature_data = []
        
        for sensor in temperature_infos:
            name, value = get_temperature_info(sensor)
            if name and value is not None:
                temperature_data.append((name, value))
                
        temperature_data.sort(key=lambda x: x[1])  # Sort by temperature value
        
        for name, value in temperature_data:
            print(f"Sensor Name: {name}")
            if value < 50:
                color = Fore.GREEN
            elif value < 80:
                color = Fore.YELLOW
            else:
                color = Fore.RED
            print(f"Temperature: {color}{value} °C{Style.RESET_ALL}")
            print("=" * 20)
                
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
