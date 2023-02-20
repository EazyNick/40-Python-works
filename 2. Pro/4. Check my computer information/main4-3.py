#1초마다 내 컴퓨터 상태 확인
import psutil

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:

    cpu_p = psutil.cpu_percent(interval=1) #인터벌을 줘서 1초마다 측정, 시작이 1초니 전부 주기가 1초가됨.
    print(f"cuu사용량: {cpu_p}%")

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available / 1024**3, 1) 
    print(f'메모리: {memory_avail}GB')

    net = psutil.net_io_counters() 
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2
    sent = round(curr_sent-prev_sent,1) #현재값에서 이전값을 빼서 얼마만큼 쓰고있는지 알 수 있다.
    recv = round(curr_recv-prev_recv,1) #소수 첫째자리까지 반올림한다.
    print(f"보내기: {sent}MB    받기 : {recv}MB")
    prev_sent = curr_sent
    prev_recv = curr_recv

#cntl + c누르면 정지된다.