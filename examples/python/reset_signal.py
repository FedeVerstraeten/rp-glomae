#!/usr/bin/python
import sys 
import redpitaya_scpi as scpi

rp_s = scpi.scpi(sys.argv[1])

rp_s.tx_txt('GEN:RST')