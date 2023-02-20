#본인의 컴퓨터 정보만을 확인 가능.
import psutil

cpu = psutil.cpu_freq() #cpu의 frequency(진동수 = 주파수)
print('cpu frequency:', cpu)

cpu_core = psutil.cpu_count(logical=False) #cpu의 물리적인 개수 코어수, (logical=False)는 논리적 코어 수 대신 물리적 코어 수로 반환
print('cpu core:',cpu_core)

memory = psutil.virtual_memory() #램
print('memory:', memory)

disk = psutil.disk_partitions() #하드디스크 용량
print('disk:', disk)

net = psutil.net_io_counters() # 컴퓨터의 네트워크 I/O정보를 가져온다.
print('net:', net)