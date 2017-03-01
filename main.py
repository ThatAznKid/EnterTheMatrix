from display import *
from draw import *

screen = new_screen()

print "new matrix"
a = new_matrix()
print_matrix(a)

print "matrix after ident\n"
ident (a) 
print_matrix(a)

print "matrix a\n"
a = [[2,2,2,2],[2,2,2,2]]
print_matrix(a)

print "matrix a after scalar mult\n"
scalar_mult(a,2)
print_matrix(a)

print "matrix b"
b =[[1,2],[3,4],[5,6]]

print "matrix c, matrix mult of a and b"
c = matrix_mult(a,b) 
print_matrix(c)

print "matrix a again"
a = [[2,2,2,2],[2,2,2,2]]
print_matrix(a)

print "adding a point to a"
add_point(a,1,1) 
print_matrix(a)

print "adding an edge to a"
add_edge(a,1,1,1,2,2,2)
print_matrix(a)

color = [ 0, 255, 0 ]
matrix = new_matrix()

for a in range(125):  
    add_edge(matrix,a*1,a*2,0,a*3,a*4,0)
    
draw_lines( matrix, screen, color )
display(screen)
