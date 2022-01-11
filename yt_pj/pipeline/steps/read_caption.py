import os.path
from yt_pj.setting import CAPTIONS_DIR
from yt_pj.pipeline.steps.step import Step



class ReadCaption(Step):
    def process(self, data, inputs, utils):
        datas= {}
        for captionfile in data:
            captions = {}
            temp_time = ''
            line_counting = 1
            with open(os.path.join(CAPTIONS_DIR, captionfile), 'r', encoding='utf-8') as caption:
                try:
                    for line in caption:
                        line_type = line_counting % 4
                        if line_type == 2:
                            temp_time = line.strip()
                        elif line_type == 3:
                            captions[line.strip()] = temp_time
                        line_counting += 1
                except UnicodeDecodeError:
                    pass
            datas[captionfile.split('.txt')[0]] = captions

        print(datas)

