from yt_pj.pipeline.steps.step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        utils.create_dir()
