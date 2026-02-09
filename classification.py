"""
GOAL: Given actual label vector and predicted label vector, determine the accurary of the predictions
"""
import numpy as np

y_actual = np.array([1, 1, 0, 1, 0, 0, 1, 0, 0, 1])
y_predicted = np.array([1, 0, 0, 1, 0, 0, 1, 1, 0, 1])

# using '==' will return a boolean array, where each true/false corresponds to the matching of that index for both vectors

result_vector = y_actual == y_predicted

# because true = 1 and false = 0, use sum() function to count number of matches from the result vector

print(f"Accurary: {np.sum(result_vector) / result_vector.size}")