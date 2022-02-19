import cls
pet_num = int(input())
pets = []
for _ in range(pet_num):
    x, y, t = map(int, input().split())
    pet = Animal(x, y, t)
    pets.append(pet)

human_num = int(input())
humans = []
for _ in range(human_num):
    x, y = map(int, input().split())
    human = Human(x, y)
    humans.append(x, y)

for loop in range(300):
    print("."*human_num)



