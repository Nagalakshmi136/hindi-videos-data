# Python code to convert video to audio
import moviepy.editor as mp
from pathlib import Path

def resolve_path(str_path):

    file_path = Path(str_path)  
    if file_path.exists():
        return file_path
    else:
        print("file not found with given path")


def video_to_audio(video_file):
    video_file_path = resolve_path(video_file)
    # Insert Local Video File Path
    clip = mp.VideoFileClip(video_file_path)

    # Insert Local Audio File Path
    clip.audio.write_audiofile(open("audio_file",mode='w',))
    
def time_duration(time_segment):
    ms = int(time_segment.split(',')[-1])
    hr,mins,s = map(int,time_segment.split(',')[0].split(':'))
    ms += hr*60*60*1000 + mins*60*1000 + s*1000
    return ms

def subtitle_formatting(subtitle_file):
    subtitle_path = resolve_path(subtitle_file)
    with open(subtitle_path) as sf:
        subtitle_data = sf.read().split('\n\n')
        for segment in subtitle_data:
            subtitle_text = segment.split('\n')[-1]
            time_segment = segment.split('\n')[1].split('-->')
            start_duration = time_duration(time_segment[0])
            end_duration = time_duration(time_segment[1])
            print(f"{start_duration} {end_duration} {subtitle_text}")
            
        
    

subtitle_formatting('/home/munikumar/Downloads/hindi_youtube_subtitles')
    

