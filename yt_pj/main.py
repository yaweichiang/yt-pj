import urllib.request as urlrq
import ssl
import json
import certifi
from .setting import API_KEY #或是寫成絕對路徑 from yt-pj.settinng import API_KEY
# import pytube

CHANALL_ID = 'UCQq36RYp2AKIftKhQGXElXA'


def get_all_video_in_channel(channel_id, api_key):
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = f'{base_search_url}key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

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
        except KeyError:
            break

    return video_links

#
#
# yt = pytube.YouTube('https://www.youtube.com/watch?v=8jo0ojNgpR8')
# yt_caption = yt.captions['a.en']
# print(yt_caption.xml_captions)
# S = yt_caption.xml_captions.splitlines()
#
# newlines = []
# memoryword = ''
# memorytime = ''
#
# for line in S:
#     for word in line:
#         if word == '<':
#             do_type = 'get_time'
#             memoryword += ' '
#         elif word == '>':
#             do_type = 'get_word'
#
#         else:
#             if do_type == 'get_time':
#                 if word == ' ':
#                     for firstword in memorytime:
#                         if firstword == 't':
#                             memoryword += memorytime
#                         else:
#                             memorytime = ''
#                 else:
#                     memorytime += word
#                 # continue
#             elif do_type == 'get_word':
#                 memoryword += word
#
# newlines = memoryword.split()
# for line in newlines:
#     print(line)
url_list = get_all_video_in_channel(CHANALL_ID,API_KEY)
print(len(url_list))
print(url_list)