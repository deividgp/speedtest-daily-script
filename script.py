import os
import schedule
import time
import sys
x = 1

def job():
    global x
    print("Speedtest at ", sys.argv[x])
    os.system("speedtest")
    x += 1

for arg in sys.argv:
    if arg != os.path.basename(__file__):
        schedule.every().day.at(arg).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)