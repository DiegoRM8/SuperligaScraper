# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Bibliotecas

from bs4 import BeautifulSoup
import requests

import pandas as pd

#### URL's  para obtener la información deseada

URL_1 = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/' #URL  de la clasificación de España

URL_2 = 'https://resultados.as.com/resultados/futbol/alemania/clasificacion/' #URL  de la clasificación de Alemania

URL_3 = 'https://resultados.as.com/resultados/futbol/italia/clasificacion/' #URL  de la clasificación de Italia

URL_4 = 'https://resultados.as.com/resultados/futbol/inglaterra/clasificacion/' #URL  de la clasificación de Inglaterra

URL_5 = 'https://resultados.as.com/resultados/futbol/francia/clasificacion/' #URL  de la clasificación de Francia

URL_1_goles = 'https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/equipos/goles/' #URL  de los goles marcados en España

URL_2_goles = 'https://resultados.as.com/resultados/futbol/alemania/2020_2021/ranking/equipos/goles/' #URL  de los goles marcados en Alemania

URL_3_goles = 'https://resultados.as.com/resultados/futbol/italia/2020_2021/ranking/equipos/goles/' #URL  de los goles marcados en Italia

URL_4_goles = 'https://resultados.as.com/resultados/futbol/inglaterra/2020_2021/ranking/equipos/goles/' #URL  de los goles marcados en Inglaterra

URL_5_goles = 'https://resultados.as.com/resultados/futbol/francia/2020_2021/ranking/equipos/goles/' #URL  de los goles marcados en Francia

URL_1_goles_recibidos = 'https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/equipos/goles-encajados/' #URL  de los goles recbidos en España

URL_2_goles_recibidos = 'https://resultados.as.com/resultados/futbol/alemania/2020_2021/ranking/equipos/goles-encajados/' #URL  de los goles recbidos en Alemania

URL_3_goles_recibidos = 'https://resultados.as.com/resultados/futbol/italia/2020_2021/ranking/equipos/goles-encajados/' #URL  de los goles recbidos en Italia

URL_4_goles_recibidos = 'https://resultados.as.com/resultados/futbol/inglaterra/2020_2021/ranking/equipos/goles-encajados/' #URL  de los goles recbidos en Inglaterra

URL_5_goles_recibidos = 'https://resultados.as.com/resultados/futbol/francia/2020_2021/ranking/equipos/goles-encajados/' #URL  de los goles recbidos en Francia

URL_1_posesion = 'https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/equipos/porcentaje-de-posesion/' #URL  de la posesión en España

URL_2_posesion = 'https://resultados.as.com/resultados/futbol/alemania/2020_2021/ranking/equipos/porcentaje-de-posesion/' #URL  de la posesión en Alemania

URL_3_posesion = 'https://resultados.as.com/resultados/futbol/italia/2020_2021/ranking/equipos/porcentaje-de-posesion/' #URL  de la posesión en Italia

URL_4_posesion = 'https://resultados.as.com/resultados/futbol/inglaterra/2020_2021/ranking/equipos/porcentaje-de-posesion/' #URL  de la posesión en Inglaterra

URL_5_posesion = 'https://resultados.as.com/resultados/futbol/francia/2020_2021/ranking/equipos/porcentaje-de-posesion/' #URL  de la posesión en Francia



# Una vez definidas las URL's, el siguiente paso será crear las funciones para extraer la información deseada

# Función 1: Obtiene la clasificación de España, Alemania e Italia.
    
def funcion_1(URL, posiciones, equipos, puntos):
    
    # Se realiza la petición a la web
    req = requests.get(URL)
    # Se comprueba que la petición nos devuelve un Status Code = 200
    status_code = req.status_code
    
    if status_code == 200:
        
        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "html.parser")
    
        tablas = html.find_all('tr', {'class':'zone-top-1'})
    
        for i, tabla in enumerate(tablas):
            
            posiciones.append(int(tabla.find('span', {'class':'pos'}).getText()))
        
            equipos.append(tabla.find('span', {'class':'nombre-equipo'}).getText())
        
            puntos.append(tabla.find('td', {'class':'destacado'}).getText())
            
    else: 
        print("No se ha obtenido respuesta correcta de la URL: {}".format(URL))

# Función 2: obtiene la clasificación de Francia e Inglaterra

def funcion_2(URL, posiciones, equipos, puntos):
    
    # Se realiza la petición a la web
    req2 = requests.get(URL)
    # Se comprueba que la petición nos devuelve un Status Code = 200
    status_code2 = req2.status_code
    
    if status_code2 == 200:
        
        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html2 = BeautifulSoup(req2.text, "html.parser")
    
        equipos_premier = html2.find_all('span', {'class':'nombre-equipo'})
    
        posiciones_premier = html2.find_all('span', {'class':'pos'})
    
        puntos_premier = html2.find_all('td', {'class':'destacado'})
    
        lista_equipos = []
    
        lista_posiciones = []
    
        lista_puntos = []
    
        for i, equipo in enumerate(equipos_premier):
        
            lista_equipos.append(equipo.getText())
    
        for i, posicion in enumerate(posiciones_premier):
        
            lista_posiciones.append(posicion.getText())
        
        for i, punto in enumerate(puntos_premier):
        
            lista_puntos.append(punto.getText())
        
        for i in range (0,4):
        
            equipos.append(lista_equipos[i])
        
            puntos.append(lista_puntos[i])
        
            posiciones.append(lista_posiciones[i])
    
    else: 
        print("No se ha obtenido respuesta correcta de la URL: {}".format(URL))

#Función 3: Obtiene los goles marcados y recibidos, así como la posesión de los equipos

def funcion_3(URL, goles_marcados, equipos_ranking):
    # Realizamos la petición a la segunda web
    req5 = requests.get(URL)
    
    # Comprobamos que la petición nos devuelve un Status Code = 200
    status_code5 = req5.status_code
    
    if status_code5 == 200 :

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html5 = BeautifulSoup(req5.text, "html.parser")
    
        ranking = html5.find('div', {'class':'rankings-table cf'})
      
        tr_ranking_body = ranking.find('tbody')
    
        tr_ranking = tr_ranking_body.find_all('tr')
        
        for i, tr in enumerate(tr_ranking):
        
            tr_equipo = tr.find('span', {'class':'name'}).getText()
        
            tr_goles_marcados = tr.find('td', {'class':'cantidad'}).getText()
        
            if tr_equipo in equipos:
                
                equipos_ranking.append(tr_equipo)
            
                goles_marcados.append(tr_goles_marcados[0:2])

    else: 
        print("No se ha obtenido respuesta correcta de la URL: {}".format(URL))

posiciones = []

equipos = []

puntos = []

goles_marcados = []

equipos_ranking = []

funcion_1(URL_1, posiciones, equipos, puntos) #Se extrae la información de la primera URL
funcion_1(URL_2, posiciones, equipos, puntos) #Se extrae la información de la segunda URL
funcion_1(URL_3, posiciones, equipos, puntos) #Se extrae la información de la tercera URL

funcion_2(URL_4, posiciones, equipos, puntos) #Se extrae la información de la cuarta URL
funcion_2(URL_5, posiciones, equipos, puntos) #Se extrae la información de la quinta URL

paises = []
lista_paises = ['España', 'Alemania', 'Italia', 'Inglaterra', 'Francia']
for i in range(0,5):
    for j in range(0,4):
        
        paises.append(lista_paises[i])

#Una vez se ha extraído la información deseada de las URL's, se almacenará en un dataframe para poder realizar análisis sobre ella.

dataframe = pd.DataFrame()

dataframe['Posicion'] = posiciones
dataframe['Equipo'] = equipos
dataframe['Puntos'] = puntos
dataframe['Pais'] = paises

# Se obtienen los goles marcados por cada equipo y se almacena en un dataframe.

funcion_3(URL_1_goles, goles_marcados, equipos_ranking)
funcion_3(URL_2_goles, goles_marcados, equipos_ranking)
funcion_3(URL_3_goles, goles_marcados, equipos_ranking)
funcion_3(URL_4_goles, goles_marcados, equipos_ranking)
funcion_3(URL_5_goles, goles_marcados, equipos_ranking)

dataframe_ranking = pd.DataFrame()

dataframe_ranking['Equipo'] = equipos_ranking

dataframe_ranking['GolesMarcados'] = goles_marcados

# Se unen ambos dataframes cuando haya coincidencia en el campo 'Equipos'

dataframe = dataframe.join(dataframe_ranking.set_index('Equipo'), on='Equipo')

# Se obtienen los goles recibidos de cada equipo y se almacena en un dataframe.

goles_recibidos = []

equipos_goles_recibidos = []

funcion_3(URL_1_goles_recibidos, goles_recibidos, equipos_goles_recibidos)
funcion_3(URL_2_goles_recibidos, goles_recibidos, equipos_goles_recibidos)
funcion_3(URL_3_goles_recibidos, goles_recibidos, equipos_goles_recibidos)
funcion_3(URL_4_goles_recibidos, goles_recibidos, equipos_goles_recibidos)
funcion_3(URL_5_goles_recibidos, goles_recibidos, equipos_goles_recibidos)

dataframe_goles_recibidos = pd.DataFrame()

dataframe_goles_recibidos['Equipo'] = equipos_goles_recibidos

dataframe_goles_recibidos['GolesRecibidos'] = goles_recibidos

# Se unen ambos dataframes cuando haya coincidencia en el campo 'Equipos'

dataframe = dataframe.join(dataframe_goles_recibidos.set_index('Equipo'), on='Equipo')

# Se obtiene la posesión de cada equipo y se almacena en un dataframe.

posesion = []

equipos_posesion = []

funcion_3(URL_1_posesion, posesion, equipos_posesion)
funcion_3(URL_2_posesion, posesion, equipos_posesion)
funcion_3(URL_3_posesion, posesion, equipos_posesion)
funcion_3(URL_4_posesion, posesion, equipos_posesion)
funcion_3(URL_5_posesion, posesion, equipos_posesion)

dataframe_posesion = pd.DataFrame()

dataframe_posesion['Equipo'] = equipos_posesion

dataframe_posesion['posesion %'] = posesion

# Se unen ambos dataframes cuando haya coincidencia en el campo 'Equipos'

dataframe = dataframe.join(dataframe_posesion.set_index('Equipo'), on='Equipo')

# Se ordena el dataframe de manera descendente respecto a la variable 'Puntos'

pd.to_numeric(dataframe['Puntos'])

dataframe = dataframe.sort_values('Puntos', ascending = False)

# Finalmente se guarda el dataframe obtenido como un csv.

dataframe.to_csv(r'\Users\USUARIO\Desktop\Master\Segundo_Cuatri\Tipología y ciclo\PEC2\clasificacion_csv', header = True, encoding='latin1')
