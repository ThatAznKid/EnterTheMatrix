from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

for a in range(125):  
    add_edge(matrix,a*1,a*2,0,a*3,a*4,0)
    
draw_lines( matrix, screen, color )
display(screen)
