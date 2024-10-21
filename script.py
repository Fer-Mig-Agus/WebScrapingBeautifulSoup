import requests
from bs4 import BeautifulSoup
import pandas as pd 

url='https://dockerlabs.es'
data=[]

try:
    response=requests.get(url)
    response.raise_for_status()
    
    soup=BeautifulSoup(response.text,'html.parser')
    machines=soup.find_all('div',onclick=True)

    if machines:
        for machine in machines:
            onclick_text=machine['onclick']
            try:
                name=onclick_text.split("'")[1]
                difficulty=onclick_text.split("'")[3]
                author=onclick_text.split("'")[7]
                
                download_button=machine.find('button',class_='download')
                if download_button:
                    download_onclick=download_button['onclick']
                    download_link=download_onclick.split("'")[1]
                    
                    data.append({
                        'Name':name,
                        'Difficulty':difficulty,
                        'Author':author,
                        'Download Link':download_link
                    })
                else:
                    print(f'El {name} no tiene link de descarga')                
            except IndexError:
                print('Error al extraer los datos de onclick')
            
    else:
        print('No se han encontrado maquinas')
    
    
         
except requests.RequestException as error:
    print(f'Hubo un error al hacer la peticion {error}')

if len(data) != 0:
    df=pd.DataFrame(data)
    df.to_excel('machines_data.xlsx',index=False, engine='openpyxl')
    print('Datos exportados a machines_data.xlsx')
else:
    print('No se cargo nada')