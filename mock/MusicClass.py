class Song:
    def __init__(self, name, genre, durations):
        self.name = name
        self.genre = genre
        self.durations = durations
    
    def show_info(self):
        mi = self.durations // 60
        sec = self.durations - mi*60
        if sec < 10:
            sec = "0"+str(sec)
        return self.name + " <|> " + self.genre + " <|> " + str(mi)+"."+str(sec)

Rickroll = Song(input(), input(), int(input()))
print(Rickroll.show_info())