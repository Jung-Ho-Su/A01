# https://www.youtube.com/watch?v=DChma7YcQ7I

import yt_dlp

# 다운로드하고 싶은 유튜브 주소
video_url = 'https://www.youtube.com/watch?v=DChma7YcQ7I'

# 다운로드 옵션 설정
ydl_opts = {
    # 'bestvideo+bestaudio'를 쓰면 화질은 좋으나 ffmpeg가 필수입니다.
    # 'best'는 비디오와 오디오가 이미 합쳐진 가장 좋은 단일 파일을 가져옵니다.
    'format': 'best',

    # 저장될 파일명 형식 (제목.확장자)
    'outtmpl': 'downloaded_video.%(ext)s',

    # 라이브 스트리밍일 경우 끝날 때까지 기다리지 않고
    # 현재 시점까지 다운로드 후 종료하려면 아래 옵션을 조절할 수 있습니다.
    'live_from_start': False,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("다운로드를 시작합니다...")
        ydl.download([video_url])
        print("\n다운로드가 완료되었습니다!")
except Exception as e:
    print(f"에러가 발생했습니다: {e}")