from machine import Pin
from time import sleep
pulsador1 = Pin (28, Pin.IN)
led1 = Pin (1, Pin.OUT)
pulsador2 = Pin (27, Pin.IN)
led2 = Pin (2, Pin.OUT)

while True:
  if pulsador1.value() == 1:
    led1.value(1)

  if pulsador1.value () == 0:
    led1.value(0)

  if pulsador2.value () == 1:

    if led2.value() == 0:
      led2.value(1)

    elif led2.value () == 1:
      led2.value(0)
  
    sleep (0.5)
