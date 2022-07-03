from math import e


class Input_Neuron:
    def __init__(self):
        self.value = None
    def propagate(self, input_value):
        self.value = input_value

class Sigmoid_Neuron:
    # weighted sum of inputs, then apply sigmoid squashing function
    def __init__(self, input_layer, input_weights):
        self.input_layer = input_layer
        self.input_weights = input_weights
        self.value = None
    def propagate(self):
        weighted_inputs = []
        for n in len(self.input_layer):
            weighted_inputs.append((self.input_layer[n].value * self.input_weights[n]))
        self.value = 1 / (1 + pow(e, -sum(weighted_inputs)))

class ReLU_Neuron:
    # rectified linear unit
    def __init__(self, input_layer, input_weights):
        self.input_layer = input_layer
        self.input_weights = input_weights
        self.value = None
    def propagate(self):
        weighted_inputs = []
        for n in len(self.input_layer):
            weighted_inputs.append((self.input_layer[n].value * self.input_weights[n]))
        if sum(weighted_inputs) > 0:
            self.value = sum(weighted_inputs)
        else:
            self.value = 0

class Output_Neuron:
    def __init__(self, input_layer, input_weights, label):
        self.input_layer = input_layer
        self.input_weights = input_weights
        self.value = None
        self.label = label
    def propagate(self):
        weighted_inputs = []
        for n in len(self.input_layer):
            weighted_inputs.append((self.input_layer[n].value * self.input_weights[n]))
        self.value = sum(weighted_inputs)
    def output(self):
        print(f"{self.label}: {self.value}")

class Input_Layer:
    def __init__(self, neurons):
        self.neurons = neurons
    def propagate(self, input_values):
        for x in len(self.neurons):
            self.neurons[x].propagate(input_values[x])

class Interior_Layer:
    def __init__(self, neurons):
        self.neurons = neurons
    def propagate(self):
        for neuron in self.neurons:
            neuron.propagate()

class Output_Layer:
    def __init__(self, neurons):
        self.neurons = neurons
    def propagate(self):
        for neuron in self.neurons:
            neuron.propagate()
    def print_output(self):
        print("OUTPUT:")
        for neuron in self.neurons:
            neuron.output()
    def get_output(self):
        labels = []
        for neuron in self.neurons:
            if neuron.value > 0:
                labels.append(neuron.label)
        if len(labels) == 1:
            labels = labels[0]
        return labels

class NeuralNetwork:
    def __init__(self):
        self.input_layer = None
        self.layers = []
        self.output_layer = None
    def def_input(self, num:int):
        neurons = []
        for i in range(num):
            neurons.append(Input_Neuron())
        self.input_layer = Input_Layer(neurons)
    def add_layer(self, num:int, type:str, weights_matrix):
        # possible types: sigmoid, relu
        if type != "sigmoid" or type != "relu":
            print("Invalid type selected for layer.")
            exit()
        neurons = []
        if len(self.layers) > 0:
            input_neurons = self.input_layer.neurons
        else:
            input_neurons = self.layers[-1].neurons
        for i in range(num):
            if type == "sigmoid":
                neurons.append(Sigmoid_Neuron(input_neurons, weights_matrix[i]))
            elif type == "relu":
                neurons.append(ReLU_Neuron(input_neurons, weights_matrix[i]))
        self.layers.append(Interior_Layer(neurons))
    def def_output(self, num:int, weights_matrix, labels):
        neurons = []
        for i in range(num):
            neurons.append(Output_Neuron(self.layers[-1].neurons, weights_matrix[i], labels[i]))
        self.output_layer = Output_Layer(neurons)
    def propagate(self, inputs):
        self.input_layer.propagate(inputs)
        for layer in self.layers:
            layer.propagate
        self.output_layer.propagate()
    def print_output(self):
        self.output_layer.print_output()
    def get_output(self):
        self.output_layer.get_output()