from pytube import YouTube
import csv

def download(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for link in reader:
            try:
                yt = YouTube(str(link))
                yt.streams.filter(file_extension='mp4')
                stream = yt.streams.get_by_itag(22)
                stream.download(output_path='arquivos')
            except:
                print(link)
                pass