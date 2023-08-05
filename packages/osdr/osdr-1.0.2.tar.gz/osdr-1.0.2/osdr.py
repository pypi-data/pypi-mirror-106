# -*- coding: UTF-8 -*-

import ftd600.ftd3xx as ftd3xx
import sys
if sys.platform == 'win32':
    import ftd600._ftd3xx_win32 as _ft
elif sys.platform == 'linux':
    import ftd600._ftd3xx_linux as _ft
import queue
import datetime
import time
import timeit
import binascii
import itertools
import ctypes
import threading
import logging
import os
import platform
import argparse
import random
import string
import numpy as np
from interval import Interval


CMD_SET_TX_FREQ       = 0x1
CMD_SET_TX_BANDWIDTH  = 0x2
CMD_SET_TX_ATTE       = 0x3
CMD_SET_RX_FREQ       = 0x4
CMD_SET_RX_BANDWIDTH  = 0x5
CMD_SET_RX_GAIN       = 0x6
CMD_SET_SAMPLERATE    = 0x7
CMD_SET_MODE          = 0x8
CMD_SET_CHANNEL       = 0x9

param = [Interval(70e6, 6e9), Interval(200e3, 56e6), Interval(0, 89),
         Interval(70e6, 6e9), Interval(200e3, 56e6), Interval(1, 71),
         Interval(2.5e6, 41.25e6), [0, 1, 2, 3], [0, 1, 2]]


def usb3_detect():
    # OSDR已连接
    result = {"fd": None, "error": "OSDR connected"}

    # 获取设备信息
    numDevices = ftd3xx.createDeviceInfoList()
    if (numDevices == 0):
        # OSDR未连接
        result["error"] = "OSDR not connected"
        return result
    elif (numDevices > 1):
        # 连接了多个OSDR设备，只支持一个设备
        result["error"] = "Multiple osdr devices are connected, and only one device is supported"
        return result
    # 打开设备
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if (D3XX is None):
        # OSDR设备端口被占用
        result["error"] = "Osdr device port occupied"
        return result
    # 检查驱动
    if (sys.platform == 'win32' and D3XX.getDriverVersion() < 0x01020006):
        # 驱动已过期
        D3XX.close()
        result["error"] = "Driver expired"
        return result

    # 确认是usb3设备
    devDesc = D3XX.getDeviceDescriptor()
    bUSB3 = devDesc.bcdUSB >= 0x300
    if (bUSB3 == False):
        #D3XX.close()
        # 不是usb3设备，请确认线缆及端口支持usb3
        result["error"] = "It's not a USB 3 device. Please make sure the cable and port support USB 3"
        #return result

    # 配置为 245 1通道 66MHz
    cfg = D3XX.getChipConfiguration()
    if ((cfg.FIFOClock != _ft.FT_CONFIGURATION_FIFO_CLK_66)
       or (cfg.ChannelConfig != _ft.FT_CONFIGURATION_CHANNEL_CONFIG_1)
       or (cfg.FIFOMode != _ft.FT_CONFIGURATION_FIFO_MODE_245)):
        # 修改芯片配置
        cfg.FIFOClock = _ft.FT_CONFIGURATION_FIFO_CLK_66
        cfg.ChannelConfig = _ft.FT_CONFIGURATION_CHANNEL_CONFIG_1
        cfg.FIFOMode = _ft.FT_CONFIGURATION_FIFO_MODE_245
        D3XX.setChipConfiguration(cfg)

    result["fd"] = D3XX
    #print(D3XX)
    return result


# buf类型必须是bytes
def usb3_write(fd, buf, len):
    # pipe = 0x02 + 通道，目前只用通道0
    if sys.platform == 'linux':
        pipe = 0
    else:
        pipe = 0x02

    result = {"cnt": 0, "err": None}

    if (fd == None):
        #print("设备未连接")
        # 设备未连接
        result["err"] = "device not connected"
        return result
    # 发送数据给指定管道
    cnt = fd.writePipe(pipe, buf, len)
    error = fd.getLastError()
    if (error != 0):
        #print("write error %s" % (ftd3xx.getStrError(error)))
        # 关闭管道
        if sys.platform == 'linux':
            fd.flushPipe(pipe)
        else:
            fd.abortPipe(pipe)
    else:
        #print("write len %d" % cnt)
        result["cnt"] = cnt

    result["err"] = ftd3xx.getStrError(error)
    return result


def usb3_read(fd, buf, len):
    # pipe = 0x82 + 通道，目前只用通道0
    if sys.platform == 'linux':
        pipe = 0
    else:
        pipe = 0x82

    result = {"cnt": 0, "err": None}

    if (fd == None):
        # 设备未连接
        result["err"] = "device not connected"
        return result

    # 发送数据给指定管道
    cnt = fd.readPipe(pipe, buf, len)
    error = fd.getLastError()
    if (error != 0):
        #print("read error %s" % (ftd3xx.getStrError(error)))
        # 关闭管道
        if sys.platform == 'linux':
            fd.flushPipe(pipe)
        else:
            fd.abortPipe(pipe)
    else:
        #print("read len %d" % cnt)
        result["cnt"] = cnt

    result["err"] = ftd3xx.getStrError(error)
    return result


def usb3_set_param(fd, cmd, data):
    global param

    # 检查参数范围
    if (data not in param[cmd-1]):
        #print(cmd, data, param[cmd-1])
        # 超出允许范围
        return {"code": -1, "err": "Out of range"}

    # 发送命令
    frame = [0x80, 0x80]
    frame.extend(cmd.to_bytes(2, 'little'))
    frame.extend(data.to_bytes(8, 'little'))
    #print(frame)
    arr = np.array(frame, dtype=np.uint8)
    arr = arr.tobytes()
    result = usb3_write(fd, arr, len(arr))
    if (result["cnt"] == 0):
        # 参数写入错误:
        return {"code": -2, "err": "Parameter setting write error: " + result["err"]}

    # 接收响应
    while(True):
        ack_len = 16000
        ack = ctypes.c_buffer(ack_len)
        result = usb3_read(fd, ack, ack_len)
        cnt = result["cnt"]
        #print(cnt)
        if (cnt == 0):
            # 参数响应超时:
            return {"code": -3, "err": "Parameter setting response timeout: " + result["err"]}
        else:
            for i in ack[0 : cnt]:
                if (i == 0x80):
                    # 参数设置成功
                    return {"code": 0, "err": "Parameter setting succeeded"}


if __name__ == "__main__":
    result = usb3_detect()
    #print(result)
    """
    fd = result["fd"]
    if (fd != None):
        cmd = [0x80, 0x80, 0x1, 0x2, 0x3, 0x4]
        usb3_set_param(fd, cmd)
    """
