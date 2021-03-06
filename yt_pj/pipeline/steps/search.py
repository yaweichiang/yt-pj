from yt_pj.pipeline.steps.step import Step
from yt_pj.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        found = []
        for yt in data:
            if not utils.captions_exist(yt):
                continue
            captions = yt.captions
            for caption in captions:
                if inputs['search_word'] in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)
        return found
