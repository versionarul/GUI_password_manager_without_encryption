import random

def generate_password():
    letter_string = ("a b c d e f g h i j k l m n o p q r s t u v x y z A B C D E F G H I J K L M N O P Q R S T U V X Y Z")
    number_string = ("0 1 2 3 4 5 6 7 8 9")
    symbol_string = (". , ! @ # $ % ^ & * ( ) + - > < ; :")

    letters = letter_string.split(" ")
    numbers = number_string.split(" ")
    symbols = symbol_string.split(" ")

    nr_letters = random.randint(8,10)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))
    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    password = "".join(password_list)
    return password