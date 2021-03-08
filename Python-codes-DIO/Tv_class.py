class Television:
    def __init__(self):
        self.ligada = False
        self.canal = 4
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def canal_up(self):
        if self.ligada:
            self.canal += 1
    def canal_down(self):
        if self.ligada:
            self.canal -= 1


tv = Television()
print(tv.ligada)
tv.power()
print(tv.ligada)
tv.power()
print(tv.ligada)
tv.canal_up()
tv.canal_up()
print(tv.canal)