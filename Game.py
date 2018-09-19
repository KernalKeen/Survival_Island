
BANNER = '''
  _____ __ __  ____  __ __  ____  __ __   ____  _          ____  _____ _       ____  ____   ___   
 / ___/|  T  T|    \|  T  |l    j|  T  | /    T| T        l    j/ ___/| T     /    T|    \ |   \  
(   \_ |  |  ||  D  )  |  | |  T |  |  |Y  o  || |         |  T(   \_ | |    Y  o  ||  _  Y|    \ 
 \__  T|  |  ||    /|  |  | |  | |  |  ||     || l___      |  | \__  T| l___ |     ||  |  ||  D  Y
 /  \ ||  :  ||    \l  :  ! |  | l  :  !|  _  ||     T     |  | /  \ ||     T|  _  ||  |  ||     |
 \    |l     ||  .  Y\   /  j  l  \   / |  |  ||     |     j  l \    ||     ||  |  ||  |  ||     |
  \___j \__,_jl__j\_j \_/  |____j  \_/  l__j__jl_____j    |____j \___jl_____jl__j__jl__j__jl_____j
'''

print(BANNER)

name = input("Enter Your Username: ")
print("Hello", name)

food = 10

while food > 0:
    print ("Food:", food)
    move = input("What Do You Want To Do? ")

    if move == "eat":
        print("You Eat A Sandwich.")
        food += 5 

    elif move == "chill":
        print("Sure... I Guess.")

    elif move == "quit":
        break

    food -= 1 

print("GAME OVER")