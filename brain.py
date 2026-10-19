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

def crossover(a, b):
    child = []
    for (weights_a, biases_a), (weights_b, biases_b) in zip(a, b):
        weights = []
        for row_a, row_b in zip(weights_a, weights_b):
            row = []
            for x, y in zip(row_a, row_b):
                row.append(x if random.random() < 0.5 else y)
            weights.append(row)
        biases = []
        for x, y in zip(biases_a, biases_b):
            biases.append(x if random.random() < 0.5 else y)
        child.append((weights, biases))
    return child

def mutate(network, rate=0.05, strength=0.3):
    for weights, biases in network:
        for row in weights:
            for i in range(len(row)):
                if random.random() < rate:
                    row[i] += random.gauss(0, strength)
        for i in range(len(biases)):
            if random.random() < rate:
                biases[i] += random.gauss(0, strength)