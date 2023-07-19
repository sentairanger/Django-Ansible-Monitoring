from django.shortcuts import render, HttpResponseRedirect
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import OutputDevice, LED, Servo, PWMOutputDevice

# Define the factories
factory = PiGPIOFactory(host='')
factory2 = PiGPIOFactory(host='')

# Define both robots
en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
motor_in1 = OutputDevice(13,  pin_factory = factory)
motor_in2 = OutputDevice(21,  pin_factory = factory)
motor_in3 = OutputDevice(17,  pin_factory = factory)
motor_in4 = OutputDevice(27,  pin_factory = factory)

en_3 = PWMOutputDevice(12, pin_factory=factory2)
en_4 = PWMOutputDevice(26, pin_factory=factory2)
pin1 = OutputDevice(13,  pin_factory = factory2)
pin2 = OutputDevice(21,  pin_factory = factory2)
pin3 = OutputDevice(17,  pin_factory = factory2)
pin4 = OutputDevice(27,  pin_factory = factory2)

#Define the eyes
linus_eye = LED(25, pin_factory=factory)
fiona_eye = LED(25, pin_factory=factory2)

#define the servos
servo1 = Servo(22, pin_factory=factory)
servo2 = Servo(23, pin_factory=factory)


def index(request):
    return render(request, 'ansibleapp/index.html', {})

def forward(request):
    motor_in1.on()
    motor_in2.off()
    motor_in3.on()
    motor_in4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def backward(request):
    motor_in1.off()
    motor_in2.on()
    motor_in3.off()
    motor_in4.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def left(request):
    motor_in1.off()
    motor_in2.on()
    motor_in3.on()
    motor_in4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def right(request):
    motor_in1.on()
    motor_in2.off()
    motor_in3.off()
    motor_in4.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def stop(request):
    motor_in1.off()
    motor_in2.off()
    motor_in3.off()
    motor_in4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def north(request):
    pin1.on()
    pin2.off()
    pin3.on()
    pin4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def south(request):
    pin1.off()
    pin2.on()
    pin3.off()
    pin4.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def west(request):
    pin1.off()
    pin2.on()
    pin3.on()
    pin4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def east(request):
    pin1.on()
    pin2.off()
    pin3.off()
    pin4.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def stop2(request):
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def eyeon(request):
    linus_eye.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def eyeoff(request):
    linus_eye.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def fionaon(request):
    fiona_eye.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def fionaoff(request):
    fiona_eye.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def thirty(request):
    en_1.value = .3
    en_2.value = .3
    en_3.value = .3
    en_4.value = .3
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def fifty(request):
    en_1.value = .5
    en_2.value = .5
    en_3.value = .5
    en_4.value = .5
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def full(request):
    en_1.value = 1
    en_2.value = 1
    en_3.value = 1
    en_4.value = 1
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def servomin(request):
    servo1.min()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def servomid(request):
    servo1.mid()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def servomax(request):
    servo1.max()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def servomin2(request):
    servo2.min()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def servomid2(request):
    servo2.mid()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def servomax2(request):
    servo2.max()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
