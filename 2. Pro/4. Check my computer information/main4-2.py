#정리해서 확인
import psutil

cpu = psutil.cpu_freq() #cpu의 frequency(진동수 = 주파수)
cpu_current_ghz = round(cpu.current / 1000, 2) # GHz단위로 바꾸기위한것. 소수점 2째자리에서 반올림. 라운드를써서 가로안의 것을 실행후 다시 그값을 왼쪽값에 넣는다.
print(f"cuu 속도: {cpu_current_ghz}GHz") #4-1과 다르게 앞에 f붙이고 {}안에 변수 입력하면 사용가능.

cpu_core = psutil.cpu_count(logical=False) #cpu의 물리적인 개수 코어수
print(f"cpu 코어: {cpu_core} 개")

memory = psutil.virtual_memory() #램
memory_total = round(memory.total / 1024**3) #기가바이트니 1024의 3제곱을 나눠준다.
print(f'메모리: {memory_total}GB')

disk = psutil.disk_partitions() #하드디스크 용량
for p in disk:
    print(p.mountpoint, p.fstype, end=' ') #디스크의 양과 타입을 출력, end=' '는 같은줄에 출력
    du = psutil.disk_usage(p.mountpoint) #디스크 사용량을 계산하고 총 크기를 검색 후 p.mountpoint값을 du에 저장.
    disk_total = round(du.total / 1024**3)
    print(f"디스크크기: {disk_total}.GB")

net = psutil.net_io_counters() # 네트워크
sent = round(net.bytes_sent/1024**2, 1) #바이트를 메가바이트로 변환.
recv = round(net.bytes_recv/1024**2, 1)
print(f"보내기: {sent}MB    받기 : {recv}MB")

print('net:', net)