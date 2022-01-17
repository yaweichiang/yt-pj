from yt_pj.pipeline.steps.step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
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
        return data
