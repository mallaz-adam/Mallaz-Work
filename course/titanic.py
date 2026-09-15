#---- Titanic Exercise ----:
import numpy as np
#--- Data ---:
passengers = np.array([
   [1, 0, 3, 22],# id - survived - passenger class - age
   [2, 1, 1, 38],
   [3, 1, 3, 26],
   [4, 1, 1, 35],
   [5, 0, 3, 35],
   [6, 0, 3, 18],
   [7, 0, 1, 54],
   [8, 0, 3, 2],
   [9, 1, 3, 27],
  [10, 1, 2, 14],
  [11, 1, 3, 4],
  [12, 1, 1, 58],
  [13, 0, 3, 20],
  [14, 0, 3, 39],
  [15, 0, 3, 14],
  [16, 1, 2, 55],
  [17, 0, 3, 2],
  [18, 1, 2, 12],
  [19, 0, 3, 31],
  [20, 1, 3, 8],
  [21, 0, 2, 35],
  [22, 1, 2, 34],
  [23, 1, 3, 15],
  [24, 1, 1, 28],
  [25, 0, 3, 8],
  [26, 1, 3, 38],
  [27, 0, 3, 2],
  [28, 0, 1, 1],
  [29, 1, 3, 5],
  [30, 0, 3, 18],
  [31, 0, 1, 40],
  [32, 1, 1, 70],
  [33, 1, 3, 33],
  [34, 0, 2, 66],
  [35, 0, 1, 28],
  [36, 0, 1, 42],
  [37, 1, 3, 5],
  [38, 0, 3, 18],
  [39, 0, 3, 18],
  [40, 1, 3, 14],
  [41, 0, 3, 40],
  [42, 0, 2, 27],
  [43, 0, 3, 29],
  [44, 1, 2, 0],
  [45, 1, 3, 19],
  [46, 0, 3, 33],
  [47, 0, 3, 14],
  [48, 1, 3, 22],
  [49, 0, 3, 41],
  [50, 0, 3, 18]
])
print(f"---> Shape of the array : {passengers.shape} <---")
print(f"---> Average age in titanic : {passengers[: , 3].mean()} <---")
index_max_age = np.argmax(passengers[: , 3])
index_min_age = np.argmin(passengers[: , 3])
print(f"---> id of the maximum age : {passengers[index_max_age,0]} - id of the youngest : {passengers[index_min_age,0]} <---")
survivor = passengers[passengers[:,1] == 1]
percentage_survivor = (survivor.shape[0] / passengers.shape[0])*100
print(f"---> percentage survivor : {percentage_survivor} <---")
#---- Special question ----:
classes = {
    "1" : passengers[passengers[:,2] == 1],
    "2" : passengers[passengers[:,2] == 2],
    "3" : passengers[passengers[:,2] == 3]
}

for passenger_class ,value in classes.items():
    print(f"---> Class : {passenger_class} <---")
    survivor = value[value[:,1] == 1]
    pourcentage = (survivor.shape[0] / value.shape[0]) * 100
    print(f"---> Pourcentage of survivor in that class : {pourcentage} <---")
    print("-"*20)