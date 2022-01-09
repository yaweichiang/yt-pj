import os
from pytube import YouTube
from .step import Step


def _loadcaptions(url):
    sourse = YouTube(url)
    code = sourse.captions.lang_code_index.keys().__iter__().__next__()
    en_caption = sourse.captions[code]
    en_str = en_caption.generate_srt_captions()
    return en_str


def _savecaptions(captions):
    with open('d_caption.txt', 'w', encoding='utf-8') as f:
        for line in captions:
            f.write(line)


class DownloadCaption(Step):
    def process(self, data, inputs):
        for url in data:
            captions = _loadcaptions(url)
            print(captions)
            # _savecaptions(captions)
            break  # 執行一次

