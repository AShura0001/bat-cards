import time


initial_time_sec = 2*60

while initial_time_sec > 0:
    initial_time_sec -= 1
    time.sleep(1)
    minutes = (initial_time_sec // 60)
    seconds = (initial_time_sec % 60)
    print (minutes,":",  seconds)