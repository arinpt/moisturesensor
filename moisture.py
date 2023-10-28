

        
import machine
import utime

red_led = machine.Pin(28, machine.Pin.OUT)  # Replace <red_pin_number> with the actual pin number for the red LED
green_led = machine.Pin(1, machine.Pin.OUT)  # Replace <green_pin_number> with the actual pin number for the green LED
adc = machine.ADC(27)
vcc_pin = machine.Pin(17, machine.Pin.OUT)
vcc_pin.value(1)

while True:
    moisture = 130 - (adc.read_u16() * (100 / 65535))
    print("Moisture: ", round(moisture, 1), "% - ", utime.localtime())
    utime.sleep(0.5)
    
    if moisture >= 70 :
        green_led.value(1)
        red_led.value(0)
        utime.sleep(0.1)
    elif moisture < 70 :
        red_led.toggle()
        green_led.value(0)
        utime.sleep_ms(200)
    
