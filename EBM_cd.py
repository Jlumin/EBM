# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:03:42 2020
EBM version 1.0
@author: Ian % Jim
"""
import serial
import time
import struct
import binascii
#portName = "/dev/ttyS0"    # Raspberry Pi 3
portName = "COM1"
BAUD_RATES = 921600 # Unit in bit/s

ser = serial.Serial(port = portName,
                    baudrate = BAUD_RATES,
                    bytesize = serial.EIGHTBITS,
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE,
                    timeout = 5) # Unit in second
try:
    while ser.isOpen:
        print(time.strftime('%Y%m%d %H:%M:%S'))
        now = time.strftime("%Y%m%d%H%M")
        readbyte = 30840
        dataAcc  = list()
        data_bin = ser.read(readbyte)
        data_hex = data_bin.hex().split('4154') # 0X4154 > ASCII: AT
        saveFid = "acc_read_{}.bin".format(now)
        for ii in range(len(data_hex)):
            if len(data_hex[ii]) == 3084: # length of th complete package is 3084
                fmt = "384f" # (3084 - 12) / 8 = 384 float numbers
                data_decode = struct.unpack_from(fmt, binascii.unhexlify(data_hex[ii][4:-8]))       
                dataAcc = dataAcc + (list(data_decode))   

        dataAcc_save = [dataAcc[n:n+3] for n in range(0, len(dataAcc), 3)]
        with open(saveFid, "a") as file:
            file.write("x,y,z,\n") 
            for ii in range(0, len(dataAcc_save)):
                file.write(str(dataAcc_save[ii][0]))
                file.write(",")
                file.write(str(dataAcc_save[ii][1]))
                file.write(",")
                file.write(str(dataAcc_save[ii][2]))
                file.write(",\n")  

except KeyboardInterrupt:
    print(" -------Stop-------")
    ser.flushInput()
    ser.close()
    print(time.strftime('%Y%m%d %H:%M:%S'))