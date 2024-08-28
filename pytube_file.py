#pip install pytube
from pytube import YouTube

# URL del video que deseas descargar
url = 'https://www.youtube.com/...'
#Crear objeto YT
yt = YouTube(url)
# Get the highest resolution stream
yd = yt.streams.get_highest_resolution()

# Descargar video en el directorio actual
yd.download()

print(f"Video '{yt.title}' descargado exitosamente!")

# Ejecutar en consola: python .\Descargar.py
