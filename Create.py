import pandas as pd
import os
import numpy as np
from datetime import datetime

data= open("Datasets\\Data.csv","a")
data.write("Nombre_Archivo;Fecha\n")
data.close()

texto1="Cliente"
texto2= "Venta"
contenido = os.listdir('Datasets\\')
data= open("Datasets\\Data.csv","a")
data2= pd.read_csv("Datasets\\Data.csv", sep=";")


cargaC=0
cargaV=0
for archivo in contenido:
    if texto1.lower() in archivo.lower():
        if cargaC>=1:
            pass
        elif any(data2["Nombre_Archivo"]==archivo):
            pass
        else:
            Cliente= pd.read_csv(f"Datasets\\{archivo}", on_bad_lines='skip', sep=";")
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
            Cliente["Latitud"]=[x.replace(',','.') for x in Cliente["Latitud"]]
            Cliente["Latitud"]=pd.to_numeric(Cliente["Latitud"],errors="coerce")
            Cliente["Longitud"]=pd.to_numeric(Cliente["Longitud"],errors="coerce")
            Cliente["Longitud"]=Cliente["Longitud"].astype(float)
            Cliente["Latitud"]=Cliente["Latitud"].astype(float)

            Cliente["Nueva_Latitud"]=Cliente["Longitud"][(Cliente["Longitud"]>-45) & (Cliente["Longitud"]<-20)]
            Cliente["Nueva_Longitud"]=Cliente["Latitud"][Cliente["Latitud"]<-45]
            Cliente["Longitud"][(Cliente["Longitud"]>-45) & (Cliente["Longitud"]<-20)]=Cliente["Nueva_Longitud"]
            Cliente["Latitud"][Cliente["Latitud"]<-45]=Cliente["Nueva_Latitud"]
            Cliente.drop("Nueva_Longitud", axis=1,inplace=True)
            Cliente.drop("Nueva_Latitud", axis=1,inplace=True)

            Cliente.drop_duplicates(inplace=True)

            Cliente.to_csv("Datasets\\Cliente_Total.csv", index=True, sep=";")

            renglon=f"{archivo};{datetime.now()}\n"
            renglon2= f"Cliente_Total.csv;{datetime.now()}\n"
            data.write(renglon)
            data.write(renglon2)
            print(f"Actualizado {archivo}")

            cargaC+=1
        
    elif texto2.lower() in archivo.lower():
        if cargaV>=1:
            pass
        elif any(data2["Nombre_Archivo"]==archivo):
            pass
        else:
            Venta= pd.read_csv(f"Datasets\\{archivo}")
            Venta.loc[Venta["Precio"].isna(),"Precio"]=0
            Venta.loc[Venta["Cantidad"].isna(),"Cantidad"]=1
            Venta.set_index("IdVenta", inplace=True)

            Venta.drop_duplicates(inplace=True)

            Venta.to_csv("Datasets\\Venta_Total.csv", index=True, sep=",")

            renglon=f"{archivo};{datetime.now()}\n"
            data.write(renglon)
            renglon=f"Venta_Total.csv;{datetime.now()}\n"
            data.write(renglon)
            print(f"Actualizado {archivo}")

            cargaV+=1

data.close()