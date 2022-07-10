import pandas as pd
import os
import numpy as np
from datetime import datetime

texto1="Cliente"
texto2= "Venta"
contenido = os.listdir('C:\\Users\\Nacho\\Downloads\\HENRY\\Proyecto 1\\DS-PI-ProyectoIndividual\\Datasets\\')
data= open("Datasets\\Data.csv","a")
data2= pd.read_csv("C:\\Users\\Nacho\\Downloads\\HENRY\\Proyecto 1\\DS-PI-ProyectoIndividual\\Datasets\\Data.csv", sep=";")


for archivo in contenido:
    try:
        if texto1.lower() in archivo.lower():
            if any(data2["Nombre_Archivo"]==archivo):
                pass
            else:
                Cliente_total= pd.read_csv("C:\\Users\\Nacho\\Downloads\\HENRY\\Proyecto 1\\DS-PI-ProyectoIndividual\\Datasets\\Cliente_Total.csv", on_bad_lines='skip', sep=";")
                Cliente= pd.read_csv(f"C:\\Users\\Nacho\\Downloads\\HENRY\\Proyecto 1\\DS-PI-ProyectoIndividual\\Datasets\\{archivo}", on_bad_lines='skip', sep=";")
                
                Cliente=Cliente.drop("col10", axis=1)
                Cliente.columns=["ID","Provincia","Nombre_y_Apellido","Domicilio","Telefono","Edad","Localidad","Longitud","Latitud"]   

                Cliente["Provincia"].fillna("Sin Dato",inplace=True)
                Cliente["Nombre_y_Apellido"].fillna("Sin Dato",inplace=True)
                Cliente["Domicilio"].fillna("Sin Dato",inplace=True)
                Cliente["Telefono"].fillna("Sin Dato",inplace=True)
                Cliente["Localidad"].fillna("Sin Dato",inplace=True)
                Cliente["Latitud"].fillna("0.0",inplace=True)
                Cliente["Longitud"].fillna("0.0",inplace=True)

                for j in [2,3,6]:
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

                renglon=f"{archivo};{datetime.now()}\n"
                data.write(renglon)
                print(f"Actualizado {archivo}")


                Cliente_total=pd.concat([Cliente_total,Cliente], axis=0, ignore_index=True)
                Cliente_total.drop_duplicates(inplace=True)                
                Cliente_total.sort_values("ID", inplace=True)
                Cliente_total.set_index("ID", inplace=True)
                Cliente_total.to_csv("Datasets\\Cliente_total.csv", sep=";",index=True)
        elif texto2.lower() in archivo.lower():
            if any(data2["Nombre_Archivo"]==archivo):
                pass
            else:
                Venta_Total= pd.read_csv(f"C:\\Users\\Nacho\\Downloads\\HENRY\\Proyecto 1\\DS-PI-ProyectoIndividual\\Datasets\\Venta_Total.csv", sep=",")
                Venta= pd.read_csv(f"C:\\Users\\Nacho\\Downloads\\HENRY\\Proyecto 1\\DS-PI-ProyectoIndividual\\Datasets\\{archivo}",sep=",")
                Venta.loc[Venta["Precio"].isna(),"Precio"]=0
                Venta.loc[Venta["Cantidad"].isna(),"Cantidad"]=1
                renglon=f"{archivo};{datetime.now()}\n"
                data.write(renglon)
                print(f"Actualizado {archivo}")
        
                Venta_Total=pd.concat([Venta_Total,Venta], axis=0, ignore_index=True)
                Venta_Total.drop_duplicates(inplace=True)
                Venta_Total.sort_values("IdVenta", inplace=True)
                Venta_Total.set_index("IdVenta", inplace=True)
                Venta_Total.to_csv("Datasets\\Venta_Total.csv", sep=",",index=True)
    except:
        print(f"ERROR {archivo}")

data.close()