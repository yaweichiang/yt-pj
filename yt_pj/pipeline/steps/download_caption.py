from pytube import YouTube
from .step import Step
from yt_pj.utils import Utils

def _loadcaptions(sourse):
    code = sourse.captions.lang_code_index.keys().__iter__().__next__()
    en_caption = sourse.captions[code]
    en_str = en_caption.generate_srt_captions()
    return en_str


def _savecaptions(captions, url):

    with open(url, 'w', encoding='utf-8') as f:
        for line in captions:
            f.write(line)
    # 以上為舊寫法,下列寫法較新 但似乎還有問題
    # file = open(f'{soures.video_id}_caption.txt', 'w', encodings='utf-8')
    # file.write(captions)
    # file.close()


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        for url in data:
            sourse = YouTube(url)
            captions = _loadcaptions(sourse)
            save_url = utils.get_caption_path(url)
            print(captions)
            _savecaptions(captions, save_url)
            break  # 執行一次

