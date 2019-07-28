#!/usr/bin/env python
# coding: utf-8

# In[147]:


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

req = requests.get('http://sitl.diputados.gob.mx/LXIV_leg/listado_diputados_gpnp.php')


# In[148]:


html_doc = req.text

html = bs(html_doc, 'html.parser')


# In[143]:


nombres = []
enlaces = []
estados = []
representacion_tipo = []
representacion = []


for text in html.find_all("td","textoNegro"):
    if ('bgcolor' in text.attrs):
        continue
    elif text.a:
        enlaces.append(text.a['href'])
        nombre_lista = text.text.split(' ')
        nombre_lista.pop(0)
        nombre = ' '.join(nombre_lista)
        nombres.append(nombre)
    elif text['width'] == '300':
        estados.append(text.text)
    else:
        lista_representacion = text.text.split('  ')
        if lista_representacion[0] == 'Circ.':
            representacion_tipo.append('Circunscripcion')
        elif lista_representacion[0] == 'Dtto.':
            representacion_tipo.append('Distrito')
        representacion.append(lista_representacion[1])            
            
            
       


# In[145]:


df = percentile_list = pd.DataFrame(
    {'nombre': nombres,
     'enlace': enlaces,
     'estado': estados,
     'tipo_de_representacion': representacion_tipo,
     'representacion': representacion
    })


# In[146]:


df


# In[ ]:




