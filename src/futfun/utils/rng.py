from time import sleep
import random

def quick_sleep_gen(seconds:int) -> None:
    upper_bound = (seconds+0.2)*10_000
    if (seconds >= 1.0):
        lowerbound = (seconds-0.2)*10_000
    else:
        lowerbound = seconds*10_000

    sleep_time = random.randint(lowerbound, upper_bound)/10_000*0.8
    sleep(sleep_time)
