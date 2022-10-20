from operator import index
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from getSNMP import consultaSNMP

x, y = letter


class Agente:

    agentes = []
    reportes = []

    def __init__(self, host):
        self.host = host
        self.version = ''
        self.comunidad = ''
        self.puerto = ''
        self.nombre = ''
        self.contacto = ''
        self.ubicacion = ''
        self.sistema = ''
        self.Nointerfaces = ''

    def setHost(self, host):
        self.host = host

    def setVersion(self, version):
        self.version = version

    def setComunidad(self, comunidad):
        self.comunidad = comunidad

    def setPuerto(self, puerto):
        self.puerto = puerto

    def setNombre(self, nombre):
        self.nombre = nombre

    def setContacto(self, contacto):
        self.contacto = contacto

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def setSistema(self, sistema):
        self.sistema = sistema

    def getHost(self):
        return self.host

    def getVersion(self):
        return self.version

    def getComunidad(self):
        return self.comunidad

    def getPuerto(self):
        return self.puerto

    def getNombre(self):
        return self.nombre

    def getContacto(self):
        return self.contacto

    def getUbicacion(self):
        return self.ubicacion

    def getSistema(self):
        return self.sistema

    # AGREGAR DISPOSITIVO

    def setAgente(self, snmp, comunidad, puerto):
        self.setVersion(snmp)
        self.setComunidad(comunidad)
        self.setPuerto(puerto)
        self.agentes.append(self)

    # Obtener agente

    def getAgente(self, agente):
        return self.agentes[agente]

    # EDITAR DISPOSITIVO

    def updateAgente(self, agente, host, version, comunidad, puerto):
        self.agentes[agente].setHost(host)
        self.agentes[agente].setVersion(version)
        self.agentes[agente].setComunidad(comunidad)
        self.agentes[agente].setVersion(puerto)
        return self.getAgente(agente)

    # def updateAgente(self, agente):
    #     return self.getAgente(agente)

    # ELIMINAR DISPOSITIVO

    def deleteAgente(self, agenteEliminar):
        print('\t\t----- Eliminar dispositivo -----')
        if (len(self.agentes) == 0):
            print('\t\t\n No hay dispositivos registrados ')
        else:
            self.agentes.pop(int(agenteEliminar)-1)
            print('Agente '+agenteEliminar + "eliminado correctamente")

    # IMPRIMIR DISPOSITIVOS

    def printAgentes(self):
        for i in range(len(self.agentes)):
            print(
                f'\t\nDispositivo {i+1} -->\n\t\t Host: {self.agentes[i].getHost()} \n\t\tComunidad: {self.agentes[i].getComunidad()} \n\t\tPuerto: {self.agentes[i].getPuerto()}')

    def printAgente(self, agente):
        print(
            f'\t\nDispositivo -->\n\t\t Host: {agente.getHost()} \n\t\tComunidad: {agente.getComunidad()} \n\t\tPuerto: {agente.getPuerto()}')

    # Consultar Sistema operativo y versión

    def consultaInfo(self):

        info = consultaSNMP(self.getComunidad(),
                            self.getHost(), "1.3.6.1.2.1.1.1.0")

        if "Windows" in info:
            self.setSistema("Windows")
            info = info[info.index('Software:')+1:]
            info = " ".join(info)
        elif "Linux" in info:
            self.setSistema("Linux")
            info = info[info.index('Linux'):info.index('Linux')+3]
            info = " ".join(info)
        else:
            info = 'Sistema operativo no reconocido'

        return info

    # Consultar nombre de dispositivo

    def consultaNombre(self):

        self.setNombre("".join(consultaSNMP(self.getComunidad(),
                       self.getHost(), "1.3.6.1.2.1.1.5.0")))

        return self.getNombre()

    # Consultar información de contacto

    def consultaContacto(self):

        self.setContacto("".join(consultaSNMP(
            self.getComunidad(), self.getHost(), "1.3.6.1.2.1.1.4.0")))

        return self.getContacto()

    # Consultar ubicación

    def consultaUbicacion(self):

        self.setUbicacion("".join(consultaSNMP(
            self.getComunidad(), self.getHost(), "1.3.6.1.2.1.1.6.0")))

        return self.getUbicacion()

    def consultaInterfaces(self):

        interfaces = int(("".join(consultaSNMP(
            self.getComunidad(), self.getHost(), "1.3.6.1.2.1.2.1.0"))))

        return interfaces

    def consultarInterfaz(self, indice):
        return ("".join(consultaSNMP(
            self.getComunidad(), self.getHost(), "1.3.6.1.2.1.2.2.1.7."+str(indice))))

     # Genera el reporte PDF

    def generarReporte(self, nombreArchivo):
        self.consultaInfo()
        archivo = canvas.Canvas(nombreArchivo + ".pdf", pagesize=letter)
        archivo.drawString(180, y-75, "INSTITUTO POLITÉCNICO NACIONAL")
        archivo.drawString(200, y-95, "Escuela Superior de Cómputo")
        archivo.drawString(
            75, y-160, f"Sistema Operativo: {self.consultaInfo()}")
        archivo.drawImage(f"{self.getSistema()}.jpg", x -
                          350, y-230, width=65, height=65)
        archivo.drawString(
            75, y-260, f"Nombre de dispositivo: {self.consultaNombre()}")
        archivo.drawString(75, y-275, f"Contacto: {self.consultaContacto()}")
        archivo.drawString(75, y-290, f"Ubicación: {self.consultaUbicacion()}")
        interfaces = self.consultaInterfaces()
        op = 305
        for i in range(interfaces):
            archivo.drawString(
                75, y-op, f"Interfaz 1.3.6.1.2.1.2.2.1.7.{i+1}: {self.consultarInterfaz(i+1)}")
            op = op+15

        #archivo.drawString(75,y-270,f"Número de interfaces: {self.consultaNombre()}")
        archivo.showPage()
        archivo.save()
        self.reportes.append(archivo)
        print(self.reportes)
