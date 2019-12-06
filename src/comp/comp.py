# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
subD = "D"
for human in humans:
    if subD in human.name[0:1]:
        a.append(human.name)
# for capDName in humans:
#     print(capDName)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
subs="e"
for human in humans:
    # print(len(human.name)-1)
    if subs in human.name[len(human.name)-1]:
        b.append(human.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
subCG = ["C", "D", "E", "F", "G"]
for human in humans:
    for sub in subCG: 
        if sub in human.name[0:1]:
            c.append(human.name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for human in humans:
    d.append(human.age + 10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for human in humans:
    e.append(human.name + "-" + str(human.age))
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for human in humans:
    if 27 <= human.age <= 32:
        f.append((human.name, human.age))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
humans_copy = humans[:]
# print(humans_copy)
# print(humans)
for human in humans_copy:
    upperName = human.name.upper()
    age5 = human.age + 5
    # newHuman = upperName, age5
    g.append(Human(upperName, age5))
print(g)
# print(humans)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
for human in humans:
    h.append(math.sqrt(human.age))
print(h)
