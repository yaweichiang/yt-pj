import math
import os
from yt_pj.pipeline.steps.get_video_list import GetVideoList
from yt_pj.pipeline.steps.create_yt import CreateYT
from yt_pj.pipeline.steps.download_caption import DownloadCaption
from yt_pj.pipeline.steps.read_caption import ReadCaption
from yt_pj.pipeline.steps.search import Search
from yt_pj.pipeline.pipeline import Pipeline
from yt_pj.utils import Utils
from yt_pj.pipeline.steps.preflight import Preflight
from yt_pj.pipeline.steps.postflight import Postflight
from yt_pj.setting import CAPTIONS_DIR
from yt_pj.pipeline.steps.teststep import TestStep

CHANNEL_ID = 'UCgc00bfF_PvO_2AvqJZHXFg'
SEARCH_WORD = 'can'

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': SEARCH_WORD,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        CreateYT(),
        # DownloadCaption(),
        TestStep(),
        ReadCaption(),
        Search(),
        # Postflight(),
    ]

    utils = Utils()

    p = Pipeline(steps)
    p.run(inputs, utils)

    # R = ReadCaption()
    # data = R.process(os.listdir(CAPTIONS_DIR), inputs, utils)
    # S = Search()
    # S.process(data, inputs, utils)




if __name__ == '__main__':
    main()
