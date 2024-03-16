import numpy as np


#------------------------------------------------------------------------------------------------
print("\nTask Four:\n")

ArrayOneForTaskFour=np.array([[8,7],[2,1],[3,9]])
ArrayTwoForTaskFour=np.array([1,32,21])
ArrayThreeForTaskFour=np.array([[50,29],[30,44]])

print(f"Matrix Multiplication:\n{np.dot(ArrayTwoForTaskFour,ArrayOneForTaskFour)}\n")
print(f"Determinant :\n{np.linalg.det(ArrayThreeForTaskFour)}\n")
print(f"Inverse:\n{np.linalg.inv(ArrayThreeForTaskFour)}\n")

resultOne,resultTwo=np.linalg.eig(ArrayThreeForTaskFour)
print(f"Eigenvalues :\n{resultOne}\n")
print(f"Eigenvectors:\n{resultTwo}\n")