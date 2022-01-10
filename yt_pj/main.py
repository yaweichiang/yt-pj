from yt_pj.pipeline.steps.get_video_list import GetVideoList
from yt_pj.pipeline.steps.download_caption import DownloadCaption
from yt_pj.pipeline.pipeline import Pipeline
from yt_pj.utils import Utils
from yt_pj.pipeline.steps.preflight import Preflight
from yt_pj.pipeline.steps.postflight import Postflight
CHANNEL_ID = 'UC-ZMWGgdNaiRcKXyRHdl_bg'


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

#
# sourse = YouTube('https://www.youtube.com/watch?v=IRyJe-0Uie0')
# print(sourse.video_id)
# code = (sourse.captions.lang_code_index).keys().__iter__().__next__()
# en_caption = sourse.captions[code]
# en_str = en_caption.generate_srt_captions()
# print(en_str)