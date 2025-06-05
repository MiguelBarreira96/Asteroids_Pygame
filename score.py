class Score:
    def __init__(self):
        self.value = 0

    def add_points(self, points):
        self.value += points

    def reset(self):
        self.value = 0

    def get_score(self):
        return self.value