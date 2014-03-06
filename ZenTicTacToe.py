#Zane D. Blalock
#Tic-Tac-Toe Assigment
#Version 1.0

from graphics import *
import math

#Window's information [Easy Edit]
window_title = "(Double Click)Are you ready to play a game >=D"
window_width = 399
window_height = 399

def Draw_Grid(my_window):
    w = my_window.getWidth() #Set's w to the width of the window
    h = my_window.getHeight() #Set's h to the height of the window
    #Vert. Lines
    Line(Point(w/3, 0), Point(w/3, h)).draw(my_window)
    Line(Point((2*w)/3, 0), Point((2*w)/3, h)).draw(my_window)
    #Line(Point(w/6, 0), Point(w/6, h)).draw(my_window) #Test
    
    #Horz. Lines
    Line(Point(0, h/3), Point(w, h/3)).draw(my_window)
    Line(Point(0, (2*h)/3), Point(w, (2*h)/3)).draw(my_window)

    #Columns Testing 
    column0 = Point(w/6, 1).draw(my_window)
    column1 = Point((3*w)/6, 1).draw(my_window)
    column2 = Point((5*w)/6, 1).draw(my_window)

    #Rows Testing 
    row0 = Point(1, h/6).draw(my_window)
    row1 = Point(1, (3*h)/6).draw(my_window)
    row2 = Point(1, (5*h)/6).draw(my_window)


def Draw_X(row, column, my_window):
    w = my_window.getWidth() #Set's w to the width of the window
    h = my_window.getHeight() #Set's h to the height of the window
    pixel_x = column * w/3 + w/6
    pixel_y = row * h/3 + h/6

    #Draw X
    #Point(pixel_x, pixel_y).draw(my_window) #Center Point!
    Line(Point(pixel_x, pixel_y), Point(pixel_x + 30, pixel_y + 30)).draw(my_window) #Down Right
    Line(Point(pixel_x, pixel_y), Point(pixel_x - 30, pixel_y + 30)).draw(my_window) #Down Left
    Line(Point(pixel_x, pixel_y), Point(pixel_x + 30, pixel_y - 30)).draw(my_window) #Up Right
    Line(Point(pixel_x, pixel_y), Point(pixel_x - 30, pixel_y - 30)).draw(my_window) #Up Left

def Draw_O(row, column, my_window):
    w = my_window.getWidth() #Set's w to the width of the window
    h = my_window.getHeight() #Set's h to the height of the window
    pixel_x = column * w/3 + w/6
    pixel_y = row * h/3 + h/6

    #Draw O
    #Point(pixel_x, pixel_y).draw(my_window) #Center Point!
    Circle(Point(pixel_x, pixel_y), 30).draw(my_window)
    
    

def Main():
    mode = "X"
    while(True):
        my_window = GraphWin(window_title, window_width, window_height)
        w = my_window.getWidth() #Set's w to the width of the window
        h = my_window.getHeight() #Set's h to the height of the window
        Draw_Grid(my_window)
        for number in range(0,9): #Because there are 9 moves in tic tac toe.
            mouse_input = my_window.getMouse()
            if(mouse_input.getY() >= (2*h)/3):
                row = 2
            elif(mouse_input.getY() >= h/3):
                row = 1
            else:
                row = 0

            if(mouse_input.getX() >= (2*w)/3):
                column = 2
            elif(mouse_input.getX() >= w/3):
                column = 1
            else:
                column = 0

            
            if(mode == "X"):
                Draw_X(row, column, my_window)
                mode = "O"
            else:
                Draw_O(row, column, my_window)
                mode = "X"
            my_window.getMouse()
            

#Testing
#my_window = GraphWin(window_title, window_width, window_height)
#Draw_Grid(my_window)
#Draw_X(1,1, my_window)
#Draw_O(0,0, my_window)

Main() 
