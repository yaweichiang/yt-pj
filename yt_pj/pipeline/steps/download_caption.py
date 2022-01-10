from pytube import YouTube
from .step import Step


def _loadcaptions(sourse, caption_code):
    en_caption = sourse.captions[caption_code]
    en_str = en_caption.generate_srt_captions()
    return en_str


def _savecaptions(captions, url):
    with open(url, 'w', encoding='utf-8') as f:
        for line in captions:
            f.write(line)


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        for url in data:
            if utils.captions_exsit(url):
                print(f'字幕檔已存在({utils.get_video_id(url)})')
                continue
            sourse = YouTube(url)
            caption_code = utils.check_caption_exist(sourse.captions)
            if caption_code == 'False':
                print(f'無字幕可下載({utils.get_video_id(url)})')
                continue
            else:
                save_url = utils.get_caption_path(url)
                captions = _loadcaptions(sourse, caption_code)
                _savecaptions(captions, save_url)
        return
