


class Found():
    def __init__(self, yt, caption, time):
        self.yt = yt
        self.caption = caption
        self.time = time
        self.start_time = self.get_start_time()
        self.end_time = self.get_end_time()

    def get_start_time(self):
        return self.time.split(' --> ')[0]

    def get_end_time(self):
        return self.time.split(' --> ')[-1]

    def __str__(self):  # 簡易說明
        return f'<Found_{self.yt}>'

    def __repr__(self):  # 詳細說明
        info = ' ; '.join([
            'yt=' + str(self.yt),
            'caption=' + str(self.caption),
            'time=' + str(self.time),
        ])
        return f'<Found({info})>'
