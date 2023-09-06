from googleapiclient.discovery import build
import numpy as np
import json

class you_tube:
    
    def __init__(self, api_key) -> None:
        self.youtube = build('youtube','v3', developerKey=api_key)
        
    def get_all_hindi_videos(self):
        videos = []
        next_page_id = None
        while 1:
            request = self.youtube.search().list(q = "hindi",
                                             part = "snippet",
                                             pageToken = next_page_id,
                                             maxResults = 50)
            response = request.execute()
            next_page_id = response.get('nextPageToken')
            videos_data = response['items']
            videos_id = [video_data['id']['videoId'] for video_data in videos_data
                         if video_data.get('id').get('videoId') != None]
            # print(videos_id,next_page_id)
            videos.append(videos_id)
            if next_page_id is None:
                break
        with open('all_videos.json1','w') as f:
                        json.dump(videos,f,indent=4)
        return videos
    
    def get_hindi_audio_videos(self,videos):
        len_videos = len(videos)
        hindi_videos = []
        for i in range(len_videos):
             videos_id = ','.join(videos[i])
             request = self.youtube.videos().list(id = videos_id,
                                                  part = "snippet",
                                                  maxResults = 50,
                                                  )
             response = request.execute()['items']
             hindi_videos_id = [videos[i][j] for j in range(len(response))
                                if response[j].get('snippet').get('defaultAudioLanguage') == 'hi']
            #  print(hindi_videos_id)
             hindi_videos.append(hindi_videos_id)
        with open('hindi_videos1.json','w') as f:
                        json.dump(hindi_videos,f,indent=4)
        return hindi_videos
             
    def get_hindi_subtitle_videos(self,videos):
        hindi_subtitle_videos = []
        for i in range(len(videos)):
            for j in range(len(videos[i])):
                request = self.youtube.captions().list(
                    videoId = videos[i][j],
                    part = "snippet"
                ) 
                response = request.execute()['items']
                print(response)
                if len(response)!=0 and response[0].get('snippet').get('language') == 'hi':
                    with open('videos_id.txt','a') as f:
                        f.write(videos[i][j])
                        f.write('\n')
                    hindi_subtitle_videos.append(videos[i][j])
        print(hindi_subtitle_videos)
        return hindi_subtitle_videos 
    
    def load_data_json(self):
        with open('hindi_videos.json','rb') as f:
            videos = json.load(f)
            return videos
    
    def get_hindi_videos(self):
        # all_hindi_videos = self.get_all_hindi_videos()
        # hindi_audio_videos = self.get_hindi_audio_videos(all_hindi_videos)
        hindi_audio_videos = self.load_data_json()
        # print(len(hindi_audio_videos))
        # ls = hindi_audio_videos[6:11][:]
        # print(ls[4].index('P7OJBJBgdK4'))
        hindi_subtitle_videos = self.get_hindi_subtitle_videos(hindi_audio_videos[10:][:])
        # return hindi_subtitle_videos 
    
API_KEY = "AIzaSyAR_lBZ5aRLNQcXZ9NpbfWYt38d2GZEUhY"
# BASE_URL = "https://www.googleapis.com/youtube/v3"
youtube_obj = you_tube(API_KEY)
youtube_obj.get_hindi_videos()