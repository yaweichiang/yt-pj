from yt_pj.pipeline.steps.step import Step


class Search(Step):
    def process(self, data, inputs, utils):
        print('搜尋字幕')
        for yt in data:
            for line in yt.captions:
                if inputs['search_word'] in line:
                    print(line, yt.captions[line])

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
