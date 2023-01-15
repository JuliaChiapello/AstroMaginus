import math
import datetime
import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Funcion que devuelve una tupla conteniendo la longitud zodiacal y el signo del zodiaco.
def convertLongitudVerdadera_a_LongitudZodiacal(long):
    if long >= 0 and long < 30:
        long = long - 0
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  ARIES"
    elif long >= 30 and long  < 60:
        long = long - 30
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  TAURO"
    elif long >= 60 and long < 90:
        long = long - 60
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  GEMINIS"
    elif long >= 90 and long < 120:
        long = long - 90
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  CANCER"
    elif long >= 120 and long < 150:
        long = long - 120
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  LEO"
    elif long >= 150 and long < 180:
        long = long - 150
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  VIRGO"
    elif long >= 180 and long < 210:
        long = long - 180
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  LIBRA"
    elif long >= 210 and long < 240:
        long = long - 210
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  ESCORPIO"
    elif long >= 240 and long < 270:
        long = long - 240
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  SAGITARIO"
    elif long >= 270 and long < 300:
        long = long - 270
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  CAPRICORNIO"
    elif long >= 300 and long < 330:
        long = long - 300
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  ACUARIO"
    elif long >= 330 and long < 359.999999:
        long = long - 330
        l = convertGradosDecimales_a_GradosMinutosSegundos(long)
        return str(l[0])+"°"+str(l[1])+"'"+str(l[2])+'"'+"  PISCIS"

        
# Funcion que calcula el arcocotangente de un valor dado.
def arccotg(x):
    return (math.pi / 2) - math.atan(x)


# Funcion que convierte grados, minutos y segundos en grados decimales y lo retorna.
def convertGradosMinutosSegundos_a_GradosDecimales(grados, minutos, segundos):
    g = grados + (minutos / 60) + (segundos / 3600)
    return g


# Funcion que convierte grados decimales a grados, minutos y segundos. Retorna una tupla.
def convertGradosDecimales_a_GradosMinutosSegundos(grados):
    parteDecimal, parteEntera = math.modf(grados)
    g = parteEntera
    parteDecimal, parteEntera = math.modf(parteDecimal * 60)
    m = parteEntera
    s = round(parteDecimal * 60, 2)
    return g, m, s


# Funcion que convierte horas, minutos y segundos a horas decimales y lo retorna.
def convertHorasMinutosSegundos_a_HorasDecimales(horas, minutos, segundos):
    return horas + minutos / 60 + segundos / 3600


# Funcion que convierte horas decimales a horas, minutos y segundos. Retorna una tupla.
def convertHorasDecimales_a_HorasMinutosSegundos(horas):
    parteDecimal, parteEntera = math.modf(horas)
    h = parteEntera
    parteDecimal, parteEntera = math.modf(parteDecimal * 60)
    m = parteEntera
    s = round(parteDecimal * 60, 2)
    return h, m, s


# Funcion que convierte grados, minutos y segundos a horas, minutos y segundos. Retorna una tupla.
def GradosMinutosSegundos_a_HorasMinutosSegundos(grados, minutos, segundos):
    g = convertGradosMinutosSegundos_a_GradosDecimales(grados, minutos, segundos)
    h = g / 15
    return convertHorasDecimales_a_HorasMinutosSegundos(h)


# Funcion que convierte horas, minutos y segundos a grados, minutos y segundos. Retorna una tupla.
def HorasMinutosSegundos_a_GradosMinutosSegundos(horas, minutos, segundos):
    h = convertHorasMinutosSegundos_a_HorasDecimales(horas, minutos, segundos)
    g = h * 15
    return convertGradosDecimales_a_GradosMinutosSegundos(g)    


# Funcion que dada un valor de tiempo, lo convierte a una hora entre 0 y 23.
def rango0a23(valor):
    if valor < 0:
        while valor < 0:
            valor = valor + 24    
    elif valor >= 24:
        while valor >= 24:
            valor = valor - 24
    return valor


# Funcion que dado un año devuelve True si el año es bisiesto y False en caso contrario.    
def esBisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False


# Funcion que devuelve True si la fecha pasada como parametro es correcta. Devuelve False en caso contrario.    
def parsearFecha(dia, mes, anio):
    if anio >= 1900 and anio <= 9999:    
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia >= 1 and dia <= 31:
                return True
            else:
                return False
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia >= 1 and dia <= 30:
                return True
            else:
                return False
        if mes == 2 and esBisiesto(anio) == True:
            if dia >= 1 and dia <= 29:
                return True
            else:
                return False
        elif mes == 2 and esBisiesto(anio) == False:
            if dia >= 1 and dia <= 28:
                return True
            else:
                return False


# Funcion que determina la zona horaria para Argentina dada una fecha. Esta puede ser 2, 3 o 4.
def zonasHorariasArgentina(dia, mes, anio, prov):
    def intervalo_Fechas(dia1, mes1, anio1, dia2, mes2, anio2):
        fecha_Inicio = str(dia1)+"/"+str(mes1)+"/"+str(anio1)
        fecha_Final = str(dia2)+"/"+str(mes2)+"/"+str(anio2)
        inicio = datetime.datetime.strptime(fecha_Inicio, "%d/%m/%Y")
        fin = datetime.datetime.strptime(fecha_Final, "%d/%m/%Y")
        intervalo_Fechas = pd.date_range(inicio, fin)
        intervalo = intervalo_Fechas.strftime("%d/%m/%Y")
        lista_Fechas = []
        for elem in intervalo:
            lista_Fechas += [elem]    
        return lista_Fechas      
    
    zm4 = [(1,5,1920,30,11,1930), (1,4,1931,14,10,1931), (1,3,1932,31,10,1932), (1,3,1933,31,10,1933), \
           (1,3,1934,31,10,1934), (1,3,1935,31,10,1935), (1,3,1936,31,10,1936), (1,3,1937,31,10,1937), \
           (1,3,1938,31,10,1938), (1,3,1939,31,10,1939), (1,3,1940,30,6,1940), (15,6,1941,14,10,1941), \
           (1,8,1943,14,10,1943), (1,3,1946,30,9,1946), (1,10,1963,14,12,1963), (1,3,1964,14,10,1964), \
           (1,3,1965,14,10,1965), (1,3,1966,14,10,1966), (2,4,1967,30,9,1967), (7,4,1968,5,10,1968), \
           (6,4,1969,4,10,1969)]

    zm3 = [(1,12,1930,31,3,1931), (15,10,1931,29,2,1932), (1,11,1932,28,2,1933), (1,11,1933,28,2,1934), \
           (1,11,1934,28,2,1935), (1,11,1935,29,2,1936), (1,11,1936,28,2,1937), (1,11,1937,28,2,1938), \
           (1,11,1938,28,2,1939), (1,11,1939,29,2,1940), (1,7,1940,14,6,1941), (15,10,1941,31,7,1943), \
           (15,10,1943,28,2,1946), (1,10,1946,30,9,1963), (15,12,1963,29,2,1964), (15,10,1964,28,2,1965), \
           (15,10,1965,28,2,1966), (15,10,1966,1,4,1967), (1,10,1967,6,4,1968), (6,10,1968,5,4,1969), \
           (5,10,1969,22,1,1974), (1,5,1974,30,11,1988), (5,3,1989,14,10,1989), (4,3,1990,20,10,1990), \
           (3,3,1991,19,10,1991), (1,3,1992,17,10,1992), (7,3,1993,29,12,2007), (16,3,2008,18,10,2008), \
           (15,3,2009,1,7,2023)]

    zm2 = [(23,1,1974,30,4,1974), (1,12,1988,4,3,1989), (15,10,1989,3,3,1990), (21,10,1990,2,3,1991), \
           (20,10,1991,29,2,1992), (18,10,1992,6,3,1993), (31,12,2007,15,3,2008), (19,10,2008,14,3,2009)]

    provincias = ["CATAMARCA", "CHUBUT", "JUJUY", "LA PAMPA", "LA RIOJA", "MENDOZA", "NEUQUÉN", "RÍO NEGRO", \
                  "SALTA", "SAN JUAN", "SAN LUIS", "SANTA CRUZ", "TIERRA DEL FUEGO"]

    if dia == 0 or dia == 1 or dia == 2 or dia == 3 or dia == 4 or dia == 5 or dia == 6 or dia == 7 or \
       dia == 8 or dia == 9:
        d = "0" + str(dia)
    else:
        d = str(dia)
    if mes == 1 or mes == 2 or mes == 3 or mes == 4 or mes == 5 or mes == 6 or mes == 7 or mes == 8 or \
       mes == 9:
        m = "0" + str(mes)
    else:
        m = str(mes)        
    a = str(anio)

    fecha = d+"/"+m+"/"+a
    llave = 0
    valor = 0
    romper = True
    j = 0
    while j < len(zm4) and romper == True:
        intervalo = intervalo_Fechas(zm4[j][0], zm4[j][1], zm4[j][2], zm4[j][3], zm4[j][4], zm4[j][5])
        i = 0
        salir = True
        while i < len(intervalo) and salir == True:
            if fecha in intervalo:
                salir = False
                valor = 4
                llave = -1
            i += 1              
        if salir == False:
            romper = False
        j += 1
    if llave != -1:
        romper = True
        j = 0    
        while j < len(zm3) and romper == True:
            intervalo = intervalo_Fechas(zm3[j][0], zm3[j][1], zm3[j][2], zm3[j][3], zm3[j][4], zm3[j][5])
            i = 0
            salir = True
            while i < len(intervalo) and salir == True:
                if fecha in intervalo:
                    salir = False
                    valor = 3
                    llave = -1
                i += 1              
            if salir == False:
                romper = False
            j += 1    
    if llave != -1:       
        romper = True
        j = 0
        while j < len(zm2) and romper == True:
            intervalo = intervalo_Fechas(zm2[j][0], zm2[j][1], zm2[j][2], zm2[j][3], zm2[j][4], zm2[j][5])
            i = 0
            salir = True
            while i < len(intervalo) and salir == True:
                if fecha in intervalo:
                    salir = False
                    if prov in provincias:
                        valor = 3
                    else:
                        valor = 2    
                i += 1              
            if salir == False:
                romper = False
            j += 1
    return valor


# Funcion que dado la fecha y hora de un determinado evento, devuelve el dia Juliano considerando la fraccion de dia.
# La fraccion de dia tiene que ver con las horas que han pasado desde que comenzo el dia.
def fecha_Gregoriano_a_Dia_Juliano(dia, mes, anio, horas, minutos, segundos):
    fraccion_de_dia = (convertHorasMinutosSegundos_a_HorasDecimales(horas, minutos, segundos) / 24) + dia
    if mes == 1 or mes == 2:
        anio = anio - 1
        mes = mes + 12
    if anio == 1582 and mes == 10 and (dia >= 16 and dia <= 31):
        A = math.trunc(anio/100)
        B = 2 - A + math.trunc(A/4)
    elif anio == 1582 and mes == 10 and dia == 15:
        B = 0
    elif anio == 1582 and (mes == 11 or mes == 12):
        A = math.trunc(anio/100)
        B = 2 - A + math.trunc(A/4)        
    elif anio == 1582 and (mes == 9 or mes == 8 or mes == 7 or mes == 6 or mes == 5 or mes == 4 or \
                           mes == 3 or mes == 2 or mes == 1):
        B = 0
    elif anio > 1582:
        A = math.trunc(anio/100)
        B = 2 - A + math.trunc(A/4)  
    elif anio < 1582:
        B = 0    
    if anio < 0:
        C = math.trunc((365.25 * anio) - 0.75)
    else:
        C = math.trunc(365.25 * anio)
    D = math.trunc(30.6001 * (mes + 1))
    diaJuliano = B + C + D + fraccion_de_dia + 1720994.5
    return diaJuliano


# Funcion que, dada una fecha,  devuelve el Tiempo Sideral en Greenwich a las 00hs.
def GST00hs(dia, mes, anio):
    A = 0
    diaJuliano_en_Greenwich_00hs = fecha_Gregoriano_a_Dia_Juliano(dia, mes, anio, 0, 0, 0)
    S = diaJuliano_en_Greenwich_00hs - 2451545.0
    T = S / 36525.0
    T0 = 6.697374558 + (2400.051336 * T) + (0.000025862 * (T ** 2))
    if T0 < 0 or T0 > 24:
        T0 = rango0a23(T0)
    return T0

"""
# Funcion que calcula el Ascendente dadas la ARMC y la Latitud del lugar de nacimiento.
# La ARMC y la Latitud deben estar en grados decimales.
def calculoAscendente(armc, latitud):
    e = math.radians(23.4457889)
    ascencion90 = armc + 90
    Atan = math.tan(math.radians((armc + 90) / 2))
    # Latitudes Norte: le sumo 90 a la variable latitud y le restamos 23.4372
    # Latitudes Sur: le resto 90 a la variable latitud y le sumamos 23.4372
    Blat1 = math.radians(((latitud - 90) + e) / 2)
    Blat1Seno = math.sin(Blat1)
    Blat1Coseno = math.cos(Blat1)
    # Latitudes Norte: le sumo 90 a la variable latitud y le sumamos 23.4372
    # Latitudes Sur: le resto 90 a la variable latitud y le restamos 23.4372
    Blat2 = math.radians(((latitud - 90) - e) / 2)
    Blat2Seno = math.sin(Blat2)
    Blat2Coseno = math.cos(Blat2)
    divSenos = Blat1Seno / Blat2Seno
    divCosenos = Blat1Coseno / Blat2Coseno
    multiTanSen = Atan * divSenos
    multiTanCos = Atan * divCosenos
    arctanMultiTanSen = math.atan(multiTanSen)
    arctanMultiTanCos = math.atan(multiTanCos)
    gradosTanSen = math.degrees(arctanMultiTanSen)
    gradosTanCos = math.degrees(arctanMultiTanCos)
    sumaGrados = gradosTanSen + gradosTanCos
    if sumaGrados < 0:
        sumaGrados = sumaGrados + 360
    return sumaGrados
"""

# Funcion que calcula el Medio Cielo y el Ascendente, dada una fecha, hora, longitud y latitud.
def calculoARMC_MC_ASC_LatDeci(dia, mes, anio, horas, minutos, segundos, longGrad, longMin, \
                                           longSeg, latGrad, latMin, latSeg, provincia):

    # Funcion que realiza una correccion pequeña para pasar de Tiempo Solar a Tiempo Sidereo.
    def correccionAditivaTS_a_TSid(horasTUGreen, minTUGreen, segTUGreen):
        horasDecimalTUGreenwich = convertHorasMinutosSegundos_a_HorasDecimales(horasTUGreen, minTUGreen, segTUGreen)
        r1 = horasDecimalTUGreenwich * 9.856
        parteDecimal, parteEntera = math.modf(r1 / 60)
        m = parteEntera
        s = round(parteDecimal * 60, 3)
        return convertHorasMinutosSegundos_a_HorasDecimales(0, m, s)

    # ----------------------------------------------------------------------------------------------------

    e = math.radians(23.4457889)
    hd = convertHorasMinutosSegundos_a_HorasDecimales(horas, minutos, segundos)
    zonaHoraria = zonasHorariasArgentina(dia, mes, anio, provincia)
    # Obtenemos el GMT o TU
    GMT = hd + zonaHoraria
    # Estos if se ejecutan cuando el GMT da mayor a 24hs indicando eso que ya nos pasamos al dia siguiente.
    # Y el dia siguiente es el que debemos utilizar para realizar los calculos siguientes.
    if GMT >= 24:
        GMT = GMT - 24
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia >= 1 and dia <= 29:
                dia = dia + 1
            elif dia == 30:
                dia = 1
                mes = mes + 1
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10:
            if dia >= 1 and dia <= 30:
                dia = dia + 1
            elif dia == 31:
                dia = 1
                mes = mes + 1
        elif mes == 12:
            if dia >= 1 and dia <= 30:
                dia = dia + 1
            elif dia == 31:
                dia = 1
                mes = 1
                anio = anio + 1
        elif mes == 2 and esBisiesto(anio) == True:
            if dia >= 1 and dia <= 28:
                dia = dia + 1
            elif dia == 29:
                dia = 1
                mes = mes + 1
        elif mes == 2 and esBisiesto(anio) == False:
            if dia >= 1 and dia <= 27:
                dia = dia + 1
            elif dia == 28:
                dia = 1
                mes = mes + 1

    # ----------------------------------------------------------------------------------------------------
    
    # Tiempo Sideral en Greenwich a las 00hs. Este valor generalmente se obtiene de las tablas de Efemerides.
    TS = GST00hs(dia, mes, anio)
    
    # ----------------------------------------------------------------------------------------------------

    # Obtenemos la TLS que es el Tiempo Sidereo Local
    GMT_hms = convertHorasDecimales_a_HorasMinutosSegundos(GMT)
    correccionAditiva = correccionAditivaTS_a_TSid(GMT_hms[0], GMT_hms[1], GMT_hms[2]) # Este resultado debe ser < 4
    longEnTiempo = convertGradosMinutosSegundos_a_GradosDecimales(longGrad, longMin, longSeg) / 15
    # Longitud Oeste ---> restamos longEnTiempo
    # Longitud Este ---> sumamos longEnTiempo
    TLS = GMT + TS + correccionAditiva - longEnTiempo
    if TLS >= 24:                                       
        TLS = TLS - 24

    # ----------------------------------------------------------------------------------------------------
    
    # La Ascencion Recta del Medio Cielo (ARMC) es el TLS convertida a grados.
    ARMC = TLS * 15
    # ----------------------------------------------------------------------------------------------------
    
    # Calculo del MC
    tanARMC = math.tan(math.radians(ARMC))
    cosOE = math.cos(e)
    A = tanARMC / cosOE
    longMC = math.degrees(math.atan(A))
    if TLS >= 6 and TLS < 18:
        MC = longMC + 180
    elif TLS >= 18 and TLS < 23.99999999999:
        MC = longMC + 360 
    else:
        MC = longMC

    # Calculo del Ascendente utilizando la formula de Giovanni Antonio Magini (Maginus)
    latDecimal = convertGradosMinutosSegundos_a_GradosDecimales(latGrad, latMin, latSeg)
    A = (math.sin(e) * math.tan(math.radians(latDecimal))) / math.cos(math.radians(ARMC))
    B = math.cos(e) * math.tan(math.radians(ARMC))
    # Hemisferio Sur: B - A; Hemisferio Norte: B + A
    LongAsc = math.degrees(arccotg(B - A))     
    if ARMC > 0 and ARMC < 90:
        ASC = 180 - LongAsc
    elif ARMC > 90 and ARMC < 180:   
        ASC = 360 - LongAsc
    elif ARMC > 180 and ARMC < 270:  
        ASC = 360 - LongAsc 
    elif ARMC > 270 and ARMC < 360:
        ASC = 180 - LongAsc

    return ARMC, MC, ASC, latDecimal, zonaHoraria, GMT, TS, TLS 


# Sistema Topocentrico para el calculo de las casas.
def sistemaTopocentrico(armc, mc, asc, latitud):
    # Hemisferio Sur ----> Latitudes negativas
    # Hemisferio Norte ----> Latitudes positivas
    latitud = latitud * (-1)
    l = math.radians(latitud)
    e = math.radians(23.4457889)
    H11 = math.radians(armc + 30)
    H12 = math.radians(armc + 60)
    H2 = math.radians(armc + 120)
    H3 = math.radians(armc + 150)
    P11 = math.atan(math.tan(l) / 3)
    P12 = math.atan(2 * (math.tan(l) / 3))
    P2 = math.atan(2 * (math.tan(l) / 3))
    P3 = math.atan(math.tan(l) / 3)
    M11 = math.atan(math.tan(P11) / math.cos(H11))
    M12 = math.atan(math.tan(P12) / math.cos(H12))
    M2 = math.atan(math.tan(P2) / math.cos(H2))
    M3 = math.atan(math.tan(P3) / math.cos(H3))
    R11 = math.degrees(math.atan((math.tan(H11) * math.cos(M11)) / math.cos(M11 + e)))
    R12 = math.degrees(math.atan((math.tan(H12) * math.cos(M12)) / math.cos(M12 + e)))
    R2 = math.degrees(math.atan((math.tan(H2) * math.cos(M2)) / math.cos(M2 + e)))
    R3 = math.degrees(math.atan((math.tan(H3) * math.cos(M3)) / math.cos(M3 + e)))
    C10 = mc
    C1 = asc
    if armc > 0 and armc < 90:
        C2 = R2 + 180
        C3 = R3 + 180
        if R11 < 0:
            C11 = R11 + 180
        else:
            C11 = R11
        if R12 < 0:
            C12 = R12 + 180
        else:
            C12 = R12
    elif armc > 90 and armc < 180:
        if R2 > 0:
            C2 = R2 + 180
        else:
            C2 = R2 + 360
        if R3 > 0:
            C3 = R3 + 180
        else:
            C3 = R3 + 360
        C11 = R11 + 180
        C12 = R12 + 180
    elif armc > 180 and armc < 270:
        if R2 < 0:
            C2 = R2 + 360
        else:
            C2 = R2
        if R3 < 0:
            C3 = R3 + 360
        else:
            C3 = R3
        if R11 > 0:
            C11 = R11 + 180
        else:
            C11 = R11 + 360
        if R12 > 0:
            C12 = R12 + 180
        else:
            C12 = R12 + 360
    elif armc > 270 and armc < 360:
        if R2 < 0:
            C2 = R2 + 180
        else:
            C2 = R2
        if R3 < 0:
            C3 = R3 + 180
        else:
            C3 = R3
        if R11 < 0:
            C11 = R11 + 360
        else:
            C11 = R11
        if R12 < 0:
            C12 = R12 + 360
        else:
            C12 = R12
    C7 = C1 + 180
    C8 = C2 + 180
    C9 = C3 + 180
    C4 = C10 + 180
    C5 = C11 + 180
    C6 = C12 + 180
    if C7 > 360:
        C7 = C7 - 360
    if C8 > 360:
        C8 = C8 - 360
    if C9 > 360:
        C9 = C9 - 360
    if C4 > 360:
        C4 = C4 - 360
    if C5 > 360:
        C5 = C5 - 360
    if C6 > 360:
        C6 = C6 - 360
    return C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12


# Sistema Regiomontanus para el calculo de las casas.
def sistemaRegiomontanus(armc, mc, asc, latitud):
    # Hemisferio Sur ----> Latitudes negativas
    # Hemisferio Norte ----> Latitudes positivas 
    latitud = latitud * (-1)
    l = math.radians(latitud)
    e = math.radians(23.4457889)
    H11 = math.radians(30)
    H12 = math.radians(60)
    H2 = math.radians(120)
    H3 = math.radians(150)
    F11 = math.radians(armc) + H11
    F12 = math.radians(armc) + H12
    F2 = math.radians(armc) + H2
    F3 = math.radians(armc) + H3
    P11 = math.atan(math.tan(l) * math.sin(H11))
    P12 = math.atan(math.tan(l) * math.sin(H12))
    P2 = math.atan(math.tan(l) * math.sin(H2))
    P3 = math.atan(math.tan(l) * math.sin(H3))
    M11 = math.atan(math.tan(P11) / math.cos(F11))
    M12 = math.atan(math.tan(P12) / math.cos(F12))
    M2 = math.atan(math.tan(P2) / math.cos(F2))
    M3 = math.atan(math.tan(P3) / math.cos(F3))
    R11 = math.degrees(math.atan((math.tan(F11) * math.cos(M11)) / math.cos(M11 + e))) 
    R12 = math.degrees(math.atan((math.tan(F12) * math.cos(M12)) / math.cos(M12 + e)))
    R2 = math.degrees(math.atan((math.tan(F2) * math.cos(M2)) / math.cos(M2 + e)))
    R3 = math.degrees(math.atan((math.tan(F3) * math.cos(M3)) / math.cos(M3 + e)))
    C10 = mc
    C1 = asc
    if armc > 0 and armc < 90:
        C2 = R2 + 180
        C3 = R3 + 180
        if R11 < 0:
            C11 = R11 + 180
        else:
            C11 = R11
        if R12 < 0:
            C12 = R12 + 180
        else:
            C12 = R12
    elif armc > 90 and armc < 180:
        if R2 > 0:
            C2 = R2 + 180
        else:
            C2 = R2 + 360
        if R3 > 0:
            C3 = R3 + 180
        else:
            C3 = R3 + 360
        C11 = R11 + 180
        C12 = R12 + 180
    elif armc > 180 and armc < 270:
        if R2 < 0:
            C2 = R2 + 360
        else:
            C2 = R2
        if R3 < 0:
            C3 = R3 + 360
        else:
            C3 = R3
        if R11 > 0:
            C11 = R11 + 180
        else:
            C11 = R11 + 360
        if R12 > 0:
            C12 = R12 + 180
        else:
            C12 = R12 + 360
    elif armc > 270 and armc < 360:
        if R2 < 0:
            C2 = R2 + 180
        else:
            C2 = R2
        if R3 < 0:
            C3 = R3 + 180
        else:
            C3 = R3
        if R11 < 0:
            C11 = R11 + 360
        else:
            C11 = R11
        if R12 < 0:
            C12 = R12 + 360
        else:
            C12 = R12
    C7 = C1 + 180
    C8 = C2 + 180
    C9 = C3 + 180
    C4 = C10 + 180
    C5 = C11 + 180
    C6 = C12 + 180
    if C7 > 360:
        C7 = C7 - 360
    if C8 > 360:
        C8 = C8 - 360
    if C9 > 360:
        C9 = C9 - 360
    if C4 > 360:
        C4 = C4 - 360
    if C5 > 360:
        C5 = C5 - 360
    if C6 > 360:
        C6 = C6 - 360
    return C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12


def limpiar():
    titulo.config(text="")
    nombre.config(text="")    
    dia.config(text="")
    mes.config(text="")
    anio.config(text="")
    horas.config(text="")
    minutos.config(text="")
    segundos.config(text="")
    provincia.config(text="")
    departamento.config(text="")
    localidad.config(text="")        


def campo_Departamento_select(event):
    campo_departamento["state"] = "readonly"
    list_prov_dpto = []
    list_dptos = []
    for elem in tabla:
        if (elem[4], elem[3]) not in list_prov_dpto:
            list_prov_dpto = list_prov_dpto + [(elem[4], elem[3])]
    i = 0
    while i < len(list_prov_dpto):
        if list_prov_dpto[i][0] == campo_provincia.get():
            list_dptos = list_dptos + [list_prov_dpto[i][1]]
        i += 1
    campo_departamento.config(values=sorted(list_dptos))
    campo_provincia["state"] = "disable"

def campo_Localidad_select(event):
    campo_localidad["state"] = "readonly"
    list_dpto_loc = []
    list_loc = []
    for elem in tabla:
        if (elem[4], elem[3], elem[0]) not in list_dpto_loc:
            list_dpto_loc = list_dpto_loc + [(elem[4], elem[3], elem[0])]        
    i = 0
    while i < len(list_dpto_loc):
        if list_dpto_loc[i][0] == campo_provincia.get() and list_dpto_loc[i][1] == campo_departamento.get():
            list_loc = list_loc + [list_dpto_loc[i][2]]
        i += 1
    campo_localidad.config(values=sorted(list_loc))
    campo_departamento["state"] = "disable"

def ventana2():
    cNombre = campo_nombre.get().upper()
    cDia = campo_dia.get()
    cMes = campo_mes.get()
    cAnio = campo_anio.get()
    cHoras = campo_horas.get()
    cMinutos = campo_minutos.get()
    cSegundos = campo_segundos.get()
    cProvincia = campo_provincia.get()
    cDepartamento = campo_departamento.get()
    cLocalidad = campo_localidad.get()
    if cNombre != "" and cDia != "" and cMes != "" and cAnio != "" and cHoras != "" and cMinutos != "" and cSegundos != "" and cProvincia != "" and cDepartamento != "" and cLocalidad != "":
        i = 0
        lat = 0
        long = 0
        while i < len(tabla):
            elem = tabla[i]
            if elem[4] == cProvincia and elem[3] == cDepartamento and elem[0] == cLocalidad:
                lat = elem[1]
                long = elem[2]
                break
            i += 1
        # Multiplicamos por -1 porque las latitudes y longitudes de la tabla estan negativos
        # y nuestras funciones de calculos trabajan con latitudes y longitudes positivas donde
        # pasan a negativas en el momento oportuno.
        lat = lat * (-1)
        long = long * (-1)
        gmsLat = convertGradosDecimales_a_GradosMinutosSegundos(lat)
        gmsLong = convertGradosDecimales_a_GradosMinutosSegundos(long)
            
        calculos = calculoARMC_MC_ASC_LatDeci(int(cDia), int(cMes), int(cAnio), int(cHoras), int(cMinutos), int(cSegundos), gmsLong[0], gmsLong[1], gmsLong[2], gmsLat[0], gmsLat[1], gmsLat[2], cProvincia)
            
        calculoCasasTopocentrico = sistemaTopocentrico(calculos[0], calculos[1], calculos[2], calculos[3])
        calculoCasasRegiomontanus = sistemaRegiomontanus(calculos[0], calculos[1], calculos[2], calculos[3])

        campo_nombre.destroy()
        campo_dia.destroy()
        campo_mes.destroy()
        campo_anio.destroy()
        campo_horas.destroy()
        campo_minutos.destroy()
        campo_segundos.destroy()
        campo_provincia.destroy()
        campo_departamento.destroy()
        campo_localidad.destroy()
        enviar.destroy()
        salir.destroy()
        
        limpiar()  

        titulo2 = Label(ventana, text="Resultados", fg="blue2", bg="Gray2", font=("Verdana", 27))
        nombre2 = Label(ventana, text="Nombre:  "+cNombre, bg="Gray2", fg="red", font=("Verdana", 12))
        fecha = Label(ventana, text="Fecha de Nacimiento:  "+cDia+"/"+cMes+"/"+cAnio, fg="red", bg="Gray2", font=("Verdana", 12))
        hora = Label(ventana, text="Hora de Nacimiento:  "+cHoras+"hs:"+cMinutos+"m:"+cSegundos+"s", bg="Gray2", fg="red", font=("Verdana", 12))
        pais = Label(ventana, text="Pais:  ARGENTINA", bg="Gray2", fg="red", font=("Verdana", 12))
        provincia = Label(ventana, text="Provincia:  "+cProvincia, bg="Gray2", fg="red", font=("Verdana", 12))
        departamento = Label(ventana, text="Departamento:  "+cDepartamento, bg="Gray2", fg="red", font=("Verdana", 12))
        localidad = Label(ventana, text="Localidad:  "+cLocalidad, bg="Gray2", fg="red", font=("Verdana", 12))   

        latLoc = Label(ventana, text="Latitud:  "+str(gmsLat[0])+"°"+str(gmsLat[1])+"'"+str(gmsLat[2])+'"'+"S", bg="Gray2", fg="red", font=("Verdana", 12))
        longLoc =Label(ventana, text="Longitud:  "+str(gmsLong[0])+"°"+str(gmsLong[1])+"'"+str(gmsLong[2])+'"'+"O", bg="Gray2", fg="red", font=("Verdana", 12)) 
        zonaH = Label(ventana, text="Zona Horaria:  "+"-"+str(calculos[4])+"hs", bg="Gray2", fg="red", font=("Verdana", 12))
        diaJ = Label(ventana, text="Dia Juliano:  "+str(round(fecha_Gregoriano_a_Dia_Juliano(int(cDia), int(cMes), int(cAnio),  int(cHoras), int(cMinutos), int(cSegundos)), 4)), bg="Gray2", fg="orange", font=("Verdana", 12))
        tuS = convertHorasDecimales_a_HorasMinutosSegundos(calculos[5])
        _tu = Label(ventana, text="TU (GMT):  "+str(tuS[0])+"hs:"+str(tuS[1])+"m:"+str(tuS[2])+"s", bg="Gray2", fg="orange", font=("Verdana", 12))
        gstS = convertHorasDecimales_a_HorasMinutosSegundos(calculos[6])
        _gst = Label(ventana, text="GST:  "+str(gstS[0])+"hs:"+str(gstS[1])+"m:"+str(gstS[2])+"s", bg="Gray2", fg="orange", font=("Verdana", 12))
        tlsS = convertHorasDecimales_a_HorasMinutosSegundos(calculos[7]) 
        _tls = Label(ventana, text="TLS:  "+str(tlsS[0])+"hs:"+str(tlsS[1])+"m:"+str(tlsS[2])+"s", bg="Gray2", fg="orange", font=("Verdana", 12))
        armcS = convertGradosDecimales_a_GradosMinutosSegundos(calculos[0])
        _armc = Label(ventana, text="ARMC:  "+str(armcS[0])+"°"+str(armcS[1])+"'"+str(armcS[2])+'"', bg="Gray2", fg="orange", font=("Verdana", 12))
        mcS = convertGradosDecimales_a_GradosMinutosSegundos(calculos[1]) 
        _mc = Label(ventana, text="MC:  "+str(mcS[0])+"°"+str(mcS[1])+"'"+str(mcS[2])+'"', bg="Gray2", fg="orange", font=("Verdana", 12))
        ascS = convertGradosDecimales_a_GradosMinutosSegundos(calculos[2])
        _asc = Label(ventana, text="ASC:  "+str(ascS[0])+"°"+str(ascS[1])+"'"+str(ascS[2])+'"', bg="Gray2", fg="orange", font=("Verdana", 12))
        
        titulo2.grid(row=0, column=1, pady=0, sticky=(N, S, E, W))
        nombre2.grid(row=1, column=0, pady=3, padx=3, sticky="W")    
        fecha.grid(row=2, column=0, pady=3, padx=3, sticky="W")
        hora.grid(row=3,  column=0, pady=3, padx=3, sticky="W")
        pais.grid(row=4, column=0, pady=3, padx=3, sticky="W")
        provincia.grid(row=5, column=0, pady=3, padx=3, sticky="W")
        departamento.grid(row=1, column=1, pady=3, padx=3, sticky="W")
        localidad.grid(row=2, column=1, pady=3, padx=3, sticky="W")
        latLoc.grid(row=3, column=1, pady=3, padx=3, sticky="W")
        longLoc.grid(row=4, column=1, pady=3, padx=3, sticky="W")
        zonaH.grid(row=5, column=1, pady=3, padx=3, sticky="W")
        diaJ.grid(row=1, column=2, pady=3, padx=3, sticky="W")
        _tu.grid(row=2, column=2, pady=3, padx=3, sticky="W")
        _gst.grid(row=3, column=2, pady=3, padx=3, sticky="W")
        _tls.grid(row=4, column=2, pady=3, padx=3, sticky="W")
        _armc.grid(row=5, column=2, pady=3, padx=3, sticky="W")
        _mc.grid(row=1, column=3, pady=3, padx=3, sticky="W")
        _asc.grid(row=2, column=3, pady=3, padx=3, sticky="W")

        titulo = Label(ventana, text="Sistema Topocentrico", fg="blue2", bg="black", font=("Verdana", 15))
        casa1 = Label(ventana, text="CASA 1 (ASC):  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[0]), bg="Gray2", fg="dark violet", font=("Verdana", 13))
        casa2 = Label(ventana, text="CASA 2:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[1]), bg="BLACK", fg="dark violet", font=("Verdana", 13))
        casa3 = Label(ventana, text="CASA 3:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[2]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa4 = Label(ventana, text="CASA 4:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[3]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa5 = Label(ventana, text="CASA 5:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[4]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa6 = Label(ventana, text="CASA 6:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[5]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa7 = Label(ventana, text="CASA 7:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[6]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa8 = Label(ventana, text="CASA 8:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[7]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa9 = Label(ventana, text="CASA 9:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[8]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa10 = Label(ventana, text="CASA 10 (MC):  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[9]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa11 = Label(ventana, text="CASA 11:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[10]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa12 = Label(ventana, text="CASA 12:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasTopocentrico[11]), bg="black", fg="dark violet", font=("Verdana", 13))
            
        titulo.grid(row=6, column=0, pady=3, sticky=(N, S, E, W))
        casa1.grid(row=7, column=0, pady=3, padx=3, sticky="W")
        casa2.grid(row=8,  column=0, pady=3, padx=3, sticky="W")
        casa3.grid(row=9, column=0, pady=3, padx=3, sticky="W")
        casa4.grid(row=10, column=0, pady=3, padx=3, sticky="W")
        casa5.grid(row=11, column=0, pady=3, padx=3, sticky="W")
        casa6.grid(row=12, column=0, pady=3, padx=3, sticky="W")
        casa7.grid(row=13, column=0, pady=3, padx=3, sticky="W")
        casa8.grid(row=14, column=0, pady=3, padx=3, sticky="W")
        casa9.grid(row=15, column=0, pady=3, padx=3, sticky="W")
        casa10.grid(row=16, column=0, pady=3, padx=3, sticky="W")
        casa11.grid(row=17, column=0, pady=3, padx=3, sticky="W")
        casa12.grid(row=18, column=0, pady=3, padx=3, sticky="W")

        titulo = Label(ventana, text="Sistema Regiomontanus", fg="blue2", bg="black", font=("Verdana", 15))
        casa1 = Label(ventana, text="CASA 1 (ASC):  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[0]), bg="Gray2", fg="dark violet", font=("Verdana", 13))
        casa2 = Label(ventana, text="CASA 2:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[1]), bg="BLACK", fg="dark violet", font=("Verdana", 13))
        casa3 = Label(ventana, text="CASA 3:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[2]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa4 = Label(ventana, text="CASA 4:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[3]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa5 = Label(ventana, text="CASA 5:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[4]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa6 = Label(ventana, text="CASA 6:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[5]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa7 = Label(ventana, text="CASA 7:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[6]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa8 = Label(ventana, text="CASA 8:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[7]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa9 = Label(ventana, text="CASA 9:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[8]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa10 = Label(ventana, text="CASA 10 (MC):  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[9]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa11 = Label(ventana, text="CASA 11:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[10]), bg="black", fg="dark violet", font=("Verdana", 13))
        casa12 = Label(ventana, text="CASA 12:  "+convertLongitudVerdadera_a_LongitudZodiacal(calculoCasasRegiomontanus[11]), bg="black", fg="dark violet", font=("Verdana", 13))

        titulo.grid(row=6, column=1, pady=3, sticky=(N, S, E, W))
        casa1.grid(row=7, column=1, pady=3, padx=3, sticky="W")
        casa2.grid(row=8,  column=1, pady=3, padx=3, sticky="W")
        casa3.grid(row=9, column=1, pady=3, padx=3, sticky="W")
        casa4.grid(row=10, column=1, pady=3, padx=3, sticky="W")
        casa5.grid(row=11, column=1, pady=3, padx=3, sticky="W")
        casa6.grid(row=12, column=1, pady=3, padx=3, sticky="W")
        casa7.grid(row=13, column=1, pady=3, padx=3, sticky="W")
        casa8.grid(row=14, column=1, pady=3, padx=3, sticky="W")
        casa9.grid(row=15, column=1, pady=3, padx=3, sticky="W")
        casa10.grid(row=16, column=1, pady=3, padx=3, sticky="W")
        casa11.grid(row=17, column=1, pady=3, padx=3, sticky="W")
        casa12.grid(row=18, column=1, pady=3, padx=3, sticky="W")
            
        salir2 = Button(ventana, text="Salir", fg="blue2", bg="Gray2", padx="30", pady="10", font=("Verdana", 15), command=ventana.destroy)
        salir2.grid(row=21, column=1, pady=7, padx=7, sticky=(N, S, E, W))    
    else:
        messagebox.showinfo(message="Hay campos vacios!!!. Complete todos los campos", title="ERROR!!!")

####################################### Programa Principal ##############################        

        
if __name__ == "__main__":
    ventana = Tk()
    ventana.title("AstroMaginus")
    # El codigo que sigue y que esta inhabilidato, centra una ventana en la pantalla
    # cuando la ventana a centrar es menor que el ancho y alto de la pantalla.
    """
    #anchoVentana = 900
    #altoVentana = 700
    #anchoPantalla = ventana.winfo_screenwidth()
    #altoPantalla = ventana.winfo_screenheight()
    #x = int((anchoPantalla / 2) - (anchoVentana / 2))
    #y = int((altoPantalla / 2) - (altoVentana / 2))
    #ventana.geometry("{}x{}+{}+{}".format(anchoVentana, altoVentana, x, y))
    """
    anchoPantalla = str(ventana.winfo_screenwidth())
    altoPantalla = str(ventana.winfo_screenheight())
    ventana.geometry(anchoPantalla+"x"+altoPantalla)    
    ventana.resizable(0,0)
    imagen = PhotoImage(file="Imagenes/img.png")
    fondo = Label(ventana, image=imagen).place(x=0, y=0)
    df = pd.read_csv("Localidades/localidades.csv", encoding="ISO-8859-1")
    tabla = df.values
    #----------------------------------------
    titulo = Label(ventana, text="Calculo de Casas", fg="blue2", bg="Gray2", font=("Verdana", 27))
    nombre = Label(ventana, text="Nombre: ", bg="Gray2", fg="white", font=("Verdana", 13))
    dia = Label(ventana, text="Dia: ", bg="Gray2", fg="white", font=("Verdana", 13))
    mes = Label(ventana, text="Mes: ", bg="Gray2", fg="white", font=("Verdana", 13))
    anio = Label(ventana, text="Año: ", bg="Gray2", fg="white", font=("Verdana", 13))
    horas = Label(ventana, text="Horas: ", bg="Gray2", fg="white", font=("Verdana", 13))
    minutos = Label(ventana, text="Minutos: ", bg="Gray2", fg="white", font=("Verdana", 13))
    segundos = Label(ventana, text="Segundos: ", bg="Gray2", fg="white", font=("Verdana", 13))
    provincia = Label(ventana, text="Provincia: ", bg="Gray2", fg="white", font=("Verdana", 13))
    departamento = Label(ventana, text="Departamento: ", bg="Gray2", fg="white", font=("Verdana", 13))
    localidad = Label(ventana, text="Localidad: ", bg="Gray2", fg="white", font=("Verdana", 13))

    titulo.grid(row=0, column=2, pady=3, sticky=(N, S, E, W))
    nombre.grid(row=1, column=0, pady=3, padx=3, sticky="W")
    dia.grid(row=2,  column=0, pady=3, padx=3, sticky="W")
    mes.grid(row=3, column=0, pady=3, padx=3, sticky="W")
    anio.grid(row=4, column=0, pady=3, padx=3, sticky="W")
    horas.grid(row=5, column=0, pady=3, padx=3, sticky="W")
    minutos.grid(row=6, column=0, pady=3, padx=3, sticky="W")
    segundos.grid(row=7, column=0, pady=3, padx=3, sticky="W")
    provincia.grid(row=8, column=0, pady=3, padx=3, sticky="W")
    departamento.grid(row=9, column=0, pady=3, padx=3, sticky="W")
    localidad.grid(row=10, column=0, pady=3, padx=3, sticky="W")
   
    campo_nombre = Entry(ventana)
    campo_nombre.focus_set()
    campo_dia = ttk.Combobox(state="readonly", width="3", values=list(range(1,32)))
    campo_mes = ttk.Combobox(state="readonly", width="3", values=list(range(1,13)))
    campo_anio = ttk.Combobox(state="readonly", width="6", values=list(range(1950, 2023)))
    campo_horas = ttk.Combobox(state="readonly", width="3", values=list(range(0,24)))
    campo_minutos = ttk.Combobox(state="readonly", width="3", values=list(range(0,60)))
    campo_segundos = ttk.Combobox(state="readonly", width="3", values=list(range(0,60)))
    lista_provincias = []
    for elem in tabla:
        if elem[4] not in lista_provincias:
            lista_provincias = lista_provincias + [elem[4]]
    campo_provincia = ttk.Combobox(state="readonly", width="40", values=sorted(lista_provincias))
    campo_departamento = ttk.Combobox(state="readonly", width="40")
    campo_localidad = ttk.Combobox(state="readonly", width="40")

    campo_nombre.grid(row=1, column=1, ipadx="75", sticky="W")
    campo_dia.grid(row=2, column=1, ipadx="1", sticky="W")
    campo_mes.grid(row=3, column=1, ipadx="1", sticky="W")
    campo_anio.grid(row=4, column=1,  ipadx="1", sticky="W")
    campo_horas.grid(row=5, column=1, ipadx="1", sticky="W")
    campo_minutos.grid(row=6, column=1, ipadx="1", sticky="W")
    campo_segundos.grid(row=7, column=1,  ipadx="1", sticky="W")
    campo_provincia.grid(row=8, column=1, ipadx="1", sticky="W")
    campo_departamento["state"] = "disable"
    campo_provincia.bind("<<ComboboxSelected>>", campo_Departamento_select)
    campo_departamento.grid(row=9, column=1, ipadx="1", sticky="W")
    campo_localidad["state"] = "disable"
    campo_departamento.bind("<<ComboboxSelected>>", campo_Localidad_select)
    campo_localidad.grid(row=10, column=1,  ipadx="1", sticky="W")
    # El  parametro command ejecutado como sigue a continuacion nos permite ejecutar varios metodos o funciones cuando el  usuario hace click en el Button:
    # command=lambda:[funcion1(), funcion2(), ....]  
    enviar = Button(ventana, text="Calcular", fg="blue2", bg="Gray2", padx="30", pady="10", font=("Verdana", 15), command=ventana2)  
    salir = Button(ventana, text="Salir", fg="blue2", bg="Gray2", padx="30", pady="10", font=("Verdana", 15), command=ventana.destroy)
    enviar.grid(row=11, column=1, pady=3, padx=3, sticky="W")
    salir.grid(row=11, column=1, pady=3, padx=3, sticky="E")
    ventana.mainloop()

   



