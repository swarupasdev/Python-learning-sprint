import yt_dlp
import pandas as pd

playlist_url = "https://www.youtube.com/watch?v=OtYEY2htIjM&list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU"

ydl_opts = {
    "quiet": True
}
videos_data = []
total_seconds = 0

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    playlist = ydl.extract_info(playlist_url, download=False)

    for index, video in enumerate(playlist['entries'], start=1):
        title = video.get("title")
        duration = video.get("duration", 0)
        video_id = video.get("id")

        total_seconds += duration
        hrs = duration // 3600
        mins = (duration % 3600) // 60
        secs = duration % 60

        formatted = (
            f"{hrs:02}:{mins:02}:{secs:02}"
            if hrs > 0 else
            f"{mins:02}:{secs:02}"
        )

        videos_data.append({
            "No": index,
            "Title": title,
            "Duration": formatted,
            "URL": f"https://youtube.com/watch?v={video_id}"
        })

df = pd.DataFrame(videos_data)
df.to_csv("python_dsa.csv", index=False)

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60

print("CSV generated: playlist.csv")
print(f"Total playlist watch time: {hours} hours {minutes} minutes")