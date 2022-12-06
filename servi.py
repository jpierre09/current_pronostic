import requests
import json
import pandas as pd

#url = "https://siata.gov.co/servicios_portales/api/portal/hidrometeo/nivel/nivelkml/"
def filteredList():
  #url = "http://siata.gov.co:8089/pronosticoMunicipios/63882184869634ff91bcf727d3fa210ec6c210bf/"
  url = "http://siata.gov.co:8089/pronosticoMunicipiosSimplificado/63882184869634ff91bcf727d3fa210ec6c210bf/?format=json"
  
  data = requests.get(url) #Se realiza la petición http

  if data.status_code == 200: # Esperando respuesta 200 del servidor para ejecutar el if
    data_json = data.json()   # 
    #print(type(data_json))
  
    
    #print(json.dumps(data_json['datos'][0:2], indent=4))   ### impresion original
    for entity in data_json["datos"]:
      entityname = entity['codigoMunicipio'], entity['nombreMunicipio']
      print(entityname)
      #for coordenates in entity["coordenadas"]:
      #  geoposition = coordenates['latitud'], coordenates['longitud']
        #print(geoposition)

filteredList()



  
  
  
 
