
# Web Scraping de DockerLabs

Este proyecto realiza un web scraping en el sitio web [DockerLabs](https://dockerlabs.es) para extraer información sobre máquinas disponibles. La información recopilada incluye el nombre, la dificultad, el autor y el enlace de descarga de cada máquina. Los datos se guardan en un archivo Excel para su posterior análisis y uso.

## Requisitos

Para ejecutar este proyecto, necesitarás tener Python instalado en tu sistema, junto con las siguientes bibliotecas:

- `requests`: Para realizar las solicitudes HTTP.
- `beautifulsoup4`: Para analizar el contenido HTML de la página.
- `pandas`: Para manejar los datos y exportarlos a Excel.
- `openpyxl`: Para guardar los datos en formato Excel.

Puedes instalar las bibliotecas necesarias utilizando `pip`:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## Cómo usar

1. **Clona el repositorio** o descarga el archivo del script Python.
2. Abre una terminal y navega hasta el directorio donde se encuentra el script.
3. Ejecuta el script con el siguiente comando:

```bash
python nombre_del_script.py
```

4. El script hará una solicitud al sitio web de DockerLabs, extraerá la información de las máquinas y la guardará en un archivo llamado `machines_data.xlsx` en el mismo directorio.

## Estructura del Código

El script realiza las siguientes acciones:

- Realiza una solicitud GET a la URL especificada.
- Verifica si la solicitud fue exitosa (código de estado 200).
- Utiliza BeautifulSoup para analizar el HTML y encontrar los elementos relevantes.
- Extrae el nombre, dificultad, autor y enlace de descarga de cada máquina.
- Almacena los datos en una lista de diccionarios.
- Crea un DataFrame de pandas a partir de la lista de diccionarios.
- Exporta el DataFrame a un archivo Excel utilizando `openpyxl`.

## Ejemplo de Uso

Al ejecutar el script, se generará un archivo `machines_data.xlsx` que contendrá los siguientes datos:

| Name          | Difficulty | Author           | Download Link                                  |
|---------------|------------|------------------|------------------------------------------------|
| AguaDeMayo    | Fácil      | The Hackers Labs | https://mega.nz/file/kC1nTCoI#MD6FBVLITgA5dtLglSBYbOUtJ_Tb-CmslqZM1kUx6C8 |

## Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna sugerencia o mejora, no dudes en hacer un fork del repositorio y enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.
