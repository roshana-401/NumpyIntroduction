import numpy as np



#------------------------------------------------------------------------------------------------
print("\nTask Two:\n")

ArrayOneForTaskTwo=np.array([1,5,8,2,4,89])
ArrayTwoForTaskTwo=np.array([[1,5,8,2],[3,1,6,12],[99,3,42,31]])
ArrayThreeForTaskTwo=np.array([[[1,5],[8,2]],[[3,1],[6,12]],[[99,3],[42,31]]])

print(f"third element of the one-dimensional array:{ArrayOneForTaskTwo[3]}\n")
print(f"([2,3]) element of the two-dimensional array:{ArrayTwoForTaskTwo[2][3]}\n")
print(f"Slicing:\n{ArrayOneForTaskTwo.reshape(2,-1)[:2,:2]}")
print(f"\nIterating:")
for i in ArrayThreeForTaskTwo:
    for j in i:
        print(j)