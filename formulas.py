# 2) Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

# 2) Has a function to calculate the circumference of a circle

# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

def cal(l,w):
    area = l * w
    
    return area

#print(cal())


def cir(r):
    circle = 2 * 3.1416 * r

    return circle

#print(cir())

