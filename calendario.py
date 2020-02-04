import calendar
mes = int(input('Digite o numero do mês: '))   #2

if (mes >=1 and mes <=12):              #3
    c = calendar.TextCalendar (calendar.SUNDAY)
    #cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    nome = calendar.day_name(localized.Brazil)
    print (nome)
    cal = c.formatmonth(2020, mes)   #4
    print ("Esse é o Calendário do mês",mes)
    print ('--------------------------------')  #5
    print (cal);             #6
else:    
    print ('Intrada invalida')         #7