
import requests
import json

class youtube:
    def __init__(self, api_key, base_url) -> None:
        self.api_key = api_key
        self.base_url = base_url
    
    def get_all_hindi_videos(self):
        url = f'{self.base_url}/search?part=snippet&q=hindi&maxResults=50&key={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            hindi_videos_data = response.json()['items']
            hindi_videos_id = [video_data['id']['videoId'] for video_data in hindi_videos_data]
            print(hindi_videos_id)
            return hindi_videos_id
        else:
            print("No videos found")
    
    def get_hindi_audio_videos(self, hindi_videos):
        id = '%2C'.join(hindi_videos)
        url = f'{self.base_url}/videos?part=snippet&id={id}&key={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            hindi_videos_data = response.json()['items']
            hindi_audio_videos_id =[]
            # print(json.dumps(hindi_videos_data,indent=4),len(hindi_videos_data))
            for i in range(len(hindi_videos_data)):
                snippet_data = hindi_videos_data[i]['snippet']
                lang = 'defaultAudioLanguage'
                if  lang in snippet_data.keys() and snippet_data[lang] == 'hi':
                    hindi_audio_videos_id.append(hindi_videos[i])                                     
            print(hindi_audio_videos_id)
            return hindi_audio_videos_id
        
    def get_hindi_subtitle_videos(self,hindi_audio_videos):
        videos_subtitle_id =[]
        for i in range(len(hindi_audio_videos)):
            url = f'{self.base_url}/captions?part=snippet&videoId={hindi_audio_videos[i]}&key={self.api_key}'
            response = requests.get(url)
            if response.status_code == 200:
                video_subtitle_data = response.json()['items'][0]
                print(json.dumps(video_subtitle_data,indent=4))
                if 'language' in video_subtitle_data.keys() and video_subtitle_data['language'] == 'hi':
                    videos_subtitle_id.append(hindi_audio_videos[i])
                print(videos_subtitle_id)
                return videos_subtitle_id
            
        
    def get_hindi_videos(self):
        all_hindi_videos = self.get_all_hindi_videos()
        hindi_audio_videos = self.get_hindi_audio_videos(all_hindi_videos)
        
        hindi_subtitle_videos = self.get_hindi_subtitle_videos(hindi_audio_videos)
        return hindi_subtitle_videos 
        
API_KEY = "AIzaSyDoA6PM3SXIPoPjLHU2BJjwYU63X6lGro0"
BASE_URL = "https://www.googleapis.com/youtube/v3"
youtube_obj = youtube(API_KEY, BASE_URL)
youtube_obj.get_hindi_videos()
