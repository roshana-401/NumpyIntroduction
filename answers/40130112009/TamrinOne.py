import numpy as np

#------------------------------------------------------------------------------------------------
#Test One
print("\nTask One:")
Array_one=np.array([1,2,3,4,5,6,7],ndmin=1)
print(f"\n{Array_one}\n")
print(f"Array_one Of dimensions:{Array_one.ndim}\n")
print(f"Array_one Of Size:{Array_one.size}\n")
print(f"Array_one Of Size:{Array_one.dtype}\n")
print(f"Array_one Sum:{Array_one.sum()}")

Array_Two=np.zeros((3,4))
print(f"\n{Array_Two}\n")
print(f"Array_Two Of dimensions:{Array_Two.ndim}\n")
print(f"Array_Two Of Size:{Array_Two.size}\n")
print(f"Array_Two Of Size:{Array_Two.dtype}\n")
print(f"Array_Two Sum:{Array_Two.sum()}")

Array_Three=np.ones((2,3,4))
print(f"\n{Array_Three}\n")
print(f"Array_Three Of dimensions:{Array_Three.ndim}\n")
print(f"Array_Three Of Size:{Array_Three.size}\n")
print(f"Array_Three Of Size:{Array_Three.dtype}\n")
print(f"Array_Three Sum:{Array_Three.sum()}\n")