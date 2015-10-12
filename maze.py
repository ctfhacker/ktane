#!/usr/bin/env python
from collections import defaultdict
from colors import color
import sys

mazes = {
(('1','2'), ('6','3')): """
x x x|x x x
  -     - -
x|x x|x x x
    - - -  
x|x x|x x x
  -     -  
x|x x x|x x
  - - - -  
x x x|x x|x
  -     -  
x x|x x|x x
""",
(('5','2'), ('2','4')): """
x x x|x x x
-   -     -
x x|x x|x x
  -   - -  
x|x x|x x x
    -   -  
x x|x x|x|x
  -   -    
x|x|x|x x|x
        -  
x|x x|x x x
""",
(('4','4'), ('6','4')): """
x x x|x|x x
  -        
x|x|x|x x|x
-     - -  
x x|x|x x|x
           
x|x|x|x|x|x
           
x|x x|x x|x
           
x x x x|x x
""",
(('1','1'), ('1','4')): """
x x|x x x x
    - - -  
x|x|x x x x
      - -  
x|x x|x x|x
  - -   -  
x|x x x x x
  - - - -  
x x x x x|x
  - - -    
x x x|x x|x
""",
(('5','3'), ('4','6')): """
x x x x x x
- - - -    
x x x x x|x
  - -   - -
x x|x x|x x
    - -    
x|x x x|x|x
  - -   -  
x|x x x x|x
    - - -  
x|x x x x x
""",
(('5','1'), ('3','5')): """
x|x x|x x x
      -    
x|x|x|x x|x
        -  
x x|x|x|x x
  - -     -
x x|x x|x|x
-          
x x|x|x|x x
  - -   -  
x x x x|x x
""",
(('2','1'), ('2','6')): """
x x x x|x x
  - -      
x|x x|x x|x
    - - -  
x x|x x|x x
- -   -   -
x x|x x x|x
      - -  
x|x|x x x|x
  - - -    
x x x x x x
""",
(('4','1'), ('3','4')): """
x|x x x|x x
    -      
x x x|x x|x
  - - - -  
x|x x x x|x
    - -    
x|x x|x x x
  -   - - -
x|x|x x x x
    - - - -
x x x x x x
""",
(('3','2'), ('1','5')): """
x|x x x x x
    - -    
x|x|x x|x x
      -    
x x x|x x|x
  - -   -  
x|x|x x|x x
      - -  
x|x|x|x x|x
          -
x x|x x|x x
""",
}

def get_maze_dict(maze):
    maze_dict = defaultdict(list)
    maze = maze[1:]
    maze = maze.split('\n')

    for row_index, line in enumerate(maze):
        for col_index, item in enumerate(line):
            if item == 'x':
                col = col_index/2+1
                row = row_index/2+1
                try:
                    if maze[row_index+1][col_index] == ' ':
                        maze_dict[(col, row)].append(('D', (col, row+1)))
                except:
                    pass
                try:
                    if maze[row_index-1][col_index] == ' ':
                        maze_dict[(col, row)].append(('U', (col, row-1)))
                except:
                    pass
                try:
                    if maze[row_index][col_index+1] == ' ':
                        maze_dict[(col, row)].append(('R', (col+1, row)))
                except:
                    pass
                try:
                    if maze[row_index][col_index-1] == ' ':
                        maze_dict[(col, row)].append(('L', (col-1, row)))
                except:
                    pass

    return maze_dict

def easy_answer(answer):
    count = 0
    curr_letter = answer[0]
    curr_answer = ''

    for index, letter in enumerate(answer):
        left = start[index:]
        if letter != curr_letter:
            curr_answer += curr_letter + str(count) + ' '
            curr_letter = letter
            count = 1
        else:
            count += 1

    curr_answer += curr_letter + str(count)

    return curr_answer
    

def traverse_maze(maze_dict, start, finish):
    path = [[('x', start)]]
    while True:
        for curr_path in path:
            temp_path = curr_path[:]
            new_paths = maze_dict[temp_path[-1][1]]
            for new_path in new_paths:
                if finish == new_path[1]:
                    answer = ''
                    for pair in (temp_path + [new_path])[1:]:
                        answer += pair[0]

                    print "Path: ", color(easy_answer(answer), 'green')
                    sys.exit(1)
                else:
                    path.append(temp_path + [new_path])

def get_maze(indicator):
    for indicators,maze in mazes.iteritems():
        if indicator in indicators:
            return maze

    return ''

# If users input , or spaces, we ignore them
indicator = raw_input("Indicator: ")
indicator = tuple(indicator.replace(',', '').replace(' ',''))

start = raw_input("Start: ")
start = tuple([int(num) for num in start.replace(',', '').replace(' ','')])

finish = raw_input("Finish: ")
finish = tuple([int(num) for num in finish.replace(',', '').replace(' ','')])

maze = get_maze(indicator)
maze_dict = get_maze_dict(maze)
traverse_maze(maze_dict, start, finish)
