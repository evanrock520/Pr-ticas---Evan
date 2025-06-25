from time import sleep
from machine import Pin, ADC

adc = ADC(Pin(32))

adc.atten(ADC.ATTN_11DB)
adc.width(ADC_WIDTH_12BIT)

while True:
    valor_adc = adc.read()
    print('Valor ADC: ' + valor_adc)
    sleep(2)