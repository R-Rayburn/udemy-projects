from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f'{self.name}, '\
            f'{len(self.inputs)} inputs, '\
            f'{len(self.outputs)} outputs.'

    # Turn scalar in collection of 1 element
    def __iter__(self):
        yield self

    # def connect_to(self, other):
        # two way connection between neurons
        # self.outputs.append(other)
        # other.inputs.append(self)

class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f'{name}-{x}'))

    def __str__(self):
        return f'{self.name} with {len(self)} neurons'

# deprecated
def connect_to(self, other):
    if self == other:
        return
    for s in self:
        for o in other:
            s.outputs.append(o)
            o.inputs.append(s)


if __name__ == '__main__':
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    layer1 = NeuronLayer('L1', 3)
    layer2 = NeuronLayer('L2', 4)

    # deprecated
    # Neuron.connect_to = connect_to
    # NeuronLayer.connect_to = connect_to

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)