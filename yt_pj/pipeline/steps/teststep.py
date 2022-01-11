import os
from yt_pj.pipeline.steps.step import Step
from yt_pj.setting import CAPTIONS_DIR


class TestStep(Step):
    def process(self, data, inputs, utils):
        print('inTest')
        newdata = []
        for yt in data:
            if f'{yt.id}.txt' in os.listdir(CAPTIONS_DIR):
                newdata.append(yt)
        return newdata
