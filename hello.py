import I2C_LCD_driver
import time
import subprocess
mylcd = I2C_LCD_driver.lcd()


mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_display_string("Pi3 b", 1, 0)

# #ylcd.lcd_display_string("Nerdlab-1814", 1, 0)
# With the help of chatgpt

def get_cpu_temp():
  with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
    cpu_temp = f.read()
  return int(cpu_temp) / 1000

# Get 1-minute load average
def get_1m_load_avg():
    output = subprocess.check_output(['uptime'])
    load_avg = output.decode().split()[-3].rstrip(',')
    return load_avg

# Run nslookup command and capture output
#output = subprocess.check_output(['nslookup', 'iotcloudlabs.com'])
# Decode output from bytes to string
#output_str = output.decode()

# Check if output contains multiple IP addresses
#if output_str.count('Address:') > 1:
# Find IP address in output
  #ip_index = output_str.find('Address:', output_str.find('Address:') + 1) + len('Address:')
  #ip_end_index = output_str.find('\n', ip_index)
  #ip_address = output_str[ip_index:ip_end_index].strip()

# Assign IP address to variable
#my_ip_address = ip_address
#mylcd.lcd_display_string("%s"%my_ip_address, 2, 0)

while True:
   cpu_temp = get_cpu_temp()
   load_avg = get_1m_load_avg()
   temp_str = '{:.1f}C'.format(cpu_temp)
   mylcd.lcd_display_string("RL: "+load_avg, 3, 0)
   mylcd.lcd_display_string("CPU "+temp_str, 3, 11)
   mylcd.lcd_display_string("%s" %time.strftime("%H:%M:%S"), 4,0)
   mylcd.lcd_display_string("%s" %time.strftime("%m/%d/%Y"), 4,10)
