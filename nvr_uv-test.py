#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cy7c65211 import *
from nvr_uv import *
from IPython import embed

# dll = "c:/app/Cypress/Cypress-USB-Serial/library/lib/cyusbserial.dll"
# dll = "C:\\Program Files (x86)\\Cypress\\USB-Serial SDK\\library\\cyusbserial\\x64\\cyusbserial.dll"
dll = "C:\\Program Files (x86)\\Cypress\\USB-Serial SDK\\library\\cyusbserial\\x86\\cyusbserial.dll"
# dll = "/usr/local/lib/libcyusbserial.so"
lib = CyUSBSerial(lib=dll)
# dev = lib.find().next()
try:
    dev = lib.find(vid=0x04B4, pid=0x000A).next()
except Exception, e:
    print e
    raise
ffi = lib.ffi

i2c = CyI2C(dev)
i2c.debug = 1

# mpu = NVR_UV(i2c)
nv = NV_UV(i2c)

# nv_read = NV_Read(i2c)

# nv.start_temp_1()
# nv_read.get_temp()
# nv.start_temp_2()
# nv.get_light()
# nv.read(2)

# nv2 = NV_Read(i2c)
# nv_read.get_light()
# nv_read.read(2)


embed()
