import urllib.request as urlrq
import ssl
import json
import certifi

from yt_pj.pipeline.steps.step import Step
from yt_pj.setting import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']
        if utils.video_list_exist(channel_id):
            print('自檔案讀取video_list')
            return utils.read_video_list(channel_id)

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = f'{base_search_url}key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

        video_links = []
        url = first_url
        print('開始使用api')
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
        print('使用api取得videolist')
        utils.write_video_list(video_links, channel_id)
        return video_links
