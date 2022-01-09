from yt_pj.pipeline.steps.get_video_list import GetVideoList
from yt_pj.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCQq36RYp2AKIftKhQGXElXA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()


# yt = pytube.YouTube('https://www.youtube.com/watch?v=8jo0ojNgpR8')
# yt_caption = yt.captions['a.en']
# print(yt_caption.xml_captions)
# S = yt_caption.xml_captions.splitlines()
#
# newlines = []
# memoryword = ''
# memorytime = ''
#
# for line in S:
#     for word in line:
#         if word == '<':
#             do_type = 'get_time'
#             memoryword += ' '
#         elif word == '>':
#             do_type = 'get_word'
#
#         else:
#             if do_type == 'get_time':
#                 if word == ' ':
#                     for firstword in memorytime:
#                         if firstword == 't':
#                             memoryword += memorytime
#                         else:
#                             memorytime = ''
#                 else:
#                     memorytime += word
#                 # continue
#             elif do_type == 'get_word':
#                 memoryword += word
#
# newlines = memoryword.split()
# for line in newlines:
#     print(line)


# url_list = get_all_video_in_channel(CHANALL_ID, API_KEY)
# API_KEY_Y=AIzaSyBe3oxJ0moiKlBC965J3S42eotO_dZlz60
