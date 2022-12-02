import time
import rrdtool
from getSNMP import consultaSNMP
#rrdpath = '../RRD/'
PromCPU = 0

while 1:
    carga_CPU1 = int(consultaSNMP('comunidad', 'localhost',
                     '1.3.6.1.2.1.25.3.3.1.2.196608'))
    carga_CPU2 = int(consultaSNMP('comunidad', 'localhost',
                     '1.3.6.1.2.1.25.3.3.1.2.196609'))
    carga_CPU3 = int(consultaSNMP('comunidad', 'localhost',
                     '1.3.6.1.2.1.25.3.3.1.2.196610'))
    carga_CPU4 = int(consultaSNMP('comunidad', 'localhost',
                     '1.3.6.1.2.1.25.3.3.1.2.196611'))
    carga_CPU5 = int(consultaSNMP('comunidad', 'localhost',
                     '1.3.6.1.2.1.25.3.3.1.2.196612'))
    carga_CPU6 = int(consultaSNMP('comunidad', 'localhost',
                     '1.3.6.1.2.1.25.3.3.1.2.196613'))
    promedio = float((carga_CPU1 + carga_CPU2 + carga_CPU3 +
                     carga_CPU4 + carga_CPU5 + carga_CPU6) / 6)
    ram = int(consultaSNMP('comunidad', 'localhost', '1.3.6.1.4.1.2021.4.6.0'))
    ramDIsp = float(ram*100/7050120)

    entradaRed = int(consultaSNMP(
        'comunidad', 'localhost', '1.3.6.1.2.1.2.2.1.10.2'))
    salidaRed = int(consultaSNMP(
        'comunidad', 'localhost', '1.3.6.1.2.1.2.2.1.16.2'))
    porcentajeRed = float(((entradaRed+salidaRed)/8)*100/100000000)

    mensaje = "N:" + str(promedio) + ' -- ' + \
        str(ramDIsp) + ' -- ' + str(porcentajeRed)
    print(mensaje)

    rrdtool.update('trend.rrd', mensaje)
    rrdtool.dump('trend.rrd', 'trend.xml')
    time.sleep(1)

if ret:
    print(rrdtool.error())
    time.sleep(300)
