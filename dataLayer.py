class Peregovorka:
    def __init__(self, max_people):
        if self.max_people <= 0:
            raise ValueError("Отрицательное количество людей в переговорке")
        self.max_people = max_people
        self.freedom = 0

    def capacity(self):
        return self.max_people

    def is_free(self):
        return self.freedom

    def change_free(self):
        if self.freedom == 1:
            self.freedom = 0
        if self.freedom == 0:
            self.freedom = 1
