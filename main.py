
# 10-m
class VideoPlayer:
    def __init__(self, title):
        self.title = title

    def play_video(self, seconds):
        print(f"{self.title} videosi {seconds} soniya o‘ynalmoqda")


class MusicPlayer:
    def play_music(self):
        print("Musiqa ijro etilmoqda")


class Computer:
    def open_media(self, obj, seconds):
        if hasattr(obj, "play_video"):
            obj.play_video(seconds)
        else:
            print("play_video method topilmadi")


video = VideoPlayer("Dars")
music = MusicPlayer()

pc = Computer()
pc.open_media(video, 60)

pc.open_media(music, 60)
