import numpy as np

# Define the weights of the connections
w1 = np.array([-1, 2, 3])
w2 = np.array([0, 1, 3])

# Define the bias terms
b1 = np.array([1, 2])
b2 = 7

# Define the input vector
x = np.array([1, 0, -1])

# Calculate the hidden layer output
z1 = np.dot(x, w1) + 1
Z2 = np.dot(x,w2) + 2
print(z1,Z2)
hi = np.array([z1,Z2])
w2 = np.array([4,2])

hii = np.dot(hi,w2) + 7 
print(hii)
print(hii)
# # Calculate the output layer output

# print("Output:", y)

# # Check if output is 11 or 4
# if np.isclose(y, 11):
#     print("Statement i is correct.")
# elif np.isclose(y, 4):
#     print("Statement iv is correct.")
# else:
#     print("Neither statement i nor iv is correct.")