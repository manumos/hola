# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:01:02 2022

@author: Manuela
"""

#PRIMERA FUNCION
def download_pubmed(keyword):
    """Descargar la data de pubmed
            -Parametros
                keyword= string con el termino de busqueda
            -Output
                Lista que contiene los IDs de los resultados encontrados
    """
    
    #importar paquetes
    import Bio
    from Bio import Entrez as en
    from Bio import Medline as md
    
    #notificar correo
    en.email = "manuela.moscoso@est.ikiam.edu.ec.com"

    #definir termino de busqueda
    busqueda=keyword+"[Title/Abstract]"
    
    #realizar la busqueda
    handle= en.esearch(db="pubmed", term=busqueda)
    record = en.read(handle)
    return (record.get("IdList"))

#SEGUNDA FUNCION
def mining_pubs(keyword,tipo):
    """Generar data frames para las variables introducidas
            -Parametros
                keyword= string con el termino de busqueda
                tipo=Sring con el codigo para obtener infromacion especifica de cada resultado
                      'AD' = Afiliacion
                      'PD' = Fecha de publicacion
                      'AU' = Autores
            -Output
                *Si el tipo es "DP" recupera el año de publicación del artículo. El retorno es un dataframe con el PMID y el DP_year.
                *Si el tipo es "AU" recupera el número de autores por PMID. El retorno es un dataframe con el PMID y el num_auth.
                *Si el tipo es "AD" recupera el conteo de autores por país. El retorno es un dataframe con el country y el num_auth.
                """
    
    #importar paquetes
    import Bio
    from Bio import Entrez as en
    from Bio import Medline as md
    import pandas as pd
    import numpy as np
 
    #notificar correo
    en.email = "manuela.moscoso@est.ikiam.edu.ec.com"
    
    #definir termino de busqueda
    busqueda=keyword+"[Title/Abstract]"

    #realizar la busqueda
    handle= en.esearch(db="pubmed", term=busqueda)
    record = en.read(handle)
    idlist = record["IdList"]
    handle = en.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")

    #almacenar los resultados para su manipulacion
    records=md.parse(handle)
    
    #crear las listas con los resultados
    pmid_dict=[]
    au_dict=[]
    ad_dict=[]
    dp_dict=[]
    
    for record in records:   
        #registrar los PMIDs    
        pmid_dict.extend(record.get("PMID", "?"))

        if tipo=='AU':
        #mostrar los autores
            au_dict.extend(record.get("AU", "?"))
            #generar la sumatoria de autores
            contador=[len (i) for i in au_dict]
            #crear los data frames a partir de las listas obtenidas
            df_autores=pd.DataFrame(list(zip(pmid_dict,contador)),columns=['PMID','num_auth'])
    
        elif tipo=='AD':
            #mostrar los paises
            ad_dict.extend(record.get("AD", "?"))
            #crear los data frames a partir de las listas obtenidas
            df_paises=pd.DataFrame(list(zip(ad_dict,contador)),columns=['country','num_auth'])
                
        elif tipo=='DP':
            #mostrar la fecha
            dp_dict.extend(record.get("DP", "?"))
            #crear los data frames a partir de las listas obtenidas
            df_fecha=pd.DataFrame(list(zip(pmid_dict,dp_dict)),columns=['PMID','DP_year'])
                    
        else:
            print("Tipo invalido")


            
      