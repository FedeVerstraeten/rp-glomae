#!/usr/bin/python
import sys 
import redpitaya_scpi as scpi

rp_s = scpi.scpi(sys.argv[1])
wave_form = 'sine'
freq = 40e6
ampl = 0.7
#phase = 45

rp_s.tx_txt('GEN:RST')
rp_s.tx_txt('SOUR1:FUNC ' + str(wave_form).upper())
rp_s.tx_txt('SOUR1:FREQ:FIX ' + str(freq)) 
rp_s.tx_txt('SOUR1:VOLT ' + str(ampl))
rp_s.tx_txt('OUTPUT1:STATE ON')