import time
from threading import Thread
from pytube import YouTube
from .step import Step


class DownloadCaption(Step):  # multi-threading1
    def process(self, data, inputs, utils):
        print('下載字幕')
        start_time = time.time()
        # new_list = []
        # yt_list = []
        # threads = []
        # for yt in data:
        #     if utils.captions_exist(yt):
        #         continue
        #     threads.append(Thread(target=self.download_and_save, args=([yt])))
        threads = [Thread(target=self.download_and_save, args=([yt])) for yt in data if not utils.captions_exist(yt)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        end_time = time.time()
        print('mulit-threading[1]耗時：', end_time - start_time)
        return data

    def download_and_save(self, yt):
        sourse = YouTube(yt.url)
        try:  # 只抓取a.en字幕,跳過無字幕及非a.en字幕的影片
            en_caption = sourse.captions['a.en']
            captions = en_caption.generate_srt_captions()
        except KeyError:
            return
        except AttributeError:
            return
        with open(yt.caption_path, 'w', encoding='utf-8') as file:
            for line in captions:
                file.write(line)
        return

# class DownloadCaption(Step):  # multi-threading
#     def process(self, data, inputs, utils):
#         print('下載字幕')
#         start_time = time.time()
#         new_list = []
#         threads = []
#         for yt in data:
#             if utils.captions_exist(yt):
#                 continue
#             new_list.append(yt)
#         for i in range(len(new_list)):
#             t = Thread(target=self.download_and_save, args=[new_list[i]])
#             t.start()
#             threads.append(t)
#         for a in threads:
#             a.join()
#         end_time = time.time()
#         print('mulit-threading[2]耗時：', end_time - start_time)
#         return data
#
#     def download_and_save(self, yt):
#             sourse = YouTube(yt.url)
#             try:  # 只抓取a.en字幕,跳過無字幕及非a.en字幕的影片
#                 en_caption = sourse.captions['a.en']
#                 captions = en_caption.generate_srt_captions()
#             except KeyError:
#                 return
#             except AttributeError:
#                 return
#             with open(yt.caption_path, 'w', encoding='utf-8') as file:
#                 for line in captions:
#                     file.write(line)
#             return


# class DownloadCaption(Step):  # 原始
#     def process(self, data, inputs, utils):
#         print('下載字幕')
#         start_time = time.time()
#         for yt in data:
#             if utils.captions_exist(yt):
#                 continue
#             sourse = YouTube(yt.url)
#             try:  # 只抓取a.en字幕,跳過無字幕及非a.en字幕的影片
#                 en_caption = sourse.captions['a.en']
#                 captions = en_caption.generate_srt_captions()
#             except KeyError:
#                 continue
#             except AttributeError:
#                 continue
#             with open(yt.caption_path, 'w', encoding='utf-8') as file:
#                 for line in captions:
#                     file.write(line)
#         end_time = time.time()
#         print('原始耗時：',end_time - start_time)
#         return data
# class DownloadCaption(Step):  # multi-threading3
#     def process(self, data, inputs, utils):
#         print('下載字幕')
#         start_time = time.time()
#         threads = []
#         for yt in data:
#             if utils.captions_exist(yt):
#                 continue
#             t = Thread(target=self.download_and_save, args=([yt],))
#             t.start()
#             threads.append(t)
#         for thread in threads:
#             thread.join()
#         end_time = time.time()
#         print('mulit-threading[3]耗時：', end_time - start_time)
#         return data
#
#     def download_and_save(self, data):
#         for yt in data:
#             sourse = YouTube(yt.url)
#             try:  # 只抓取a.en字幕,跳過無字幕及非a.en字幕的影片
#                 en_caption = sourse.captions['a.en']
#                 captions = en_caption.generate_srt_captions()
#             except KeyError:
#                 continue
#             except AttributeError:
#                 continue
#             with open(yt.caption_path, 'w', encoding='utf-8') as file:
#                 for line in captions:
#                     file.write(line)
#         return
