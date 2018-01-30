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
dev = lib.find().next()
ffi = lib.ffi

i2c = CyI2C(dev)
i2c.debug = 1

mpu = NVR_UV(i2c)

embed()
