from download_media import initialize


def main():
    # URLの取得
    TARGET_URL = initialize()

    # ダウンロード
    download_media(TARGET_URL)


if __name__ == "__main__":
    main()