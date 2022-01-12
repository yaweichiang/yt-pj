import os
from yt_pj.setting import CAPTIONS_DIR
from yt_pj.setting import DOWNLOADS_DIR
from yt_pj.setting import VIDEOS_DIR
from yt_pj.setting import OUTPUTS_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def create_dir():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(OUTPUTS_DIR, exist_ok=True)

    @staticmethod
    def check_caption_exist(captions):  # search caption_code 無使用
        caption_code = captions.lang_code_index.keys().__iter__().__next__()
        return caption_code

    @staticmethod
    def captions_exist(yt):
        path = yt.caption_path
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def video_exist(yt):
        path = yt.video_path
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def get_outputs_path(inputs):
        filename = f'{inputs["channel_id"]}_{inputs["search_word"]}.mp4'
        return os.path.join(OUTPUTS_DIR, filename)
