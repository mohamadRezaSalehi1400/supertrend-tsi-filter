from time import time, localtime, sleep
from datetime import datetime, timedelta
#from sound import sound


#برای زمانی که ساعت سیستم با ساعت متاتریدر مساوی است با دقت یک ثانیه
def check_meta_tf_per_second(tf, tz):
    obj = datetime.fromtimestamp(time() -tz)
    m = obj.minute
    s = obj.second
    h = obj.hour
    if obj.weekday() >=5 : return False
    if tf == 'M5' and s == 0 and ( m == 0 or m == 5 or m == 10 or m == 15 or m == 20 or m == 25 or m == 30 or m == 35 or m == 40 or m == 45 or m == 50 or m == 55): return True
    if tf == 'M10' and s == 0 and ( m == 10 or m== 20 or m== 30 or m== 40 or m == 0): return True
    if tf == 'M15' and s == 0 and ( m == 0 or m == 30 or m == 45 or m == 15): return True
    if tf == 'M30' and s == 0 and ( m== 0 or m== 30): return True
    if tf == 'H1' and s == 0 and m == 0: return True
    if tf == 'H4' and s ==0 and m == 0 and ( h ==  0 or h == 4 or h == 8 or h == 12 or h == 16 or h == 20): return True
    if tf == 'H8' and s ==0 and m ==0 and (h == 0 or h == 8 or h == 16): return True
    if tf == 'D1' and h == 0 and m == 0 and s == 0 : return True
    return False

#برای زمانی که ساعت سیستم یک ساعت ونیم از ساعت متاتریدر جلو تر است با دقت یک ثانیه
def check_current_tf_per_second(tf):
    obj = datetime.fromtimestamp(time())
    m = obj.minute
    s = obj.second
    h = obj.hour
    if obj.weekday() >=5 : return False
    if tf == 'M2' and s == 0 and ( m == 0 or m == 2 or m == 4 or m == 6 or m == 8 or m == 10 or m == 12 or m == 14 or m == 16 or m == 18 or m == 20 or m == 22 or m == 24 or m == 26 or m == 28 or m == 30 or m == 32 or m == 34 or m == 36 or m == 38 or m == 40 or m == 42 or m == 44 or m == 46 or m == 48 or m == 50 or m == 52 or m == 54 or m == 56 or m == 58 ): return True
    if tf == 'M5' and s == 0 and ( m == 0 or m == 5 or m == 10 or m == 15 or m == 20 or m == 25 or m == 30 or m == 35 or m == 40 or m == 45 or m == 50 or m == 55): return True
    if tf == 'M10' and s == 0 and ( m == 10 or m== 20 or m== 30 or m== 40 or m == 0): return True
    if tf == 'M15' and s == 0 and ( m == 0 or m == 30 or m == 45 or m == 15): return True
    if tf == 'M30' and s == 0 and ( m== 0 or m== 30): return True
    if tf == 'H1' and s == 0 and m == 30: return True
    if tf == 'H4' and s ==0 and m == 30 and ( h ==  1 or h == 5 or h == 9 or h == 13 or h == 17 or h == 21): return True
    if tf == 'H8' and s ==0 and m ==30 and (h == 1 or h == 9 or h == 17): return True
    if tf == 'D1' and h ==1 and m ==30 and s ==0 : return True
    return False


if __name__ =='__main__':
    i = 40
    #tf = 'M5'
    tf = input('timeframe')
    while True:
        sleep(1)
        #time_now =time()
        #if not check_day(time_now) : continue
        if not check_current_tf_per_second(tf): continue
        i += 5
        print(i)
        #sound("./sound/notification.wav")

