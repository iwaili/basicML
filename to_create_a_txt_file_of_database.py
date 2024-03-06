#block 1
import tensorflow as tf
from tensorflow.keras.datasets import mnist
# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Display every matrix value of the first image
with open('example.txt', 'w') as f:
    for ij in range(60000):
        for i in range(x_train[ij].shape[0]):
            temp = ""
            for j in range(x_train[ij].shape[1]):
                temp += "1" if x_train[ij][i][j]>0 else "0"
            f.write(temp.strip() + "\n")  # Remove trailing space and move to the next line after printing each row
        f.write(str(y_train[ij])+"\n")

#block 2
# Open the example.txt file in read mode
with open('example.txt', 'r') as f:
    # Read and print each line of the file
    for line in f:
        print(line.strip())  # Remove newline characters and print each line

#block 3
from google.colab import files
# Download example.txt from Google Colab
files.download('example.txt')
