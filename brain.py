import math

def neuron(inputs, weights, bias):
    total = bias
    for i in range(len(inputs)):
        total += inputs[i] * weights[i]
    return math.tanh(total)

print(neuron([1, 0.5], [0.5, -1], 0.1))