import sys
import rrdtool
import time
from Notify import send_alert_attached
import time
from getSNMP import consultaSNMP

hostname = str(consultaSNMP('comunidad', 'localhost', '1.3.6.1.2.1.1.1.0'))

correo = str(consultaSNMP('comunidad', 'localhost', '1.3.6.1.2.1.1.4.0'))

ubicacion = str(consultaSNMP('comunidad', 'localhost', '1.3.6.1.2.1.1.6.0'))


def generarGraficaCPU(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv("deteccionCPU.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final+1),
                         "--vertical-label=Cpu load",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "--title=CARGA CPU - Aaron Jhair Fabela Galvan",
                         "DEF:cargaCPU=trend.rrd:CPUload:AVERAGE",
                         "LINE2:cargaCPU#FFFF11:Carga de CPU",
                         "HRULE:70#FF3B11:Umbral 70%",
                         "HRULE:40#1CFF11:Umbral 40%")
    print('Listo CPU')


def generarGraficaRam(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv("deteccionRAM.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final+1),
                         "--vertical-label=Ram disponible",
                         '--lower-limit', '0',
                         '--upper-limit', '30',
                         "--title=RAM - Aaron Jhair Fabela Galvan",
                         "DEF:cargaRAM=trend.rrd:RAM:AVERAGE",
                         "LINE2:cargaRAM#117DFF:Carga de RAM",
                         "HRULE:40#FF3B11:Umbral 40%",
                         "HRULE:30#1CFF11:Umbral 30%")
    print('Listo RAM')


def generarGraficaRed(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv("deteccionRed.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final+1),
                         "--vertical-label=Porcentaje de red ocupada",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "--title=RED - Aaron Jhair Fabela Galvan",
                         "DEF:cargaRed=trend.rrd:Red:MAX",
                         "LINE2:cargaRed#FB11FF:Carga de Red",
                         "HRULE:1#FF3B11:Umbral 1%",
                         "HRULE:2#1CFF11:Umbral 2%")
    print('Listo Red')


while (1):

    ultima_actualizacion = rrdtool.lastupdate("trend.rrd")
    CPU = ultima_actualizacion['ds']['CPUload']
    RAM = ultima_actualizacion['ds']['RAM']
    RED = ultima_actualizacion['ds']['Red']
    tiempo = ultima_actualizacion['date'].timestamp()

    if CPU > 40.0 and CPU < 70.0:
        generarGraficaCPU(tiempo)
        send_alert_attached("CPU está en el umbral precaución", "deteccionCPU.png", "Porcentaje: "+str(
            CPU)+"\nHostname: "+hostname+'\n' + "Contacto:" + correo + '\n' + "Ubicación: " + ubicacion)
    if CPU > 70:
        generarGraficaCPU(tiempo)
        send_alert_attached("CPU Está en el umbral crítico", "deteccionCPU.png", "Porcentaje: "+str(
            CPU)+"\nHostname: "+hostname+'\n' + "Contacto:" + correo + '\n' + "Ubicación: " + ubicacion)

    if RAM < 40 and RAM > 30:
        generarGraficaRam(tiempo)
        send_alert_attached("RAM en umbral crítico", "deteccionRAM.png", "Porcentaje libre: "+str(
            RAM)+"\nHostname: "+hostname+'\n' + "Contacto:" + correo + '\n' + "Ubicación: " + ubicacion)
    if RAM < 30:
        generarGraficaRam(tiempo)
        send_alert_attached("RAM Está en el umbral precaución", "deteccionRAM.png", "Porcentaje libre: "+str(
            RAM)+"\nHostname: "+hostname+'\n' + "Contacto: " + correo + '\n' + "Ubicación: " + ubicacion)

    if RED > 1 and RED < 2:
        generarGraficaRed(tiempo)
        send_alert_attached("Red en umbral Correcto", "deteccionRed.png", "Porcentaje usado: "+str(
            RED)+"\nHostname: "+hostname+'\n' + "Contacto: " + correo + '\n' + "Ubicación: " + ubicacion)
    if RED > 2:
        generarGraficaRed(tiempo)
        send_alert_attached("Red está en umbral Precaución", "deteccionRed.png", "Porcentaje usado: "+str(
            RED)+"\nHostname: "+hostname+'\n' + "Contacto: " + correo + '\n' + "Ubicación: " + ubicacion)
    time.sleep(10)
