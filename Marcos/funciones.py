def convertir_a_segundos(horas,minutos,segundos):
    segundos+=minutos*60
    segundos+=horas*60*60
    return segundos

def convertir_a_hms(segundos):
    horas=0
    minutos=0
    while True:
        if segundos>=3600:
            horas+=1
            segundos-=3600
        elif segundos >= 60:
            minutos+=1
            segundos-=60
        else:
            break
    return [horas,minutos,segundos]

def convertir_a_hms_otro(segundos):
    horas=segundos/3600
    minutos=(segundos-horas*3600)/60
    segundos-=(horas*3600+minutos*60)
    return horas,minutos,segundos


hora_1=["","",""]
hora_2=["","",""]
hora_resultado=["","",""]
hora_1[0]=int(raw_input("Hora 1:"))
hora_1[1]=int(raw_input("Minutos 1:"))
hora_1[2]=int(raw_input("Segundos 1:"))
hora_2[0]=int(raw_input("Hora 2:"))
hora_2[1]=int(raw_input("Minutos 2:"))
hora_2[2]=int(raw_input("Segundos 2:"))

hora_resultado[0]=hora_1[0]+hora_2[0]
hora_resultado[1]=hora_1[1]+hora_2[1]
hora_resultado[2]=hora_1[2]+hora_2[2]

print "El resultado es:",convertir_a_hms_otro(convertir_a_segundos(hora_resultado[0],hora_resultado[1],hora_resultado[2]))

