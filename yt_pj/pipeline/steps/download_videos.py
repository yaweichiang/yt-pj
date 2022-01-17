from pytube import YouTube
from yt_pj.pipeline.steps.step import Step
from yt_pj.setting import VIDEOS_DIR
from concurrent.futures import ThreadPoolExecutor


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        set_data = set([found.yt for found in data])  # 將found 物件中相同yt 保留一個
        with ThreadPoolExecutor(max_workers=35) as ex:
            # {ex.submit(self.downloading, yt) for yt in data if not (utils.video_exist(yt))}
            for yt in set_data:
                if inputs['fast'] is True:
                    if utils.video_exist(yt):
                        continue
                ex.submit(self.downloading, yt)

        return data

    @staticmethod
    def downloading(yt):
        YouTube(yt.url).streams.get_lowest_resolution().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
