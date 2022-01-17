import getopt
import sys
import logging
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


def gethelper():
    print('{:<6} {:<12},{}'.format('-h', '--helper', '取得使用說明'))
    print('{:<6} {:<12},{}'.format('-c', '-channel', '-c <Youtube channel id> 或 --channel <Youtube channel id>'))
    print('{:<6} {:<12},{}'.format('-s', '--search', '-s <要搜尋的詞彙>'))
    print('{:<6} {:<12},{}'.format('-l', '--limit', '-l <剪輯片段數量> ,此參數須為正整數 預設值為20'))
    print('{:<6} {:<12},{}'.format('f', '--fast', '--fast 程式在下載時會先確認使否已有預下載之檔案,若有將直接跳過該檔案,預設值為False'))
    print('{:<6} {:<12},{}'.format('', '--cleanup', '--cleanup 程式結束後會清除下載的資料,預設值為False'))
    print('{:<6} {:<12},{}'.format('', '--sloglev', '--sloglev <stream handler level> ,預設值為全部顯示'
                                                    ',可設定為debug,info,warning,error,crittcal五個等級'))


def set_logger(lev):
    logger = logging.getLogger('log')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('log.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(lev)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


def main(argv):
    inputs = {
        'channel_id': None,
        'search_word': None,
        'limit': 20,
        'cleanup': False,
        'fast': False,
        'sloglev': logging.WARNING
    }

    try:
        opts, args = getopt.getopt(argv[1:], "hfc:s:l:", ["help", "fast", "cleanup", "channel=", "search=", "limit=",
                                                          "sloglev="])
    except getopt.GetoptError:
        gethelper()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--sloglev':
            if arg == 'debug':
                inputs['sloglev'] = logging.DEBUG
            elif arg == 'info':
                inputs['sloglev'] = logging.INFO
            elif arg == 'warning':
                inputs['sloglev'] = logging.WARNING
            elif arg == 'error':
                inputs['sloglev'] = logging.ERROR
            elif arg == 'crittcal':
                inputs['sloglev'] = logging.CRITICAL
        else:
            continue
    set_logger(inputs['sloglev'])
    logger = logging.getLogger('log')
    for opt, arg in opts:
        if opt == '--sloglev':
            continue
        elif opt in ('-h', '--help'):
            gethelper()
            sys.exit(0)
        elif opt == '--fast':
            inputs['fast'] = True
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
                logger.error('limit參數須為正整數')
                gethelper()
                sys.exit(2)
            if arg <= 0:
                logger.error('limit參數須為正整數')
                gethelper()
                sys.exit(2)
            inputs['limit'] = arg

    logger = logging.getLogger('log')

    if None in (inputs['channel_id'], inputs['search_word']):
        logger.error('頻道ID以及要搜尋的詞彙是必填參數')
        gethelper()
        sys.exit(2)
    logger.info(f'開始執行。頻道:{inputs["channel_id"]},查詢詞彙:{inputs["search_word"]}')

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
    if utils.outputs_exist(inputs) and inputs['fast']:
        logger.warning('相同設定值檔案已存在')
    else:
        p.run(inputs, utils)


if __name__ == '__main__':
    main(sys.argv)
