class Robot:
    type = 'robot'

    def __init__(self, name, age):
        self.name = name
        self.age = age

tom = Robot('tom', 10)
jerry = Robot('jerry', 15)

print("Hello! my name is Tom. I am a {}".format(tom.type))
print("Hello! my name is Jerry. I am a {}".format(jerry.type))

print("{} is {} years old.".format(tom.name, tom.age))
print("{} is {} years old.".format(jerry.name, jerry.age))


