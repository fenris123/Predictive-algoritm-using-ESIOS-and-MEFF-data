# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:39:59 2025

@author: fenris123
"""

import pandas as pd
import os
import datetime


# PASO 1  MONTAR EL DF DE DATOS HISTORICOS COMPLETOS.


df = pd.DataFrame()
carpeta = "C:\\Datos\\ESIOS" 

for fichero in os.listdir(carpeta):
    
    if fichero.endswith(".csv"):
        
        datos = pd.read_csv(f"C:\\Datos\\ESIOS\\{fichero}",sep=";")
        df = pd.concat([df,datos], ignore_index=True) 



df = df.drop(index=0).reset_index(drop=True)    #el primer dato eran las 23:00 del año 2018. No lo queremos.

 
 
#  PASO 2 AÑADIR COLUMNA CON DIA DE LA SEMANA        

df["dia_sem"] = ""
df["date"] = pd.to_datetime(df["date"])

 
def semana(fecha):
    return fecha.weekday() + 1


df["dia_sem"] = df["date"].apply(semana)



#  PASO 3: añadir los periodos 

df["periodo"] = ""
df["time"] = pd.to_datetime(df["time"],format="%H:%M:%S").dt.time


def periodo (row):
  
    dia_sem = row["dia_sem"]
    hora = row["time"]

    if (dia_sem in [6, 7]) or (datetime.time(0, 0) <= hora < datetime.time(8, 0)):
        return 3
    elif (datetime.time(10, 0) <= hora < datetime.time(14, 0)) or (datetime.time(18, 0) <= hora < datetime.time(22, 0)):
        return 2
    else:
        return 1
            
        
df["periodo"] = df.apply(periodo, axis=1)
