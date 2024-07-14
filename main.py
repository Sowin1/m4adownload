import os
from yt_dlp import YoutubeDL

def download_youtube_video_as_m4a(youtube_url, output_folder="result"):
    # Vérifier si le dossier de sortie existe, sinon le créer
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Options de téléchargement
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    print(f"Téléchargement terminé! Le fichier m4a est sauvegardé dans {output_folder}")

# Exemple d'utilisation avec une URL YouTube valide
download_youtube_video_as_m4a("<lien>")
