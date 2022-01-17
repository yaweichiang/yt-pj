import os
from time import time
import urllib.request as urlrq
import ssl
import json
import certifi
import logging
from yt_pj.setting import DOWNLOADS_DIR
from yt_pj.pipeline.steps.step import Step
from yt_pj.setting import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']

        if inputs['fast'] is True:
            if self.video_lists_exist(channel_id):
                logging.getLogger('log').info('自檔案讀取video_list')
                return self.read_video_lists(channel_id)

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = f'{base_search_url}key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

        video_links = []
        url = first_url
        logging.getLogger('log').info('開始使用api')
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
        logging.getLogger('log').info('使用api取得videolist')
        self.write_video_lists(video_links, channel_id)
        return video_links

    @staticmethod
    def get_video_lists_path(channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_lists_exist(self, channel_id):  # 檢查videolist是否存在
        path = self.get_video_lists_path(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def write_video_lists(self, video_list, channel_id):
        with open(self.get_video_lists_path(channel_id), 'w', encoding='utf-8') as f:
            for url in video_list:
                f.write(url + '\n')

    def read_video_lists(self, channel_id):
        with open(self.get_video_lists_path(channel_id), 'r', encoding='utf-8') as f:
            video_link = []
            for url in f:
                video_link.append(url.strip())
        return video_link

