import requests
import pandas as pd
import json

#https://apidatalake.tesouro.gov.br/docs/sadipem/#/PVL%20-%20Dados%20B%C3%A1sicos

r'''  
"items": [
    {
      "id_pleito": 25056,
      "tipo_interessado": "Estado",
      "interessado": "Paraná",
      "cod_ibge": 41,
      "uf": "PR",
      "num_pvl": "PVL02.000961/2017-51",
      "status": "Deferido",
      "num_processo": "17944.000628/2017-12",
      "data_protocolo": "2017-09-22T19:38:07Z",
      "tipo_operacao": "Operação contratual interna",
      "finalidade": "Renegociação de dívidas",
      "tipo_credor": "Empresa Estatal",
      "credor": "Companhia Paranaense de Energia",
      "moeda": "Real",
      "valor": 1460119244.75,
      "pvl_assoc_divida": 1,
      "pvl_contradado_credor": 0,
      "data_status": "28/09/2017"
    },


'''
requests = requests.get('https://apidatalake.tesouro.gov.br/ords/sadipem/tt/pvl?uf=PR&tipo_interessado=Município')

j = json.loads(requests.text)


df = pd.DataFrame(j['items'])
print(df.head(10))
#print(j)
#
#df = pd.DataFrame.from_dict(j)
#df.head()