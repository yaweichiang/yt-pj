from yt_pj.pipeline.steps.step import Step
from yt_pj.model.yt import YT


class CreateYT(Step):
    def process(self, data, inputs, utils):
        print('建立ＹＴ')
        return [YT(url, inputs['channel_id']) for url in data]



