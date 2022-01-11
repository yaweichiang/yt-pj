from yt_pj.pipeline.steps.step import Step
from yt_pj.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        print('搜尋字幕')
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


# class Search(Step):
#     def process(self, data, inputs, utils):
#         print('搜尋詞語')
#         datas = {}
#         for dic_caption in data:
#             picktime = []
#             for item in data[dic_caption]:
#                  if inputs['search_word'] in item:
#                      time = data[dic_caption][item].split('-->')
#                      picktime.append((time[0], time[1], item))
#
#             if picktime != []:
#                 datas[dic_caption] = picktime
#         print(datas)
#         return datas
