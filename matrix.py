import math


def print_matrix( matrix ):
    string = ""
    for a in range(len(matrix)): 
        string += "| "
        for b in range(len(matrix[a])): 
            string += str(matrix[a][b])
            string += " "
        string += "|\n"
    print string
    

def ident( matrix ): 
    for a in range(len(matrix)): 
        for b in range(len(matrix[a])): 
            if (a == b): 
                matrix[a][b] = 1 


def scalar_mult( matrix, s ):
    for a in range(len(matrix)): 
        for b in range(len(matrix[a])):
            matrix[a][b] *= s 
         
#m1 * m2 -> m2
def matrix_mult( m1, m2 ): 
    new = [] 
    for a in range (len(m1)): 
        new_row = [] 
        for b in range (len(m2[0])): 
            total = 0 
            for c in range (len(m2)): 
                total += m1[a][c] * m2 [c][b] 
            new_row.append(total)
        new.append(new_row) 
    return new 

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

#a = [[2,2,2],[2,2,2]]
#print_matrix(a) 
#ident (a) 
#print_matrix(a)
#scalar_mult(a,2)
#print_matrix(a)

#b =[[1,2],[3,4],[5,6]]
#c = matrix_mult(a,b) 
#print_matrix(c)
