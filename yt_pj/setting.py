import os
from dotenv import load_dotenv
load_dotenv()  # 載入.env 到環境變數中

API_KEY = os.getenv('API_KEY')  # 讀取環境變數

# 也有人單純存在檔案,使用第三方套件configparser載入（配置檔載入）


DOWNLOADS_DIR = 'downloads'
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
