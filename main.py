#Terminal: pip install pytube, pip install moviepy
from pathlib import Path
import download_youtube
import extract_audio

file= r'todownload.csv'
directory_to_save = r'C:\Users\hemil\Desktop\DownloadAndConvert\arquivos'
path_list = Path(directory_to_save).glob('*.mp4')

mp4 = download_youtube.download(file)
mp3 = extract_audio.extract(path_list)









