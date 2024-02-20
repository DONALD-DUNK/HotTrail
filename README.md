# HotTrail

## Members
    Tillman Tate - Project manager
    Bennett Judd - Coder
    Elliot Maw - Audio/Visual Designer
    Bikram - Project Researcher
    Joe rinehart - 
    
## Project objective
Hot Trail is a side-scrolling game where you play as a criminal fleeing from the police.
Just press play after the logo, and you'll find yourself navigating through alleys while being chased by cops.
It's all about dodging and escaping in this fast-paced adventure!
## Ui and Logic planning and classes
GameController Class:

#Constructor: GameController()
##Member Variables:
player: Reference to the player character object.
police: List of police characters chasing the player.
score: Integer to keep track of the player's score.
level: Integer indicating the current level.
Methods:
startGame(): Begins the game loop.
update(): Updates the game state each frame.
endGame(): Ends the game and displays the final score.
Player Class:

#Constructor: Player()
##Member Variables:
position - this is the current position of the player on the screen.
velocity this is the speed and direction of player movement.
health this is the current health of the player.
##Methods:
moveLeft() - this if for moves the player character left.
moveRight(): Moves the player character right.
jump(): Makes the player character jump.
attack(): Initiates an attack or special action.
Police Class:

Constructor: Police()
Member Variables:
position: Current position of the police on the screen.
velocity: Speed and direction of police movement.
aggression: Level of aggression of the police (determines behavior).
Methods:
patrol(): Initiates a standard patrol behavior.
chasePlayer(): Makes the police character pursue the player.
attackPlayer(): Initiates an attack on the player.
Obstacle Class:

Constructor: Obstacle()
Variables:
position - this is the Current position of the obstacle on the screen.
size - is the size or Dimensions of the obstacle.
Methods:
collideWithPlayer() - this will Determine if the player collides with the obstacle.
collideWithPolice() - this will Determine if the police collide with the obstacle.
We could also have a class for the score if needed or if we add it



