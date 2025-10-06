from time import sleep
import random

def quick_sleep_gen(seconds:float) -> None:
    upper_bound = (seconds+0.2)*10_000
    if (seconds >= 1.0):
        lower_bound = (seconds-0.2)*10_000
    else:
        lower_bound = seconds*10_000

    sleep_time = random.randint(int(lower_bound), int(upper_bound))/10_000*0.8
    sleep(sleep_time)
