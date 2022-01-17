
import os
from yt_pj.setting import CAPTIONS_DIR
from yt_pj.setting import VIDEOS_DIR
from pytube import YouTube



class YT:
    def __init__(self, url, channel_id):
        self.url = url
        self.channel_id = channel_id
        self.id = self.get_video_id()
        self.caption_path = self.get_caption_path()
        self.video_path = self.get_video_path()
        self.captions = None
        # self.caption_language = self.get_video_language()

    def get_video_id(self):
        return self.url.split('watch?v=')[-1]

    def get_caption_path(self):
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

    def get_video_path(self):
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')

    def __str__(self):  # 簡易# 說明
        return f'YT_{self.id}'

    def __repr__(self):  # 詳細說明
        info = ' ; '.join([
            'id=' + str(self.id),
            'url=' + str(self.url),
            ])

        return f'<YT({info})>'

    # def get_video_language(self):
    #     try:
    #         video_lang = YouTube(self.url).captions.lang_code_index.keys().__iter__().__next__()
    #     except AttributeError:
    #         video_lang = None
    #     return video_lang