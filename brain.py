import math
import random

def neuron(inputs, weights, bias):
    total = bias
    for i in range(len(inputs)):
        total += inputs[i] * weights[i]
    return math.tanh(total)

def layer(inputs, weights, biases):
    outputs = []
    for n in range(len(biases)):
        outputs.append(neuron(inputs, weights[n], biases[n]))
    return outputs

def forward(inputs, network):
    values = inputs
    for weights, biases in network:
        values = layer(values, weights, biases)
    return values

def create_network(sizes):
    network = []
    for i in range(len(sizes) - 1):
        n_in = sizes[i]
        n_out = sizes[i + 1]
        weights = []
        for _ in range(n_out):
            row = []
            for _ in range(n_in):
                row.append(random.uniform(-1, 1))
            weights.append(row)
        biases = []
        for _ in range(n_out):
            biases.append(random.uniform(-1, 1))
        network.append((weights, biases))
    return network

net = create_network([7, 15, 15, 4])
print(len(net), len(net[0][0]), len(net[0][0][0]))
print(forward([1, 0.5, 0.2, 1, 0.3, 0.8, 1], net))