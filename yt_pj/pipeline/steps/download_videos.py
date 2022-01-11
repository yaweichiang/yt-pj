from pytube import YouTube
from yt_pj.pipeline.steps.step import Step
from yt_pj.setting import VIDEOS_DIR



class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        print('下載影片')
        set_data = set([found.yt for found in data])  # 將found 物件中相同yt 保留一個
        count = 0
        for yt in set_data:
            url = yt.url
            if utils.video_exist(yt):
               continue
            YouTube(url).streams.get_lowest_resolution().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
            count += 1
            if count == 10:
                count = 0
                break



