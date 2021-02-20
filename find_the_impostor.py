import random
print("Welcome to Among Us<guess>")
print("___________________")
print("The spaceship has 4 people left <inclue you>")
print("____________________________________________")
print("You have to find the impostor by input 1, 2 or 3 for the first/second/third person <not include you> ")
guess = int(input("Input here( if you input the number > 3, he won't be the imposter and one person of 3 people left <not include you> will be ejected :  "))
if guess == random.randint(1,3):
    print("Yoo, you have ejected the impostor")
else:
    print("Noo, he was not The Impostor")
    print("Eject on more person")
    number = int(input("Input number 1 or 2( the first left person and the second left person : "))
    if number == random.randint(1,2):
        print("Yes, you have kicked the imposter")
    else:
        print("Noo, he was not The Imposter")
        print("____________________________")
        print("So the left person is the imposter")
        print("_______________________________________")
        print("GAME OVER")

    




