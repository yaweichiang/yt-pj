from pytube import YouTube
from .step import Step
from concurrent.futures import ThreadPoolExecutor


class DownloadCaption(Step):  # multi-threading1
    def process(self, data, inputs, utils):
        with ThreadPoolExecutor(max_workers=35) as ex:
            # {ex.submit(self.download_and_save, yt): yt for yt in data if not (utils.captions_exist(yt))}
            for yt in data:
                if inputs['fast'] is True:
                    if utils.captions_exist(yt):
                        continue
                ex.submit(self.download_and_save, yt)
        return data

    @staticmethod
    def download_and_save(yt):
        try:
            s = YouTube(yt.url)
            en_captions = s.captions['a.en']
        except KeyError:
            return
        except AttributeError:
            return
        captions = en_captions.generate_srt_captions()
        with open(yt.caption_path, 'w', encoding='utf-8') as file:
            for line in captions:
                file.write(line)
        return
