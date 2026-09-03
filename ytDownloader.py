import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

def downloader():
    print("--- YouTube Downloader para Chromebook ---")
    print("1. Descargar VIDEO (Máxima resolución)")
    print("2. Descargar AUDIO (Calidad máxima .mp3)")
    
    opcion = input("\nSelecciona una opción (1 o 2): ")
    
    if opcion not in ['1', '2']:
        print("Opción no válida. Abortando.")
        return

    url = input("Pega la URL de YouTube: ")

    try:
        yt = YouTube(url, on_progress_callback=on_progress, use_po_token=True)
        print(f"\nProcesando: {yt.title}")

        if opcion == '1':
            print("Buscando video...")
            stream = yt.streams.get_highest_resolution()
            print(f"Descargando video en {stream.resolution}...")
            stream.download()
            print("\n¡Video descargado con éxito!")

        else:
            print("Buscando audio...")
            # Filtramos solo audio y descargamos el de mayor bitrate
            stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            print(f"Descargando audio ({stream.abr})...")
            
            archivo_descargado = stream.download()
            
            # Cambiamos la extensión a .mp3 para que ChromeOS lo reconozca fácil
            base, ext = os.path.splitext(archivo_descargado)
            nuevo_archivo = base + '.mp3'
            os.rename(archivo_descargado, nuevo_archivo)
            
            print(f"\n¡Audio descargado y convertido a .mp3!")

    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
        print("Tip: Si el error persiste, intenta: pip install --upgrade pytubefix --break-system-packages")

if __name__ == "__main__":
    downloader()

# # Ejecutar en consola: python3 ./ytDownloader.py
# # Para mantener pytubefix al día, se debe ejecutar este comando: 
# # pip install --upgrade pytubefix --break-system-packages
# # Si alguna vez el script se vuelve "loco" y no funciona ni actualizando, a veces es mejor forzar una reinstalación limpia:
# # pip uninstall pytubefix --break-system-packages -y && pip install pytubefix --break-system-packages

# Solución sin el script,porque ya está roto, descargar yt-dlp:
# pip install --upgrade yt-dlp --break-system-packages
# Usarlo para mp3 y video máxima resolución ejecutar respectivamente:
# yt-dlp -x --audio-format mp3 "TU_URL_AQUÍ"
# yt-dlp "TU_URL_AQUÍ"


# Para descargar de mitocode de vimeo:
# sudo apt update
# sudo apt install python3-venv python3-full
# python3 -m venv venv
# source venv/bin/activate
# Verás que tu prompt ahora empieza con (venv). Ahora sí puedes instalar lo que quieras.
# pip install yt-dlp
# sudo apt update && sudo apt install ffmpeg
# Ejecutar comando: 
# yt-dlp --referer "https://apps.mitocode.com/" "https://player.vimeo.com/video/1185028918"
# O ejecutar el script en su lugar pero saliendo del ambiente (env) con deactivate