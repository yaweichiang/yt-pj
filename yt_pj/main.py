import urllib.request as urlrq
import ssl
import json
import certifi



CHANALL_ID = 'UCgc00bfF_PvO_2AvqJZHXFg'
API_KEY= 'AIzaSyBe3oxJ0moiKlBC965J3S42eotO_dZlz60'

def get_all_video_in_channel(channel_id,api_key):
   base_video_url = 'https://www.youtube.com/watch?v='
   base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

   first_url =f'{base_search_url}key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

   video_links = []
   url = first_url

   while True:

      inp = urlrq.urlopen(url, context=ssl.create_default_context(cafile=certifi.where()))
      resp = json.load(inp)

      for i in resp['items']:
         if i['id']['kind'] == "youtube#video":
            video_links.append(base_video_url + i['id']['videoId'])

      try:
         next_page_token = resp['nextPageToken']
         url = first_url + '&pageToken={}'.format(next_page_token)
      except:
         break
   return video_links
#https://youtube.googleapis.com/youtube/v3/captions?videoId=mVx9G3_5Exc&key=AIzaSyBe3oxJ0moiKlBC965J3S42eotO_dZlz60
def get_channel_captionid(video_id,api_key):
   base_search_url = 'https://youtube.googleapis.com/youtube/v3/captions?'

   first_url =f'{base_search_url}videoId={video_id}&key={api_key}'
   caption_list = []
   url = first_url

   inp = urlrq.urlopen(url, context=ssl.create_default_context(cafile=certifi.where()))
   resp = json.load(inp)

   for i in resp['items']:
         caption_list.append(i['id'])

   return caption_list

# video_list = get_all_video_in_channel(CHANALL_ID,API_KEY)
# print(video_list)
get_channel_captionid('mVx9G3_5Exc',API_KEY)






