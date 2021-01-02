import psutil 

print('Physical Cores: ',psutil.cpu_count(logical=False))
print('Total Cores: ', psutil.cpu_count(logical=True))


#CPU Frequecies
cpufreq = psutil.cpu_freq()
print(f'Max Freq: {cpufreq.max:.2f}Mhz ')
print(f'Current Freq: {cpufreq.current:.2f}Mhz ')

#Usage
print('CPU Usage Per Core: ')
for i, percentage in enumerate(psutil.cpu_percent(percpu=True,interval = 1)):
    print(f"Core{i}: {percentage}%")
print(f'Total CPU Usage: {psutil.cpu_percent()}%')
