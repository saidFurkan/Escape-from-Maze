
fileName = input("File Name : ")
try:
  f = open(fileName,"r")
  text = f.read()
  text = text.replace('\n','')
  f.close()
except FileNotFoundError:
  print('File does not exist')
except:
  print("The file could not be read")
  exit(1)


print("\nMaze input")
column = int(input("Maze Column Number : "))
row = int(input("Maze Row Number : "))

print("\nExecution code for {} x {} Maze".format(row,column))

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



path = []
mazeElements = ['1','0','6','8','4','2','5','9']  # 1:wall, 0:road, 6:right, 8:up, 4:left, 2:down, 5:start, 9:finish
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def manipulatePath(x, y, amINecessary):
  global maze

  if amINecessary:
    if(maze[y][x] not in lowercase):
      path.append(str(10- int(maze[y][x])))
  else:
    path.pop()



def findFinish( x, y, keys, amINecessary=False):
  global maze

  if(maze[y][x] in lowercase):
    path.append(maze[y][x])
    keys.append(maze[y][x])
    maze[y][x] = '7'
    amINecessary = True

  if( maze[y][x] == '9'):
    path.append('9')

    print("\nDirections :")
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

    print("\nMaze :")
    for i in range(10):
      print(maze[i])
    exit(0)
  

  if(maze[y][x+1] == '0' or maze[y][x+1] in lowercase or (maze[y][x+1] in uppercase and maze[y][x+1].lower() in keys) or maze[y][x+1] == '9'):
    maze[y][x] = '6'
    path.append('6')
    if findFinish( x+1, y, keys): amINecessary = True
    manipulatePath(x, y, amINecessary)
  
  if(maze[y][x-1] == '0' or maze[y][x-1] in lowercase or (maze[y][x-1] in uppercase and maze[y][x-1].lower() in keys) or maze[y][x-1] == '9'):
    maze[y][x] = '4'
    path.append('4')
    if findFinish( x-1, y, keys): amINecessary = True 
    manipulatePath(x, y, amINecessary)
  
  if(maze[y+1][x] == '0' or maze[y+1][x] in lowercase or (maze[y+1][x] in uppercase and maze[y+1][x].lower() in keys) or maze[y+1][x] == '9'):
    maze[y][x] = '2'
    path.append('2')
    if findFinish( x, y+1, keys): amINecessary = True
    manipulatePath(x, y, amINecessary)
  
  if(maze[y-1][x] == '0' or maze[y-1][x] in lowercase or (maze[y-1][x] in uppercase and maze[y-1][x].lower() in keys) or maze[y-1][x] == '9'):
    maze[y][x] = '8'
    path.append('8')
    if findFinish( x, y-1, keys): amINecessary = True
    manipulatePath(x, y, amINecessary)

  return amINecessary


findFinish(x=sPoint[1], y=sPoint[0], keys=[])

print("\nThe task failed.\nFinish wasn't found.")