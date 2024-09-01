class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            print(new_floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name
        return self.number_of_floors


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Золотой Родник', 9)
h = [h1, h2, h3]
for i in range(3):
    print('Название:', str (h[i]), ', кол-во этажей:', len(h[i]))
for i in range(3):
    print(len(h[i]))
h2.go_to(7)
