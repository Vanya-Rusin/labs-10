class progression:
    def __init__(self, a1, d):
        self.a1 = a1
        self.d = d

    def first_task(self):
        self.a1 = float(input('введіть значення a1'))

    def seckond_task(self):
        self.d = float(input('введіть значення d'))

    def third_task(self):
        self.n = int(input('введіть значення n '))
        print(self.a1 + (self.n * self.d))

    def fourth_task(self):
        self.n = int(input('введіть значення n '))
        self.s = self.a1 + (self.n * self.d)
        print((self.s / 2) * self.n)


progression1 = progression(2,2)
progression1.first_task()
progression1.seckond_task()
progression1.third_task()
progression1.fourth_task()
