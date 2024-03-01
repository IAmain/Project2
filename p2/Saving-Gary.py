import turtle                           # Import the turtle module for graphical output
import random                           # Import the random module for generating random numbers
import time                             # Import the time module for time-related functions
import sys                              # Import the sys module for system-related functions
from tkinter import *                   # Import tkinter for GUI elements

root = Tk()                             # Create main Tkinter window
root.withdraw()                         # Hide window until after eula
eula = Tk()                             # Create eula Tkinter window     

# Fawziyah
def RunGame(difficulty):                # Define a function to run the game based on selected difficulty
    """This function runs the game"""
    
    if difficulty == "Beginner":        # Set parameters for Beginner difficulty
        factor = 1
        enemy_speed = 0.85
        star_speed = 2
    elif difficulty == 'Intermediate':  # Set parameters for Intermediate difficulty
        factor = 0.85
        enemy_speed = 1.5
        star_speed = 3
    else:                               # Set parameters for Expert difficulty
        factor = 0.65
        enemy_speed = 2.5
        star_speed = 4

    root.destroy()                     # Close the Tkinter window after selecting difficulty

    try:
        with open('highscore.txt', 'r') as f:  # Read the high score from a file
            high_score = int(f.read())
    except FileNotFoundError:                  # Handle the case when high score file is not found
        high_score = 0

    class Delay:                                # Define a class for introducing delays
        def __init__(self):
            """This function initializes the instance of delay"""
            self.StartTime = time.time()

        def Wait(self, delay, func):            # Method to wait for a specified delay before executing a function
            """This function waits for a delay before executing a function"""
            if time.time() >= self.StartTime + delay:
                func()
                self.StartTime = time.time()

    class MatchTimer:                           # Define a class for managing game time
        def __init__(self):
            """This function initializes an instance of the timer"""
            self.StartTime = time.time()

        def GetTime(self):                      # Method to get current game time
            """This function returns the time"""
            return time.time() - self.StartTime

        def EndMatch(self):                     # Method to end the game and record time
            """This function returns the time at the end of the game"""
            self.EndTime = self.GetTime()

        def GetNetTime(self):                   # Method to get total game time
            """This function returns the total time"""
            return self.EndTime

        # Shuhena
        def GameOver(self):
            """This function shows the game over screen"""
            #Here is a Game Over frame that shows up on the screen using Tkinter. Once the player lose all their lives the pop up comes up.
            #Once the Game over pop up comes up, it allows the user to quit/exit the game.
            Game_Over_Screen = Frame()
            Game_Over_Screen.pack()

            # Display final score and high score after game over
            pen.goto(-215, 220)
            pen.clear()
            pen.color('white')
            pen.write(f'Score: {int(timer.GetTime()) + score} \nHigh Score: {high_score} \n Game Over! ', font=("Calibri", 12, "bold"))

            #The Game Over will appear in this font type and size. 
            label_and_font = ('times', 40, 'bold')
                
            #Here it shows a Game Over pop up using Tkinter
            widget = Label(Game_Over_Screen, text= 'Game Over!', font = label_and_font).pack(side=TOP)

            #This allows the user to quit/exit the game once the game is over.
            Button(Game_Over_Screen, text = 'Quit', command= on_quit).pack(side = TOP)
            Game_Over_Screen.mainloop()
            

    ENEMY_GAP = 300                             # Set gap between enemy spawns
    STAR_GAP = 1000                              # Set gap between star spawns
    enemies = []                                # Initialize list to hold enemy turtles
    stars = []                                  # Initialize list to hold star turtles

    score = 0  
    #star_speed = 3                                 # Initialize score
    # Fawziyah
    def create_enemy():                         # Function to create an enemy turtle
        """This function creates enemies"""
        # Create and customize the enemy turtle
        enemy = turtle.Turtle()
        enemy.ht()
        enemy.speed(0)
        enemy.penup()
        enemy.shape("shark.gif")
        enemy.shapesize(3, 3)
        enemy.goto(random.choice([-200, -100, 0, 100, 200]), 350 + ENEMY_GAP * len(enemies))
        enemy.st()
        enemies.append(enemy)                   # Add the enemy turtle to the list
    # Fawziyah
    def create_star():                          # Function to create a star turtle
        """This function creates the stars"""
        # Create and customize the star turtle
        star = turtle.Turtle()
        star.ht()
        star.speed(0)
        star.penup()
        star.shape("star.gif")
        star.shapesize(3, 3)
        star.goto(random.choice([-200, -100, 0, 100, 200]), 350 + STAR_GAP * len(stars))
        star.st()
        stars.append(star)                      # Add the star turtle to the list
    # Fawziyah
    def check_collision(obj1, obj2):           # Function to check collision between two objects
        """This function checks for a collision with a larger distance"""
        return obj1.distance(obj2) < 50        # Return True if collision occurs, False otherwise
    # Fawziyah
    def check_collision2(obj1, obj2):          # Function to check collision with a smaller distance
        """This function checks for a collision with a smaller distance"""
        return obj1.distance(obj2) < 20        # Return True if collision occurs, False otherwise

    win = turtle.Screen()                      # Create a turtle window
    win.screensize(300, 300)                   # Set screen size
    win.bgcolor('light blue')                  # Set background color
    win.title('Saving Gary')                   # Set window title
    win.register_shape("shark.gif")            # Register image for enemy turtle
    win.register_shape("star.gif")             # Register image for star turtle

    # Create barriers on the left and right sides of the window
    barrier_left = turtle.Turtle()
    barrier_left.shape('square')
    barrier_left.penup()
    barrier_left.speed(0)
    barrier_left.shapesize(40, 8)
    barrier_left.goto(-300, 0)
    barrier_left.color('black')

    barrier_right = turtle.Turtle()
    barrier_right.shape('square')
    barrier_right.penup()
    barrier_right.speed(0)
    barrier_right.shapesize(40, 8)
    barrier_right.goto(300, 0)
    barrier_right.color('black')

    # Functions to move the turtle left and right
    # Fawziyah
    def on_left():
        """This function moves the player left"""
        if gary.xcor() > -200:
            gary.setx(gary.xcor() - 100)

    def on_right():
        """This function moves the player right"""
        if gary.xcor() < 200:
            gary.setx(gary.xcor() + 100)

    win.listen()
    win.onkeypress(on_left, 'Left')
    win.onkeypress(on_right, 'Right')

    # Set up the pen for displaying score
    pen = turtle.Turtle()
    pen.penup()
    pen.ht()
    pen.color('white')
    pen.speed(0)
    pen.goto(-220, 220)
    pen.pensize(8)

    # Create the player turtle
    gary = turtle.Turtle()
    gary.penup()
    gary.shape('turtle')
    gary.color('dark green')
    gary.shapesize(3, 3)
    gary.speed(0)
    gary.left(90)
    gary.goto(0, -150)

    clock = Delay()                         # Create instance of Delay class for controlling enemy and star creation
    clock2 = Delay()

    win.tracer(0)                           # Turn off animation

    timer = MatchTimer()                    # Create instance of MatchTimer class to track game time
    remaining_lives = 3                     # Initialize lives
    #run = True                              # Variable to control game loop
    while remaining_lives > 0:
        speed = (timer.GetTime() / 30)     # Adjust speed based on game time

        # Fawziyah
        clock.Wait(factor, create_enemy)   # Wait and create enemies
        clock2.Wait(factor *2, create_star)   # Wait and create stars

        # Update enemy positions and check for collisions
        # Fawziyah
        for enemy in enemies:
            #The player only has 3 lives to play the game. If the players lives end, the game is over.
            enemy.goto(enemy.xcor(), enemy.ycor() - enemy_speed - speed)
            if enemy.ycor() <= -320:
                enemy.reset()
                enemies.remove(enemy)
                enemy.ht()
            elif check_collision(enemy, gary):
                pen.clear()
                enemy.reset()
                enemies.remove(enemy)
                enemy.ht()
                # Shuhena
                #Once a player hits a dangerous object the lives decrease by one each time.
                remaining_lives = remaining_lives - 1


            if remaining_lives == 0:
                run = False
                print("Game Over!")
                # Compare the score with the high score and update it if necessary
                if timer.GetNetTime() + score > high_score:
                    high_score = int(timer.GetNetTime()) + score
                    with open('highscore.txt', 'w') as f:
                        f.write(str(high_score))

                timer.EndMatch()
                timer.GameOver()

        # Update star positions and check for collisions
        # Fawziyah
        for star in stars:
            star.goto(star.xcor(), star.ycor() - star_speed - speed)
            if star.ycor() <= -320:
                star.reset()
                stars.remove(star)
                star.ht()
            elif check_collision2(star, gary):
                pen.clear()
                score += 10                  # Increment the score by 10 when the turtle hits the star
                pen.write(f'Score: {int(timer.GetTime()) + score}', font=("Calibri", 12, "bold"))
                star.reset()
                stars.remove(star)
                star.ht()

        gary.goto(gary.xcor(), gary.ycor())     # Update player turtle position
        pen.goto(-220, 220)       # Update score display position
        pen.clear()                            # Clear previous score display
        pen.color('white')                     # Set color for new score display
        pen.write(f'Score: {int(timer.GetTime()) + score} \nHigh Score: {high_score} \nRemaining Lives: {remaining_lives} ',align="left", font=("Calibri", 12, "bold"))  # Display score, high score, and remaining lives.
        win.update()                           # Update the window


    win.mainloop()   # Start the Tkinter event loop

# Darbi
def on_yes():
    """This function stores the eula verification and then runs the game"""
    v = open("eula_verification.txt", "w")
    v.write("yes")                              # Update verification
    v.close()
    eula.destroy()                              # Close Eula

    root.deiconify()                            # Show difficulty menu
    root.title('Saving Gary Game Settings')    # Set window title
    root.geometry('1000x700')                    # Set window size
    root.config(bg='light blue')                     # Set background color

    f = open('gary_instructions.txt', 'r')      # Open instructions
    instructions = f.read()                     # Store instructions
    f.close()                                   # Close file 
    
    T = Text(root, wrap = WORD, width = 75, height = 18) #Create text box
    T.insert(END, instructions)                 # Insert the box
    T.config(state=DISABLED)                    # Do not allow the user to change the text
    T.grid(row=1, column=0, pady=25)            # Set position and padding

    heading = Label(text='Choose Your Difficulty ')  # Create label for difficulty selection
    heading.grid(row=2,column=0,padx=275)           # Set label position and padding

    heading.config(bg='light grey' , fg='green' , font=('Calibri' , 24))  # Configure label appearance

    options = [                                   # Define options for difficulty selection
        'Beginner' ,
        'Intermediate',
        'Expert'
    ]

    clicked = StringVar()                          # Create a StringVar to hold selected difficulty
    clicked.set('Beginner')                        # Set default difficulty

    # Create dropdown menu for selecting difficulty
    drop = OptionMenu( root , clicked , *options)
    drop.config(width=20)
    drop.grid(row=3,column=0 , padx=400 , pady=75)

    # Create button to start the game
    button = Button(root , width=20 , height=3 , text='Play Game' , bg='green' , fg='white' , command=lambda:RunGame(clicked.get()))
    button.grid(row = 4 , column = 0 , padx=400 , pady=10)

    root.mainloop()  # Start the Tkinter event loop

# Darbi
def on_no():
    """This function exits the program since the user did not agree to the EULA"""
    sys.exit()                                      # Exit if user does not agree

# Darbi
def on_quit():
    """This function closes the turtle window and exits the program"""
    turtle.bye()
    sys.exit()
    
#Darbi
def main():
    """The main function checks if the EULA has been agreed to. If not, it asks the user
        to agree to it. If so, it runs the game"""
    f = open('eula_verification.txt', 'r')
    verification = f.read()
    f.close()
    #If not already agreed to, show EULA
    if verification != 'yes':
        eula.deiconify()
        #Store agreement 
        a = open('eula_agreement.txt', 'r')
        agreement = a.read()
        a.close()
        #Create text box
        eula.geometry("500x500")
        T = Text(eula, wrap = WORD, width = 50, height = 20)
        T.insert(END, agreement)
        T.config(state=DISABLED)
        T.pack(padx=10, pady=10)
        eula.title("EULA Acknowledgement")
        l = Label(eula, text="EULA")
        l.config(font = ("Georgia", 18))
        #Create yes and no buttons
        button1 = Button(eula, text = "I agree", command = on_yes)
        button2 = Button(eula, text = "I do not agree", command = on_no)
        #Show text box
        l.pack()
        button1.pack(side=RIGHT, padx=5, pady=10)
        button2.pack(side=LEFT, padx=5, pady=10)
        eula.mainloop()
    #Else launch game
    else:
        on_yes()    

# Run the main function
if __name__ == "__main__":
    main()
