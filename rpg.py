class Character():

    def __init__(self, name, level):
        self.name = name
        self.level = level
        
    @classmethod #декоратор, выделяет некоторую особенность метода
    def from_string(cls, data):
        pars = data.split(',')
        return cls(pars[0], int(pars[1]))

    @staticmethod #не соответствует оопшной парадигме
    def can_join(c1, c2): #можем не передавать ни метод ни класс, лучше не использовать
        
        return abs(c1.level - c2.level) < 5
        

char1 = Character.from_string('Archer, 10')
char2 = Character.from_string('Warrior, 7')

print(char1.can_join(char1, char2))
