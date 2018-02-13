#!/bin/env python
# -*- coding: utf-8 -*-

from bitstring import *

# Young Optics CY7C65215 I2C value
I2C_SLV_ADDR = 0x1B
LED_CURRENT_CMD = 0x54
LED_ENABLE_CMD = 0x52
LED_ENABLE_CTRL = 0x02
LED_DISABLE_CTRL = 0x00
SOURCE_SEL_CMD = 0x05
PATTERN_SEL_CMD = 0x0B
HDMI_SEL_DATA = 0x00
PATTERN_SEL_DATA = 0x01

class ValueObject():
    pass

class NV_UV():
    # def __init__(self, i2c, address=0x68):
    def __init__(self, i2c, address=0x1B):  # 0x37 read / 0x36 write
    # def __init__(self, i2c, address=0x39):
        self.i2c = i2c
        # self.cfg = i2c.prepare(slaveAddress=address, isStopBit=1, isNakBit=1)
        self.cfg = i2c.prepare(slaveAddress=address, isStopBit=1, isNakBit=0)

    def read(self, len=1):
        buf = "\x00" * len
        return self.i2c.read(self.cfg, buf)

    def write(self, data):
        return self.i2c.write(self.cfg, data)

    def get_reg(self, reg, len=1):
        self.write(pack('<B', reg).bytes)
        return self.read(len)

    def set_reg(self, reg, val):
        return self.write(pack('<BB', reg, val).bytes)

    #=============================================== add local

    def led_on(self, val):
        if val == 1:
            ch_data = pack('<BB', LED_ENABLE_CMD, LED_ENABLE_CTRL).bytes
        else:
            ch_data = pack('<BB', LED_ENABLE_CMD, LED_DISABLE_CTRL).bytes
        return self.i2c.write(self.cfg, ch_data)

    def divide_hex(self, val):
        return divmod(val, 0x100)

    def led_cur(self, val):
        try:
            high, low = self.divide_hex(val)
            # high_hex = format(high, '02x')
            # low_hex = format(low, '02x')
            msb_high = hex(high)
            lsb_low = hex(low)
        except Exception, e:
            print e
            raise

        # 00 00 21 02 00 00
        try:
            # test_data = pack('<BBBBBBB', LED_CURRENT_CMD, 0x0, 0x0, 0x21, 0x2, 0x0, 0x0).bytes
            ch_data = pack('<BBBBBBB', LED_CURRENT_CMD, 0x0, 0x0, low, high, 0x0, 0x0).bytes
        except Exception, e:
            raise
        # print ch_data

        return self.i2c.write(self.cfg, ch_data)

    def test_pattern(self, val):
        if val == 1:    # ramp
            source_data = pack('<BB', SOURCE_SEL_CMD, 0x01).bytes
            self.i2c.write(self.cfg, source_data)
            ch_data = pack('<BBBBBBB', PATTERN_SEL_CMD, 0x01, 0x70, 0x00, 0xFF, 0x00, 0x00).bytes
            return self.i2c.write(self.cfg, ch_data)
        elif val == 2:  # checker
            source_data = pack('<BB', SOURCE_SEL_CMD, 0x01).bytes
            self.i2c.write(self.cfg, source_data)
            ch_data = pack('<BBBBBBB', PATTERN_SEL_CMD, 0x07, 0x70, 0x04, 0x00, 0x04, 0x00).bytes
            return self.i2c.write(self.cfg, ch_data)
        else:   # 0 hdmi
            source_data = pack('<BB', SOURCE_SEL_CMD, 0x00).bytes
            return self.i2c.write(self.cfg, source_data)

    def start_temp_1(self):
        source_data1 = pack('<B', 0xD6).bytes
        # source_data0 = pack('<B', 0xAC).bytes
        # source_data1 = pack('<BB', 0xD6, 0x03).bytes
        self.i2c.write(self.cfg, source_data1)
        # self.i2c.write(self.cfg, source_data0)
        aaa = self.read(2)
        return aaa
        # source_data2 = pack('<BB', 0xA0, 0x00).bytes
        # self.i2c.write(self.cfg, source_data2)

    def start_temp_2(self):
        # source_data1 = pack('<BB', 0xA0, 0x03).bytes
        # source_data0 = pack('<B', 0xAC).bytes
        # # source_data1 = pack('<BB', 0xD6, 0x03).bytes
        # self.i2c.write(self.cfg, source_data1)
        # self.i2c.write(self.cfg, source_data0)
        # aaa = self.read(2)
        source_data2 = pack('<BB', 0xA0, 0x00).bytes
        self.i2c.write(self.cfg, source_data2)

    def get_light(self):
        # source_data0 = pack('<BB', 0xA0, 0x03).bytes
        # self.i2c.write(self.cfg, source_data0)
        source_data1 = pack('<B', 0xAC).bytes
        self.i2c.write(self.cfg, source_data1)
        # aaa = self.read(2)
        # return aaa
        # source_data2 = pack('<BB', 0xA0, 0x00).bytes
        # self.i2c.write(self.cfg, source_data2)


class NV_Read():
    # def __init__(self, i2c, address=0x68):
    # def __init__(self, i2c, address=0x1B):  # 0x37 read / 0x36 write
    def __init__(self, i2c, address=0x39):  # 0x73 read
        self.i2c2 = i2c
        # self.cfg = i2c.prepare(slaveAddress=address, isStopBit=1, isNakBit=1)
        self.cfg2 = i2c.prepare(slaveAddress=address, isStopBit=1, isNakBit=0)

    def read(self, len=1):
        buf = "\x00" * len
        return self.i2c2.read(self.cfg2, buf)

    def write(self, data):
        return self.i2c2.write(self.cfg2, data)

    def get_reg(self, reg, len=1):
        self.write(pack('<B', reg).bytes)
        return self.read(len)

    def set_reg(self, reg, val):
        return self.write(pack('<BB', reg, val).bytes)

    def get_temp(self):
        # aaa = self.read(1)
        bbb = self.read(2)
        return bbb

    def get_light(self):
        source_data1 = pack('<B', 0xAC).bytes
        self.i2c2.write(self.cfg2, source_data1)
