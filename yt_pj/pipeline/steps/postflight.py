from yt_pj.pipeline.steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('postflight')
        pass
