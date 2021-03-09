'''
For to check the function working, just change the valus below in the print(add_time)
'''
def add_time(começa, duração,dia=None):

    duração_hora=int(duração[0:-3])
    duração_minutos=int(duração[-2:])
    if len(começa)==8:
        começa_hora=int(começa[0:2])
        começa_minutos=int(começa[3:5])
    elif len(começa)==7:
        começa_hora=int(começa[0:1])
        começa_minutos=int(começa[2:4])
    if começa_hora==12:
        começa_hora=0
    if começa[-2:]=="PM":
        começa_hora+=12

    minutos=começa_minutos+duração_minutos
    if minutos>=60:
        minutos-=60
        duração_hora+=1
    horas=começa_hora+duração_hora
    dias=horas//24
    lista_dias =['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']
    if dia:
        index=lista_dias .index(dia.capitalize())
        index=(index+dias)%7
        dia=lista_dias [index]
    horas=horas%24

    novo_horário=''
    if horas>=12:
        horas-=12
        if horas==0:
            horas=12
        novo_horário+=str(horas)+':'+str(minutos).rjust(2,'0')+' PM'
    else:
        if horas==0:
            horas=12
        novo_horário+=str(horas)+':'+str(minutos).rjust(2,'0')+' AM'
    
    if dia:
        novo_horário+=', '+dia
    if dias>0:
        novo_horário+=' '
        if dias==1:
            novo_horário+="(Próximo dia)"
        else:
            novo_horário+="({} dias depois)".format(dias)
    return novo_horário

if __name__ == "__main__":
    print(add_time("5:01 AM", "200:50"))