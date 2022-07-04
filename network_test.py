from main import *

def create_nn():
    nn = NeuralNetwork()
    nn.def_input(4)
    nn.add_layer(4, "sigmoid", [
        [1,0,0,1],
        [0,1,1,0],
        [1,0,0,-1],
        [0,1,-1,0]
    ])
    nn.add_layer(4, "sigmoid", [
        [1,1,0,0],
        [-1,1,0,0],
        [0,0,1,-1],
        [0,0,1,1]
    ])
    nn.add_layer(8, "relu", [
        [1,0,0,0],
        [-1,0,0,0],
        [0,1,0,0],
        [0,-1,0,0],
        [0,0,1,0],
        [0,0,-1,0],
        [0,0,0,1],
        [0,0,0,-1]
    ])
    nn.def_output(4, [
        [1,1,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,1,1]
    ], [
        "solid", "vertical", "diagonal", "horizontal"
    ])
    return nn


### TESTS:

## test 1
print("Test 1")
input_matrix = [-1,-1,1,1] # black top row, white bottom row
nn = create_nn()
nn.propagate(input_matrix)
print(nn.out())

## test 2
print("\nTest 2")
nn = create_nn()
nn.propagate([-1,1,-1,1]) # black top left corner & bottom right corner diagonal, rest white
print(nn.out())

## test 3
print("\nTest 3")
nn = create_nn()
nn.propagate([1,1,1,1]) # solid white box
print(nn.out())

## test 4
print("\nTest 4")
nn = create_nn()
nn.propagate([-1,1,1,-1]) # black left col, white right col
print(nn.out())
