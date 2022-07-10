import pandas as pd
import os
import numpy as np
from datetime import datetime


data= open("Datasets\\Data.csv","a")
data.write("Nombre_Archivo;Fecha\n")
data.close()

texto1="Cliente"
texto2= "Venta"
contenido = os.listdir('C:\\Users\\Nacho\\Downloads\\HENRY\\Proyecto 1\\DS-PI-ProyectoIndividual\\Datasets\\')
data= open("Datasets\\Data.csv","a")
data2= pd.read_csv("C:\\Users\\Nacho\\Downloads\\HENRY\\Proyecto 1\\DS-PI-ProyectoIndividual\\Datasets\\Data.csv", sep=";")


for archivo in contenido:
    if texto1 in archivo:
        if any(data2["Nombre_Archivo"]==archivo):
            pass
        elif texto1 in archivo:
            Cliente= pd.read_csv("C:\\Users\\Nacho\\Downloads\\HENRY\\Proyecto 1\\DS-PI-ProyectoIndividual\\Datasets\\{archivo}", on_bad_lines='skip', sep=";")
            Cliente=Cliente.drop("col10", axis=1)
            Cliente.columns=["ID","Provincia","Nombre_y_Apellido","Domicilio","Telefono","Edad","Localidad","Longitud","Latitud"]   

            Cliente.set_index("ID", inplace=True)


            Cliente["Provincia"].fillna("Sin Dato",inplace=True)
            Cliente["Nombre_y_Apellido"].fillna("Sin Dato",inplace=True)
            Cliente["Domicilio"].fillna("Sin Dato",inplace=True)
            Cliente["Telefono"].fillna("Sin Dato",inplace=True)
            Cliente["Localidad"].fillna("Sin Dato",inplace=True)
            Cliente["Latitud"].fillna("0.0",inplace=True)
            Cliente["Longitud"].fillna("0.0",inplace=True)

            for j in [1,2,5]:
                for i in range(len(Cliente)):
                    Cliente.iloc[i,j]=Cliente.iloc[i,j].title()


            Cliente["Longitud"]=[x.replace(',',".") for x in Cliente["Longitud"]]
            Cliente["Latitud"]=[x.replace(',','.') for x in Cliente["Longitud"]]
            try:
                for i in Cliente.index:
                    float(Cliente["Longitud"][i])
            except:
                Cliente.loc[i,"Longitud"]=0
            try:
                for i in Cliente.index:
                    float(Cliente["Latitud"][i])
            except:
                Cliente.loc[i,"Latitud"]=0

            renglon=f"{archivo};{datetime.now()}\n"
            data.write(renglon)
            print("Actualizado")
    elif texto2 in archivo:
        if any(data2["Nombre_Archivo"]==archivo):
            pass
        elif texto2 in archivo:
            Venta= pd.read_csv("C:\\Users\\Nacho\\Downloads\\HENRY\\Proyecto 1\\DS-PI-ProyectoIndividual\\Datasets\\{archivo}")
            Venta.loc[Venta["Precio"].isna(),"Precio"]=0
            Venta.loc[Venta["Cantidad"].isna(),"Cantidad"]=1
            Venta.set_index("IdVenta", inplace=True)
            renglon=f"{archivo};{datetime.now()}\n"
            data.write(renglon)
            print("Actualizado")

data.close()
