fileName = input("File Name : ")
try:
  f = open(fileName,"r")
  text = f.read()
  text = text.replace('\n','')
  f.close()
except:
  print('File does not exist')
  exit(1)


print("\nMaze input")
column = int(input("Maze Column Number : "))
row = int(input("Maze Row Number : "))

print("\nExecution code for {} x {} Maze".format(row,column))

# set maze matrix
maze = [[text[j*column + i] for i in range(column)] for j in range(row)]


sPoint = (-1,-1)  # Start Point
check = False
for i in range(column):
  for j in range(row):
    if maze[j][i] == '5':
      check = True
      sPoint = (j , i)
      break
  if check:
    break

if not check:
  print("Not Find Start Point")
  exit(0)



path = ['5']
keys = []
mazeElements = ['1','0','6','8','4','2','5','9']  # 1:wall, 0:road, 6:right, 8:up, 4:left, 2:down, 5:start, 9:finish
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



def printResult():
  path.append('9')

  print("\nPath : {}".format(path))
  print("\nDirections :\nStart")
  count = 1
  for i in range(len(path)-1):
    if(path[i] == path[i+1]):
      count += 1
    else:
      if(path[i] == '6'):
        print(count , " unit right")
      elif(path[i] == '8'):
        print(count , " unit up")
      elif(path[i] == '4'):
        print(count , " unit left")
      elif(path[i] == '2'):
        print(count , " unit down")
      elif(path[i] in lowercase):
        print("key '{}' received".format(path[i]))
      count = 1
  
  print("End point Reached")
  exit(0)



def moveBackInPath(val):
  # if go back, delete last element and no append val to path. Because we want to shortest path.
  if(path[-1] == str(10-int(val))):
    del path[-1]
    return
  path.append(val)



def move(x, y, direction, lastDirection):
  if(maze[y][x] == '0' or maze[y][x] in lowercase or (maze[y][x] in uppercase and maze[y][x].lower() in keys) or maze[y][x] == '9') and direction != str(10-int(lastDirection)):
    path.append(direction)
    findFinish( x, y, direction)
    # Go back
    moveBackInPath(str(10 - int(direction)))



def findFinish( x, y, lastDirection):
  global maze

  if( maze[y][x] == '9'):
    printResult()

  if(maze[y][x] in lowercase):
    path.append(maze[y][x])
    keys.append(maze[y][x])
    maze[y][x] = '0'
  
  elif(maze[y][x] in uppercase):
    maze[y][x] = '0'


  move(x+1, y, '6', lastDirection) # move right

  move(x, y+1, '2', lastDirection) # move down

  move(x, y-1, '8', lastDirection) # move up

  move(x-1, y, '4', lastDirection) # move left
  
  # If there is no direction to go, reassessing earlier directions
  move(x+1, y, '6', lastDirection) # move right

  move(x, y+1, '2', lastDirection) # move down

  move(x, y-1, '8', lastDirection) # move up





findFinish(x=sPoint[1], y=sPoint[0], lastDirection=0)


print("\nThe task failed.\nFinish wasn't found.")