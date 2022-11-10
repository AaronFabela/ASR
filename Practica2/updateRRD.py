import time
import rrdtool
from getSNMP import consultaSNMP
entradaUCast = 0
entradaIPv4 = 0
echoICMP = 0
segmentos = 0
dataUDP = 0

while 1:
    entradaUCast = int(consultaSNMP('comunidad', 'localhost',
                                           '1.3.6.1.2.1.2.2.1.11.1'))
    entradaIPv4 = int(consultaSNMP('comunidad', 'localhost',
                                           '1.3.6.1.2.1.4.3.0'))
    echoICMP = int(consultaSNMP('comunidad', 'localhost',
                                           '1.3.6.1.2.1.5.21.0'))
    segmentos = int(consultaSNMP('comunidad', 'localhost',
                                     '1.3.6.1.2.1.6.10.0'))
    dataUDP = int(consultaSNMP('comunidad', 'localhost',
                                     '1.3.6.1.2.1.7.1.0'))

    valor = "N:" + str(entradaUCast) + ':' + str(entradaIPv4) + ':' + str(echoICMP) + ':' + str(segmentos) + ':' + str(dataUDP)
    print(valor)
    #rrdtool.update('Data.rrd', valor)
    rrdtool.dump('Data.rrd','Data.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)