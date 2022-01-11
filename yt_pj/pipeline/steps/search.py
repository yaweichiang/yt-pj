from yt_pj.pipeline.steps.step import Step


class Search(Step):
    def process(self, data, inputs, utils):
        datas = {}
        for dic_caption in data:
            picktime = []
            for item in data[dic_caption]:
                 if inputs['search_word'] in item:
                     time = data[dic_caption][item].split('-->')
                     picktime.append((time[0], time[1], item))

            if picktime != []:
                datas[dic_caption] = picktime
        print(datas)
        return datas



