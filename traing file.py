import json
import legibilidad

f = open('getDevocionalesRevisionTutor.json',encoding='utf8')
g = open('mapTrainging.json','w',encoding='utf8')

array = []

data = json.load(f)

for i in data['data']:
    lecturasDiariasData = i['lecturasDiariasData']
    for j in lecturasDiariasData:
        campo1 = j['campo1']
        campo2 = j['campo2']

        fernandez_huertaCampo1 = legibilidad.fernandez_huerta(campo1)
        gutierrezCampo1 = legibilidad.gutierrez(campo1)
        szigriszt_pazosCampo1 = legibilidad.szigriszt_pazos(campo1)
        muCampo1 = legibilidad.mu(campo1)
        crawfordCampo1 = legibilidad.crawford(campo1)

        fernandez_huertaCampo2 = legibilidad.fernandez_huerta(campo2)
        gutierrezCampo2 = legibilidad.gutierrez(campo2)
        szigriszt_pazosCampo2 = legibilidad.szigriszt_pazos(campo2)
        muCampo2 = legibilidad.mu(campo2)
        crawfordCampo2 = legibilidad.crawford(campo2)
        
        array.append({
            "campo":j['campo1'],
            "fernandez_huerta": fernandez_huertaCampo1,
            "gutierrez": gutierrezCampo1,
            "szigriszt_pazos": szigriszt_pazosCampo1,
            "mu": muCampo1,
            "crawford": crawfordCampo1,
            "result":True,
        })

        array.append({
            "campo":j['campo2'],
            "fernandez_huerta": fernandez_huertaCampo2,
            "gutierrez": gutierrezCampo2,
            "szigriszt_pazos": szigriszt_pazosCampo2,
            "mu": muCampo2,
            "crawford": crawfordCampo2,
            "result":True,
        })

g.write(json.dumps(array,indent=2,ensure_ascii=False))

g.close()
f.close()