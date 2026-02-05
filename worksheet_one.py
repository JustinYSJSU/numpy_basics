"""
GOAL: Implement basic numpy operations

1.) Initialize 5x5 ndarray. Manually change a middle value to 0. ndarray will represent soil moisture data

2.) Calculate the average of the grid

3.) Find the "0" and replace it with the calculated average

4.) Flatten the 5x5 ndarray into a 1D array
"""
import numpy as np

# declare intiial 5x5
data = np.array(
    [[10, 50, 25, 16, 18],
    [15, 24, 47, 4, 5],
    [1, 17, 15, 42, 41],
    [5, 6, 2, 14, 17],
    [22, 48, 34, 20, 21]]
)
print(f"Initial data: {data}")
# manually change a middle value to 0
data[2][2] = 0
print(f"Data after changing value to 0: {data}")

# calculate the mean
average = np.mean(data)
print(f"Mean value: {average}")

zero = np.where(data == 0) # find location of the zero => (2,2)
print(zero)
data[zero] = average # set location of the zero to the calculated average
print(f"Data after replace 0 with average: {data}")

max = np.max(data) # find max value
print(f"Max value: {max}")

vectorized_data = data / max # vectorize by dividing by max value
print(f"Data after vectorization (divide by max): {vectorized_data}")
