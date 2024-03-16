import numpy as np

#------------------------------------------------------------------------------------------------
print("\nTask Five:\n")

ArrayOneForTaskFive=np.array([[1,5],[9,10],[2,19]])
ArrayTwoForTaskFive=np.array([3,2,91,13,23,1])


print(f"mean:\n{np.mean(ArrayOneForTaskFive)}\n")
print(f"median:\n{np.median(ArrayOneForTaskFive)}\n")
print(f"variance:\n{np.var(ArrayOneForTaskFive)}\n")
print(f"Standard deviation:\n{np.std(ArrayOneForTaskFive)}\n")
print(f"Correlation:\n{np.correlate(ArrayOneForTaskFive.reshape(-1),ArrayTwoForTaskFive)}\n")
