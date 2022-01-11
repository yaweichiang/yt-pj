from pytube import YouTube
from .step import Step


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        print('下載字幕')
        for yt in data:
            if utils.captions_exist(yt):
                continue
            sourse = YouTube(yt.url)
            try:  # 只抓取a.en字幕,跳過無字幕及非a.en字幕的影片
                en_caption = sourse.captions['a.en']
                captions = en_caption.generate_srt_captions()
            except KeyError:
                continue
            except AttributeError:
                continue
            with open(yt.caption_path, 'w', encoding='utf-8') as file:
                for line in captions:
                    file.write(line)
        return data
