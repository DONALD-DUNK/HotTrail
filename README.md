# HotTrail

## Members
    Tillman Tate - Project manager
    Bennett Judd - Coder
    Elliot Maw - Visual Designer
    Bikram - Audio designer/Project Researcher
    Joe rinehart - Coder
    
## Project objective
Hot Trail is a side-scrolling game where you play as a criminal fleeing from the police.
Just press play after the logo, and you'll find yourself navigating through alleys while being chased by cops.
It's all about dodging and escaping in this fast-paced adventure!
## Ui and Logic planning and classes
GameController Class:

## GameController()
### Member Variables:
player: Reference to the player character object.
police: List of police characters chasing the player.
score: Integer to keep track of the player's score.
level: Integer indicating the current level.
Methods:
startGame(): Begins the game loop.
update(): Updates the game state each frame.
endGame(): Ends the game and displays the final score.
Player Class:

## Player()
![Player idle sprite](https://github.com/DONALD-DUNK/SideScroller/blob/main/images/character_idle_side_hi.gif?raw=true)
### Member Variables:
position - this is the current position of the player on the screen.
velocity this is the speed and direction of player movement.
health this is the current health of the player.
### Methods:
moveLeft() - this if for moves the player character left.
moveRight(): Moves the player character right.
jump(): Makes the player character jump.
attack(): Initiates an attack or special action.
Police Class:


## Enemy()
### Member Variables:
position: Current position of the enemy on the screen.
velocity: Speed and direction of enemy movement.
aggression: Level of aggression of the enemy (determines behavior).
### Methods:
patrol(): Initiates a standard patrol behavior.
chasePlayer(): Makes the police character pursue the player.
attackPlayer(): Initiates an attack on the player.
Obstacle Class:

## Obstacle()
### Variables:
position - this is the Current position of the obstacle on the screen.
size - is the size or Dimensions of the obstacle.
### Methods:
collideWithPlayer() - this will Determine if the player collides with the obstacle.
collideWithPolice() - this will Determine if the police collide with the obstacle.
We could also have a class for the score if needed or if we add it
![class diagram](https://github.com/DONALD-DUNK/SideScroller/blob/main/images/Screenshot%202024-03-01%20at%2010.26.15%20AM.png?raw=true)

![GUI mockup](https://github.com/DONALD-DUNK/SideScroller/blob/main/images/image.jpg?raw=true)

# Progress of sidescroller
## First level of development added movement
![first movement screen](https://github.com/DONALD-DUNK/SideScroller/blob/main/images/Screenshot%202024-02-22%20at%209.18.09%20AM.png?raw=true)


![updated startup screen](https://github.com/DONALD-DUNK/SideScroller/blob/main/images/Screenshot%202024-03-01%20at%2010.04.36%20AM.png?raw=true)

![updated startup](https://github.com/DONALD-DUNK/SideScroller/blob/main/images/Screenshot%202024-03-01%20at%2010.58.01%20AM.png?raw=true)

![updated movement screen](https://github.com/DONALD-DUNK/SideScroller/blob/main/images/Screenshot%202024-03-01%20at%2010.11.20%20AM.png?raw=true)
