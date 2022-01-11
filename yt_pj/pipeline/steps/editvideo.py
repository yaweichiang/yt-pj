from yt_pj.pipeline.steps.step import Step


class EditVideo(Step):
    def process(self, data, inputs, utils):
        print('剪輯影片')
        for yt in data:
