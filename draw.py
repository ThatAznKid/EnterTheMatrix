from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    #plot(screen,color,x,y)
    for a in range (0,len(matrix),2):
        draw_line(matrix[a][0],matrix[a][1],matrix[a+1][0],matrix[a+1][1],screen,color) 
    

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    new_row = [] 
    new_row.append(x0) 
    new_row.append(y0) 
    new_row.append(z0)  
    new_row.append(1.0)
    matrix.append(new_row)
    new_row = [] 
    new_row.append(x1) 
    new_row.append(y1) 
    new_row.append(z1)   
    new_row.append(1.0)
    matrix.append(new_row)

def add_point( matrix, x, y, z=0 ):
    new_row = [] 
    new_row.append(x) 
    new_row.append(y) 
    new_row.append(z)  
    new_row.append(1.0)
    matrix.append(new_row)

def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line

#a = [[2,2,2],[2,2,2]]
#print_matrix(a)
#add_point(a,1,1) 
#print_matrix(a)
#add_edge(a,1,1,1,2,2,2)
#print_matrix(a)
