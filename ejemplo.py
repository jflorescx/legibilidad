#!/usr/bin/env python3

import legibilidad
import json

f = open('getDevocionalesRevisionTutor.json')
log = open('log.txt','w')

data = json.load(f)

for i in data['data']:
    userId = i['userId']
    lecturasDiariasData = i['lecturasDiariasData']
    log.write('*************\n')
    log.write('userId: '+ userId + '\n')

    for j in lecturasDiariasData:
        idDevo = j['idDevo']
        campo1 = j['campo1']
        campo2 = j['campo2']
        
        comprenCampo1 = legibilidad.gutierrez(campo1)
        comprenCampo2 = legibilidad.gutierrez(campo2)
        perspiCampo1 = legibilidad.szigriszt_pazos(campo1)
        perspiCampo2 = legibilidad.szigriszt_pazos(campo2)
        if campo1 == campo2:
            log.write('\tidDevo: '+ idDevo+' - Duplicados\n')
        if comprenCampo1 < 25 or comprenCampo2 < 25 or perspiCampo1 < 30 or perspiCampo2 < 30:
            log.write('\tidDevo: '+ idDevo+' - Comprencion abajo de 30\n')
            log.write('\t\tCampo1: '+ campo1+'\n')
            log.write('\t\t' + str(comprenCampo1) + ' - ' + str(perspiCampo1) + '\n')
            log.write('\t\tCampo2: '+ campo2+'\n')
            log.write('\t\t' + str(comprenCampo2) + ' - ' + str(perspiCampo2)+'\n')

        # log.write('idDevo: '+ idDevo+'\n')
        # log.write('campo1: '+ campo1+'\n')
        # log.write('comprenCampo1: '+ str(comprenCampo1)+'\n')
        # log.write('perspiCampo1: '+ str(perspiCampo1)+'\n')

        # log.write('campo2: '+campo2+'\n')
        # log.write('comprenCampo2: '+ str(comprenCampo2)+'\n')
        # log.write('perspiCampo2: '+str(perspiCampo2)+'\n')

log.close()
f.close()
