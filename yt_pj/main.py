from pytube import YouTube
from yt_pj.pipeline.steps.get_video_list import GetVideoList
from yt_pj.pipeline.steps.download_caption import DownloadCaption
from yt_pj.pipeline.pipeline import Pipeline
from yt_pj.utils import Utils
from yt_pj.pipeline.steps.preflight import Preflight
from yt_pj.pipeline.steps.postflight import Postflight
CHANNEL_ID = 'UCgc00bfF_PvO_2AvqJZHXFg'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaption(),
        Postflight(),
    ]

    utils = Utils()

    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()

