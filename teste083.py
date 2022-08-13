from youtube_dl import YoutubeDL
video_info = YoutubeDL().extract_info(
    url = 'https://www.youtube.com/watch?v=SJPEL8eY4I4',download=False
)
filename = f"{video_info['title']}.mp3"
options={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl':filename,
}

with YoutubeDL(options) as ydl:
    ydl.download([video_info['webpage_url']])