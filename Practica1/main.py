# Programa principal
import os
from getSNMP import consultaSNMP
from functions import *
from agente import *

bandera = True
agente = False
fileA = File()

os.system('cls')
print('Sistema de Administración de Red')
while bandera:
    os.system('cls')
    print("Selecciona una opcion: ")
    print("\t 1.-Agregar dispositivo")
    print("\t 2.-Cambiar información de dispositivo")
    print("\t 3.-Eliminar dispositivo")
    print("\t 4.-Generar reporte")
    print("\t 5.-Salir")
    opc = input(': ')
    if opc == "1":
        os.system('cls')
        print('----- Agregar dispositivo -----')
        print('\n\tIndica los siguientes datos: \n')
        host = input('Indica el nombre o host del nuevo dispositivo: ')
        snpm = input('\t\tVersión SNMP: \n')
        comunidad = input('\t\tNombre de la comunidad: \n')
        puerto = input('\t\tPuerto: \n')
        host = Agente(host)
        host.setAgente(snpm, comunidad, puerto)
        agente = True
        os.system('pause')
    if opc == "2":
        os.system('cls')
        if (agente):
            print('\t\t----- Editar dispositivo -----')
            print('\t\nDispositivos existentes: ')
            print(host.printAgentes())
            agenteActualizar = int(input(
                "Ingresa el numero de agente a actualizar: "))
            nuevoHost = input(
                'Indica el nuevo nombre o host del nuevo dispositivo: ')
            snpm = input('\t\tindica la nueva versión SNMP: \n')
            comunidad = input('\t\tIndica nuevo nombre de la comunidad: \n')
            puerto = input('\t\tIndica nuevo puerto: \n')
            agenteActualizar = agenteActualizar - 1
            print("Agente actualizado")
            print(host.printAgente(host.updateAgente(agenteActualizar,
                  nuevoHost, snpm, comunidad, puerto)))
            # print(host.updateAgente(agenteActualizar))
            # print(host.printAgente(host.getAgente(agenteActualizar-1)))
        else:
            print('AGREGA UN DISPOSITIVO')
        os.system('pause')
    if opc == "3":
        os.system('cls')
        if (agente):
            print(host.printAgentes())
            agenteEliminar = input('Numero de agente que se eliminará: ')
            host.deleteAgente(agenteEliminar)
        else:
            print('NO HAY DISPOSITIVO REGISTRADO')
        os.system('pause')
    if opc == "4":
        os.system('cls')
        print('GENERAR REPORTE')
        host.generarReporte(str(host.agentes.index(host)))
        os.system('pause')
    if opc == "5":
        os.system('cls')
        print('\n\tGracias por utilizar el programa...\n')
        os.system('pause')
        bandera = False
