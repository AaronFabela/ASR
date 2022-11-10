import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = int(time.mktime((2022,11,10,8,20,0,0,0,0)))
tiempo_final = int(time.mktime((2022,11,10,9,9,0,0,0,0)))
ret1 = rrdtool.graph( "traficoRED1.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                     "DEF:entradaUcast=Data.rrd:entradaUcast:AVERAGE",
                     "CDEF:escalaIn=entradaUcast,8,*",
                     "LINE1:escalaIn#FF0000:Tráfico de entrada")

ret2 = rrdtool.graph( "traficoRED2.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                        "DEF:entradaIPv4=Data.rrd:entradaIPv4:AVERAGE",
                     "CDEF:escalaIn=entradaIPv4,8,*",
                     "LINE1:escalaIn#FF0000:Tráfico de entrada")

ret3 = rrdtool.graph( "traficoRED3.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                        "DEF:echoICMP=Data.rrd:echoICMP:AVERAGE",
                     "CDEF:escalaIn=echoICMP,8,*",
                     "LINE1:escalaIn#FF0000:Tráfico de entrada")

ret4 = rrdtool.graph( "traficoRED4.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                        "DEF:segmentos=Data.rrd:segmentos:AVERAGE",
                     "CDEF:escalaIn=segmentos,8,*",
                     "LINE1:escalaIn#FF0000:Tráfico de entrada")

ret5 = rrdtool.graph( "traficoRED5.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                        "DEF:dataUDP=Data.rrd:dataUDP:AVERAGE",
                     "CDEF:escalaIn=dataUDP,8,*",
                     "LINE1:escalaIn#FF0000:Tráfico de entrada")