import numpy as np




#------------------------------------------------------------------------------------------------        
print("\nTask Three:\n")

ArrayOneForCalc=np.array([32,4,1,3,6,21])
ArrayTwoForCalc=np.array([4,2,6,4,2,4])
ArrayThreeForCalc=np.array([[5,1],[4,6],[99,42]])
ArrayFourForCalc=np.array([1,2,3])


print(f"Addition:{np.add(ArrayOneForCalc,ArrayTwoForCalc)}\n")
print(f"Subtraction:{np.subtract(ArrayOneForCalc,ArrayTwoForCalc)}\n")
print(f"Multiplication:{np.multiply(ArrayOneForCalc,ArrayTwoForCalc)}\n")
print(f"Division:{np.divide(ArrayOneForCalc,ArrayTwoForCalc)}\n")

print(f"Broadcasting:\n{ArrayThreeForCalc+ArrayFourForCalc[:,np.newaxis]}\n")
print(f"Reshaping:\n{ArrayThreeForCalc.reshape(2,-1)}\n")
print(f"Flattening:\n{ArrayThreeForCalc.reshape(-1)}\n")