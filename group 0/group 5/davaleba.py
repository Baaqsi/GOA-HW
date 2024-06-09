"""
##2
age1 = 18
age2 = 14
age3 = 47
age4 = 48

age4 = age4 + 10
age2 = age2 + 10
calc = age4 // age2

print(calc)
"""


"""
##4
#2)
old1 = 14
old2 = 18
old3 = 47
old4 = 48

new1 = old1 + 20
new2 = old2 + 20
new3 = old3 + 20
new4 = old4 + 20

print(f"mama: {new4} , deda: {new3}, dzma: {new2} , me: {new1}")

#3)
user1 = input("enter your sister/brother's age (if u have one): ")
user2 = input("enter your mother's age: ")
user3 = input("enter your father's age: ")
user4 = input("enter your  age: ")

print(f"mother's age: {user2} , fathers age: {user3}, sister/brother's age: {user1}, your age: {user4}")
"""


"""
#?
salary = int(input("enter your salary: "))

if salary > 10000:
    print("did u study at GOA? ")
elif salary >= 1000 and salary <= 10000:
    print("YOU MID ")
elif salary < 1000:
    print("why did'nt you join GOA?!?  ")
else:
    print("nice salary my g ")
"""


"""
#?
i = 0
while i <= 30:
    i = i + 1
    if i % 2 == 0:
        print(f"{i} aris luwi")
    else:
        print(f"{i} aris kenti")
    if i == 30:
        break
        

ticket = 25
adult = 10
children = 3

charge = ticket * adult - children * 0
print(charge)
"""

"""
i = 0
while i <= 100:
    i = i + 1
    if i % 5 == 0:
        print(i)
    else:
        pass
        
"""
"""
x = [2, 4, 6, 2, 4, 7, 2, 9]

def yup(x):
    k = []
    for i in x:
        if i  != 4:
            k.append(i)
    return k

print(yup(x))
"""
"""
#?
family = ["14", "18", "47", "48"]
print("my age is: {}, my brotha's age is: {} my mom's age is: {} my da's age is: {}".format(family[0], family[1], family[2], family[3]))

family_plus_10 = [str(int(age) + 10) for age in family]

print("my age is: {}, my brotha's age is: {} my mom's age is: {} my da's age is: {}".format(family_plus_10[0], family_plus_10[1], family_plus_10[2], family_plus_10[3]))
"""
"""
#1
def triangle(x,y,z):
    if x + y > z:
        print("es samkutxedi sworea")
    else:
        print("es samkutxedi ar arsebobs")
    
triangle(3,4,5)

#2
def names(nam1, nam2, nam3):
    listt = [nam1, nam2, nam3]
    return ', '.join(listt)

print(names("givi", "gio", "trundle"))
"""