from pyb import Pin, Timer,ExtInt
import math

def filtr_mas(mas):
    z = {}
    max_data = 0
    count = 0
    for i in mas:
        if i in z:
            z[i] += 1
        else:
            z[i] = 1
    for i in sorted(z):
        if z[i] > count:
            count = z[i]
            max_data = i
    return max_data


def pulseIn(pin,st):
    start = 0
    end = 0
    mas_filtr=[]
    micros = Timer(5, prescaler=83, period=0x3fffffff)
    micros.counter(0)
    if st:
        while pin.value() == 0:
            start = micros.counter()

        while pin.value() == 1:
            end = micros.counter()
    else:
        while pin.value() == 1:
            start = micros.counter()

        while pin.value() == 0:
            end = micros.counter()


    micros.deinit()
    res=(end - start)
    mas_filtr=[res for i in range(10)]

    return filtr_mas(mas_filtr)


def constrain(x, out_min, out_max):
    if x < out_min:
        return out_min
    elif out_max < x:
        return out_max
    else:
        return x


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def sum_set(x, n):
    for i in range(n):
        x += x
        return x


def interval(val, a, b, st=False):
    if not st:
        if val < a:
            return False
        elif val > b:
            return False
        else:
            return True
    if st:
        if val < a:
            return True
        elif val > b:
            return True
        else:
            return False

class PWM:
    def __init__(self,pin_i,freq=1000):

        timer_n=0
        channel=0
        self.state=False
        self.pulse_width_get=6000
        self.pulse_width=30000
        self.pin=Pin(pin_i)

        if pin_i=='A0'or pin_i=='X1':
            self.state = False
            timer_n=2
            channel=1
        elif pin_i=='A1'or pin_i=='X2':
            self.state = False
            timer_n = 2
            channel = 2
        elif pin_i=='A2'or pin_i=='X3':
            self.state = False
            timer_n = 2
            channel = 3
        elif pin_i=='A5'or pin_i=='X6':
            self.state=True
            timer_n = 8
            channel = 1

        elif pin_i == 'A6' or pin_i == 'X7':
            self.state = False
            timer_n = 13
            channel = 1

        elif pin_i=='A7'or pin_i=='X8':
            self.state = False
            timer_n = 14
            channel = 1
        elif pin_i=='B6'or pin_i=='X9':
            self.state = False
            timer_n = 4
            channel = 1
        elif pin_i=='B7'or pin_i=='X10':
            self.state = False
            timer_n = 4
            channel = 2
        elif pin_i=='B10'or pin_i=='Y9':
            self.state = False
            timer_n = 2
            channel = 3
        elif pin_i=='B11'or pin_i=='Y10':
            self.state = False
            timer_n = 2
            channel = 4
        elif pin_i=='B0'or pin_i=='Y11':
            self.state = True
            timer_n = 8
            channel = 2

        elif pin_i=='B1'or pin_i=='Y12':
            self.state = True
            timer_n = 8
            channel = 3

        elif pin_i=='B8'or pin_i=='Y3':
            self.state = False
            timer_n = 4
            channel = 3

        elif pin_i=='B9'or pin_i=='Y4':
            self.state = False
            timer_n = 4
            channel = 4

        elif pin_i=='B13'or pin_i=='Y6':
            self.state = True
            timer_n = 1
            channel = 1
            print('incorrect operation of pwm')

        elif pin_i=='B14'or pin_i=='Y7':
            self.state = True
            timer_n = 1
            channel = 2
        elif pin_i=='B15'or pin_i=='Y8':
            self.state = True
            timer_n = 1
            channel = 3

        elif pin_i=='C6'or pin_i=='Y1':
            self.state = False

            timer_n = 8
            channel = 1

        elif pin_i=='C7'or pin_i=='Y2':
            self.state = False
            timer_n = 8
            channel = 2
        self.timer = Timer(timer_n, freq=freq)
        self.ch = self.timer.channel(channel, Timer.PWM, pin=self.pin)#
        self.pwm_write(0)

    def pwm_write(self,percent):

        if self.state:
            self.ch.pulse_width_percent(100-percent)
        else:
            self.ch.pulse_width_percent(percent)


'''
x, y, z = accel.filtered_xyz()  


# main.py -- put your code here!
import pyb,time
import encoder.encoder as anc

enc = anc.Encoder(pin_clk='X11', pin_dt='X12')

def readloop(enc):
        oldval = 0
        while True:
            val = enc.value
            if oldval != val:
                print(val)
                oldval = val
            time.sleep_ms(50)

readloop(enc)



'''