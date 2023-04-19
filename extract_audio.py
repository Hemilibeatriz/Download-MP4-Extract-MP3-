from moviepy.editor import *

def extract(path_list):
    for file in path_list:
        video = VideoFileClip(str(file))
        video.audio.write_audiofile(f"{str(file)}.mp3")