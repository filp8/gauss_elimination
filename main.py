from gauss import det

# classica matrice quadrata
square_matrix = [[1,3,1,-1],[3,9,4,1],[2,1,5,2],[0,1,-1,-1]]

d = det(square_matrix)
print(f"det: {d}\nMatrix: {square_matrix}")