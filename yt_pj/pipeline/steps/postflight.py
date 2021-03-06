from yt_pj.pipeline.steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        cutvideo = set([found.yt for found in data])
        print(f'共剪輯 {len(cutvideo)}部影片！清單如下：')
        for video in cutvideo:
            print(video)
        if inputs['cleanup'] is True:
            utils.delete_dir()
        return
