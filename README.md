# Escape-from-Maze
Looking for a way out of a maze

As an example, it is aimed to find the shortest exit way of a labyrinth designed as in the shared 'maze.txt' file. This maze consists of walls, doors and keys. Doors are defined as obstacles like walls. The program needs to collect the keys in order to pass the doors.

Maze elements are defined as "1: wall, 0: road, 5: start, 9: finish". The program follows the '0s until exit, collects the keys. It leaves information about the direction in which it travels (6: right, 8: up, 4: left, 2: down).

![Ekran Alıntısı](https://user-images.githubusercontent.com/37874147/81610596-756a1580-93e2-11ea-9c4e-fc5ddbab9a7f.JPG)


Every move made is added to the path array. But when a wrong path is entered, this motion information must be deleted from the path because we want the shortest path. I used a variable called 'amINecessary' to control this process. The necessity of the operation with this variable is checked. If there is an finish point or key in current location or later, this move is required. Otherwise, this move is unnecessary and is deleted from the path.

The program generally finds the starting point. However, it does not work in case it has to pass from where it has passed. I have not solved this problem yet.

A failed example

![Ekran Alıntısı](https://user-images.githubusercontent.com/37874147/81609793-28d20a80-93e1-11ea-9961-43ad9ba8bb5f.JPG)

Cannot follow the path drawn in blue. So it can't find the exit
