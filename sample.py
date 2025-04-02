import random


class Animal:
    def say(self) -> None:
        raise NotImplementedError()


class Dog(Animal):
    def say(self) -> None:
        print("Bark")


class Cat(Animal):
    def say(self) -> None:
        print("Meow")


def create_animal() -> Animal:
    if random.random() < 0.5:
        return Dog()
    else:
        return Cat()


animals = []

for _ in range(5):
    animals.append(create_animal())

for animal in animals:
    animal.say()




'''
Animal=基底クラス
疎結合→他のクラスや関数の中身を変えた時にそれが影響する範囲をできる限り少なくする


'''