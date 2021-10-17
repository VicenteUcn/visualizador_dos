import pandas as pd

import numpy as np
from django.shortcuts import render

# Create your views here.

def inicio(request):

    coquimbo=pd.read_table('core/datos/coquimbo.csv', sep=',',decimal=",")

    exceso_oferta=pd.read_table('core/datos/EXC_OFERTA.csv', sep=';', decimal=".")
 
    total=exceso_oferta[exceso_oferta['EXC_OFERTA']=='100%']


    coquimbo['check']=coquimbo.RBD.isin(total.rbd)
    procesados=coquimbo[coquimbo['check']]

    latitud=procesados['LATITUD']
    longitud=procesados['LONGITUD']
    
    mylist = zip(latitud.to_list(), longitud.to_list())
    nombres=procesados['NOM_RBD'].to_list()

   

    datos=pd.read_csv('core/datos/rbd_nom_cupos_vacante_ponderacion_total.csv' ,decimal=",")
    urbanos=datos[datos['RURAL_RBD']==0]
    rurales=datos[datos['RURAL_RBD']==1]
    
    datos_urbanos=urbanos.groupby('ponderacion').count()
    datos_rurales=rurales.groupby('ponderacion').count()
    datos_globales=datos.groupby('ponderacion').count()

    context={ 'cord': mylist,'nombres':nombres,
    'datos_urbanos':datos_urbanos['rbd'] ,
       'datos_rurales':datos_rurales['rbd'] ,
       'datos_globales':datos_globales['rbd'] ,
       'eje_y':datos['ponderacion'].unique() ,}


       
    return render(request, 'modulos/inicio.html', context)