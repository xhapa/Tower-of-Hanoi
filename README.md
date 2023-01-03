# Tower-of-Hanoi
## About the game
It's project is a game about tower of hanoi interface to solve it and play it, The Tower of Hanoi (also called The problem of Benares Temple or Tower of Brahma or Lucas' Tower and sometimes pluralized as Towers, or simply pyramid puzzle) is a mathematical game or puzzle consisting of three rods and a number of disks of various diameters, which can slide onto any rod. [Tower-of-Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi)

<p align="center">
  <img  src="https://i.imgur.com/fjtfU83.png" width="350" height="245" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img  src="https://i.imgur.com/1S2Psda.png" width="350" height="245" />
</p>

## How does it work?
### Main script
The ```main()``` function is called to start the game. In this function, ```pygame.init()``` is called to initialize all imported pygame modules. 
A Tower object is created and the game's main loop is started.

The loop processes events and updates the game screen with the ```draw_screen()``` function. 
This function first clears the screen, then draws the 'Reset' button and the game's title. 
It then calls the ```draw_tower()``` method of the tower object to draw the game's tower and disks on the screen.

The loop also checks for user input events, such as pressing the space bar to solve the puzzle automatically, 
clicking and dragging disks to move them, and clicking the 'Reset' button to reset the game.

If the user presses the space bar, the ```solve()``` method of the tower object is called to automatically solve the puzzle. 
This method takes four parameters: the number of disks, the initial peg, the target peg, and the auxiliary peg. 
It then uses the recursive algorithm for solving the Tower of Hanoi to move the disks from the initial peg to the target peg.

The ```main()``` function is called again at the end of the script to start the game. The ```if __name__ == '__main__'``` condition ensures 
that the game is only started if the script is run directly, and not when it is imported as a module by another script.

### Tower and Disk class
The Disk class represents a disk in the game. It has a ```__init__()``` method that takes three parameters: the disk's value, its x-coordinate position, and its y-coordinate position. The rect attribute is a pygame.Rect object that holds the dimensions and position of the disk on the game screen.

The ```move_disk()``` method is used to move the disk to a new position on the screen. The method takes a tuple containing the new x and y coordinates of the disk, and updates the rect attribute accordingly.

The get_value and set_value methods are used to access and modify the __value attribute, which holds the disk's value.

The Tower class represents the game's tower and disks. It has a ```__init__()``` method that initializes the game's attributes and sets up the initial state of the tower.

The N attribute holds the number of disks in the game. The colors attribute is a list of colors for the disks, with each color corresponding to a different disk value. The __A, __B, and __C attributes are tuples containing a list of Disk objects and a pygame.Rect object for each peg in the game. The __A peg contains the initial stack of disks, arranged in descending order of size.

The ```draw_tower()``` method is used to draw the game's tower and disks on the screen. It takes a screen parameter that represents the game screen. It first draws the base and pegs of the tower, then calls the ```draw_disks()``` method to draw the disks on the pegs.

The ```draw_disks()``` method iterates over the disks on each peg and draws them on the screen using the ```pygame.draw.rect()``` method.
