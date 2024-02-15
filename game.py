import random


#number = int(input("Enter a number between 1 and 100: "))
def GameRevers():
    low = 1
    big = 100
    count_max = 5
    count = 0
    print('Guess the number')
    print('comp has only 5 attempts')

    while True:
        
        count += 1
        #print(f'action {count}')

        if count > count_max:
            print('You win!')
            break
        
        comp_num = random.randint(low,big)
        print(f'number from comp: {comp_num}')

        user_stap = input("you need use <, >, = : ")
        if user_stap == '=':
            print('comp win')
            break
        elif user_stap == '>':
            low = comp_num + 1
        elif user_stap == '<':
            big = comp_num - 1

def GameUser():
    number = random.randint(1,100)
    #print(number)

    user_num = None
    count = 0

    levels = {1:10, 2:5, 3:3}
    level = int(input('select difficulty level from 1 to 3: '))
    max_count = levels[level]
    user_count = int(input('enter the number of users: '))
    users = []

    for i in range(user_count):
        user_name = input(f'enter name of user {i+1}: ')
        users.append(user_name)
    print(users)

    is_winner = False
    winner_name = None

    while not is_winner:
        count += 1
        if count > max_count:
            print('game over')
            break
        print(f'Attemp N: {count}')
        
        for user in users:
            print(f'step of user: {user}')

            # step 2. Ask user to enter the number
            user_num = int(input(f'{user} your number: '))
            if user_num == number:
                is_winner = True
                winner_name = user
                break
            #step 3. Comparison of numbers. Output of the results
            elif number < user_num:
                print('your number is bigger than expected')
            else:
                print('your number is less than expeted')
    else:
        print(f'congratulation! {winner_name}!')

def Game():
    print('choice game')
    print('if you want to guess the number from the computer type 1')
    print('if you want the computer to guess your number, type 2')
    num = int(input(''))
    if num == 1:
        GameUser()
    if num == 2:
        GameRevers()

if __name__ == '__main__':
    Game()
    GameRevers()
    GameUser()