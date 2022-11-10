#!/usr/bin/env python
import rrdtool
ret = rrdtool.create("Data.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:entradaUcast:COUNTER:120:U:U",
                     "DS:entradaIPv4:COUNTER:120:U:U",
                     "DS:echoICMP:COUNTER:120:U:U",
                     "DS:segmentos:COUNTER:120:U:U",
                     "DS:dataUDP:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:1:50")

if ret:
    print (rrdtool.error())
