import os

# URLの取得
def initialize()->str:
    from dotenv import load_dotenv
    load_dotenv()

    TARGET_URL = os.getenv("TARGET_URL")
    print('-'*50)
    print(f'対象URL:{TARGET_URL}')
    print('-'*50)

    return TARGET_URL


def download_media(TARGET_URL:str):
    pass

