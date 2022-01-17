import logging
from .steps.step import StepException
from time import time


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                start = time()
                data = step.process(data, inputs, utils)
                end = time()
                logging.getLogger('log').info(f'{step.__module__.split("yt_pj.pipeline.steps.")[-1]}'
                                              f'執行時間： {end - start}')
            except StepException as e:
                logging.getLogger('log').error('Exception happened :', e)
                break
