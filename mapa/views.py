import pandas as pd
import numpy as np
from django.shortcuts import render
# Create your views here.

def mapa(request):
    #directorio de coquimbo
    coquimbo=pd.read_table('core/datos/coquimbo.csv', sep=',',decimal=",")
    #el array a trabajar
    seleccion=[]
    cord=[]
    nombres_colegios=[]
    #array del select
    ciudades=coquimbo['NOM_COM_RBD'].unique()
    
    #Cuando es post
    if request.method == 'POST':
        #trabajar con una copia de coquimbo
        seleccion=coquimbo[:]
        
        #los options
        if request.POST.get('es_urbano') == 'urbano':
            seleccion=seleccion[seleccion['RURAL_RBD']==0]
            
        elif request.POST.get('es_urbano') == 'rural':
            seleccion=seleccion[seleccion['RURAL_RBD']==1]

        #Trabajar con las ciudades

        if  request.POST.getlist('ciudades', 'null') != 'null':
            
            lista_ciudades=request.POST.getlist('ciudades')

            terms = ['foo', 'baz']
            seleccion['check_ciudad']=seleccion['NOM_COM_RBD'].isin(lista_ciudades)
            seleccion=seleccion[seleccion['check_ciudad']]
       

           

        latitud=seleccion['LATITUD']
        longitud=seleccion['LONGITUD']

        cord=zip(latitud.to_list(), longitud.to_list())
        nombres_colegios=seleccion['NOM_RBD']
  

    context={ 'cord': cord,
            'nombres':nombres_colegios,
            'ciudades':ciudades}


    return render(request, 'modulos/mapa.html', context)