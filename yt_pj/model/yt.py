
import os
from yt_pj.setting import CAPTIONS_DIR
from yt_pj.setting import VIDEOS_DIR


class YT:
    def __init__(self, url, channel_id):
        self.url = url
        self.channel_id = channel_id
        self.id = self.get_video_id()
        self.caption_path = self.get_caption_path()
        self.video_path = self.get_video_path()
        self.captions = None

    def get_video_id(self):
        return self.url.split('watch?v=')[-1]

    def get_caption_path(self):
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

    def get_video_path(self):
        return os.path.join(VIDEOS_DIR, self.id)