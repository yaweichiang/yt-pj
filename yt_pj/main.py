import getopt
import sys
from yt_pj.pipeline.pipeline import Pipeline
from yt_pj.pipeline.steps.preflight import Preflight
from yt_pj.pipeline.steps.get_video_list import GetVideoList
from yt_pj.pipeline.steps.create_yt import CreateYT
from yt_pj.pipeline.steps.download_caption import DownloadCaption
from yt_pj.pipeline.steps.read_caption import ReadCaption
from yt_pj.pipeline.steps.download_videos import DownloadVideos
from yt_pj.pipeline.steps.search import Search
from yt_pj.pipeline.steps.editvideo import EditVideo
from yt_pj.pipeline.steps.postflight import Postflight
from yt_pj.utils import Utils

CHANNEL_ID = 'UCgc00bfF_PvO_2AvqJZHXFg'
SEARCH_WORD = 'can'


def gethelper():
    print('{:<6} {:<12},{}'.format('-h', '--helper', '取得使用說明'))
    print('{:<6} {:<12},{}'.format('-c', '-channel', '-c Youtube channel id 或 --channel <Youtube channel id> ,此參數必填'))
    print('{:<6} {:<12},{}'.format('-s', '--search', '-s 要搜尋的詞彙 ,此參數必填'))
    print('{:<6} {:<12},{}'.format('-l', '--limit', '-l 要剪輯的影片數 ,此參數須為正整數 預設值為20'))
    print('{:<6} {:<12},{}'.format('', '--cleanup', '輸入--cleanup 程式結束後會清除下載的資料 未輸入此值會保留下載資料'))


def main(argv):
    inputs = {
        'channel_id': None,
        'search_word': None,
        'limit': 20,
        'cleanup': False

    }

    try:
        opts, args = getopt.getopt(argv[1:], "hc:s:l:", ["help", "cleanup", "channel=", "search=", "limit="])
    except getopt.GetoptError:
        gethelper()
        sys.exit(2)
    print(opts)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            gethelper()
            sys.exit(0)
        elif opt == '--cleanup':
            inputs['cleanup'] = True
        elif opt in ('-c', '--channel'):
            inputs['channel_id'] = arg
        elif opt in ('-s', '--search'):
            inputs['search_word'] = arg
        elif opt in ('-l', '--limit'):
            try:
                arg = int(arg)
            except ValueError:
                print('limit參數須為正整數')
                gethelper()
                sys.exit(2)
            if arg <= 0:
                print('limit參數須為正整數')
                gethelper()
                sys.exit(2)
            inputs['limit'] = arg

    if None in (inputs['channel_id'], inputs['search_word']):
        print('有必填參數未輸入')
        gethelper()
        sys.exit(2)
    print(f'開始執行。頻道:{inputs["channel_id"]},查詢詞彙:{inputs["search_word"]}')

    steps = [
        Preflight(),
        GetVideoList(),
        CreateYT(),
        DownloadCaption(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    utils = Utils()

    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main(sys.argv)
