from yt_pj.pipeline.steps.step import Step

from time import time


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        print('讀取字幕')
        start_time = time()
        for yt in data:
            if not utils.captions_exist(yt):
                continue
            with open(yt.caption_path, 'r', encoding='utf-8') as caption:
                captions = {}
                temp_time = ''
                line_counting = 1
                for line in caption:
                    line_type = line_counting % 4
                    if line_type == 2:
                        temp_time = line.strip()
                    if line_type == 3:
                        captions[line.strip()] = temp_time
                    line_counting += 1
                yt.captions = captions
        end_time = time()
        print(end_time-start_time)
        return data
