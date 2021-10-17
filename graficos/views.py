import pandas as pd
import numpy as np 
from django.shortcuts import render

# Create your views here.

def evolucion_directorio(request):
    datos=pd.read_csv('core/datos/evolucion_comuna.csv', decimal=',')

    urbanos=pd.read_csv('core/datos/evolucion_urbanos.csv', decimal=',')

    dependencia=pd.read_csv('core/datos/evolucion_por_depe.csv', decimal=',')
     

    datos=datos.sort_values('2020')
    dependencia=dependencia.sort_values('2020')

    context={
        'comunas':datos['nom_com_rbd'].to_list(),
        'data_2016':datos['2016'].to_list(),
        'data_2017':datos['2017'].to_list(),
        'data_2018':datos['2018'].to_list(),
        'data_2019':datos['2019'].to_list(),
        'data_2020':datos['2020'].to_list(),

       
        'urbanos_2016':urbanos['2016'].to_list(),
        'urbanos_2017':urbanos['2017'].to_list(),
        'urbanos_2018':urbanos['2018'].to_list(),
        'urbanos_2019':urbanos['2019'].to_list(),
        'urbanos_2020':urbanos['2020'].to_list(),

        'por_depe_2016':dependencia['2016'].to_list(),
        'por_depe_2017':dependencia['2017'].to_list(),
        'por_depe_2018':dependencia['2018'].to_list(),
        'por_depe_2019':dependencia['2019'].to_list(),
        'por_depe_2020':dependencia['2020'].to_list(),

        
        
    }

    return render(request,'modulos/informes/establecimientos/evolucion_directorio.html', context)

def sae(request):
     #datos de las comunas
    cupos_comunas=pd.read_csv('core/datos/vacantes_cupos_totales_por_comuna.csv')
    comunas=pd.read_csv('core/datos/tabla_comunas.csv' ,decimal=",")
    comunas_rural=pd.read_csv('core/datos/tabla_comunas_rural.csv' ,decimal=",")

    #datos de la ponderacion
    datos=pd.read_csv('core/datos/rbd_nom_cupos_vacante_ponderacion_total.csv' ,decimal=",")
    datos_decimal=pd.read_csv('core/datos/rbd_nom_cupos_vacante_ponderacion_total_tres.csv' ,decimal=",")

    #variables
        #variables de urbanidad ponderacion
    urbanos=datos[datos['RURAL_RBD']==0]
    rurales=datos[datos['RURAL_RBD']==1]

        #variable urbanidad comunas
    com_rural=comunas_rural[comunas_rural['RURAL_RBD']==1]
    com_urbana=comunas_rural[comunas_rural['RURAL_RBD']==0]
    
    #agrupacion 
    datos_urbanos=urbanos.groupby('ponderacion').count()
    datos_rurales=rurales.groupby('ponderacion').count()
    datos_globales=datos.groupby('ponderacion').count()

    #top de colegios
        #top menos vacantes
    datos_decimal_menos_vacantes=datos_decimal.sort_values('vacantes')
    top_menos_vacantes=datos_decimal_menos_vacantes[:10]
        #top menos ponderacion
        #top mas vacantes
        #top mas ponderacion


    context= {
       'datos_urbanos':datos_urbanos['rbd'] ,
       'datos_rurales':datos_rurales['rbd'] ,
       'datos_globales':datos_globales['rbd'] ,
       'eje_y':datos['ponderacion'].unique() ,

       'nom_com_rbd':comunas['NOM_COM_RBD'].to_list(),
       'ponderacion_comunas':comunas['ponderacion'].to_list(),

       'ponderacion_comuna_rural':com_rural['ponderacion'].to_list(),
       'ponderacion_comuna_urbana':com_urbana['ponderacion'].to_list(),

        #menos vacantes
        'nombres_menos_vacantes':top_menos_vacantes['NOM_RBD'].to_list(),
        'vacantes_menos_vacantes':top_menos_vacantes['vacantes'].to_list(),

        'nombre_cupos':cupos_comunas['NOM_COM_RBD'].to_list(),
        'cupo_comuna':cupos_comunas['cupos_totales'].to_list(),
        'vacante_comuna':cupos_comunas['vacantes'].to_list(),

   }



    return render(request,'modulos/informes/sae/sae_2020/graficos_sae.html', context)

def sae_demanda(request):
    datos=pd.read_csv('core/datos/demanda_comuna.csv', decimal=',')
    datos=datos.sort_values('rbd')
    datos_a=datos[:11]
    datos_b=datos[-3:]

    context={
        'comunas':datos['NOM_COM_RBD'].to_list(),
        'comunas_a':datos_a['NOM_COM_RBD'].to_list(),
        'comunas_b':datos_b['NOM_COM_RBD'].to_list(),

        'demanda':datos['rbd'].to_list(),
        'demanda_a':datos_a['rbd'].to_list(),
        'demanda_b':datos_b['rbd'].to_list()
    }

    return render(request, 'modulos/informes/sae/sae_2020/sae_demanda.html',context)

def directorio_2020(request):

    datos=pd.read_csv('core/datos/agrupado_rural.csv', decimal=',')
   

    urbano=datos[datos['RURAL_RBD']==0]
    rurales=datos[datos['RURAL_RBD']==1]


    context={
        'comunas':datos['NOM_COM_RBD'].unique(),
        'urbano':urbano['NOM_RBD'].to_list(),
        'rurales':rurales['NOM_RBD'].to_list(),

        
    }
    return render(request,'modulos/informes/establecimientos/directorio_2020.html', context)
    