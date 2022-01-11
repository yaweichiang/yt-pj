import os
from yt_pj.setting import CAPTIONS_DIR
from yt_pj.setting import DOWNLOADS_DIR
from yt_pj.setting import VIDEOS_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def get_video_id(url):
        return url.split('watch?v=')[-1]

    def get_caption_path(self, url):
        return os.path.join(CAPTIONS_DIR, self.get_video_id(url) + '.txt')

    @staticmethod
    def create_dir():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    @staticmethod
    def check_caption_exist(captions):  # search caption_code 無使用
        caption_code = captions.lang_code_index.keys().__iter__().__next__()
        return caption_code

    @staticmethod
    def get_video_lists_path(channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def write_video_lists(self, video_list, channel_id):
        with open(self.get_video_lists_path(channel_id), 'w', encoding='utf-8') as f:
            for url in video_list:
                f.write(url + '\n')

    def video_lists_exist(self, channel_id):  # 檢查videolist是否存在
        path = self.get_video_lists_path(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def read_video_lists(self, channel_id):
        with open(self.get_video_lists_path(channel_id), 'r', encoding='utf-8') as f:
            video_link = []
            for url in f:
                video_link.append(url.strip())
        return video_link

    def captions_exist(self, url):
        path = self.get_caption_path(url)
        return os.path.exists(path) and os.path.getsize(path) > 0
