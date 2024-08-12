# First-Come, First-Served Scheduling Algorithm
# [Your Name]

# 프로세스 정보 (도착 시간, 작업 시간, 우선순위)
processes = [
    {"id": "P1", "arrival_time": 0, "burst_time": 15, "priority": 3},
    {"id": "P2", "arrival_time": 5, "burst_time": 8, "priority": 4},
    {"id": "P3", "arrival_time": 8, "burst_time": 2, "priority": 1},
    {"id": "P4", "arrival_time": 10, "burst_time": 5, "priority": 2},
]

# 프로세스를 도착 시간에 따라 정렬
processes.sort(key=lambda x: x["arrival_time"])

# 변수 초기화
current_time = 0
waiting_times = []

# 실행 순서 기록
execution_order = []

# 프로세스 스케줄링
for process in processes:
    if current_time < process["arrival_time"]:
        current_time = process["arrival_time"]
    
    # 대기 시간 계산
    waiting_time = current_time - process["arrival_time"]
    waiting_times.append(waiting_time)
    
    # 실행
    execution_order.append(process["id"])
    current_time += process["burst_time"]

# 평균 대기 시간 계산
average_waiting_time = sum(waiting_times) / len(waiting_times)

# 결과 출력
print(f"### FCFS - [Your Name] ###")
print(f"실행 순서: {' -> '.join(execution_order)}")
for i, process in enumerate(processes):
    print(f"{process['id']} 대기: {waiting_times[i]}초")
print(f"평균 대기시간: {average_waiting_time}초")