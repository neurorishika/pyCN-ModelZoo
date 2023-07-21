import torch
import torch.nn as nn

class FeedForwardNetwork(nn.Module):
    """
    Simple Feed-Forward Neural Network with arbitrary number of hidden layers
    """
    def __init__(self, n_input : int, hidden_layer_sizes : list, n_output: int, bias : bool = False):
        """
        Initialize the network
        :param n_input: number of input neurons
        :param hidden_layer_sizes: list of number of hidden neurons in each layer
        :param n_output: number of output neurons
        """
        super().__init__()
        self.bias = bias
        self.layers = nn.ModuleList([nn.Linear(n_input, hidden_layer_sizes[0], bias = bias)]) # first layer
        self.layers.extend([nn.Linear(h1, h2, bias = bias) for h1, h2 in zip(hidden_layer_sizes, hidden_layer_sizes[1:])]) # hidden layers
        self.layers.append(nn.Linear(hidden_layer_sizes[-1], n_output, bias = bias)) # output layer
    
    def forward(self, x):
        """
        Forward pass through the network
        :param x: network input
        """
        for layer in self.layers:
            x = torch.relu(layer(x)) # apply ReLU activation function
        return x
    
    def reset_parameters(self):
        """
        Reset the parameters of the network
        """
        for layer in self.layers: # reset all layers
            layer.reset_parameters()
    
    def hebbian_update(self,input,lr,max_weight=1,max_bias=1):
        """
        Perform forward Hebbian update of the network
        :param input: input to the network
        :param lr: learning rate
        """
        x = input
        for layer in self.layers:
            y = torch.relu(layer(x))
            if max_weight is not None:
                layer.weight.data += lr * torch.mm(y.t(), x) * (max_weight - torch.abs(layer.weight.data))
            else:
                layer.weight.data += lr * torch.mm(y.t(), x)
            if self.bias:
                if max_bias is not None:
                    layer.bias.data += lr * torch.sum(y, dim=0) * (max_bias - torch.abs(layer.bias.data))
                else:
                    layer.bias.data += lr * torch.sum(y, dim=0)
            x = y

    def get_weights_and_biases(self):
        """
        Get the weights and biases of the network
        """
        if self.bias:
            return [layer.weight.data.numpy() for layer in self.layers], [layer.bias.data.numpy() for layer in self.layers]
        else:
            return [layer.weight.data.numpy() for layer in self.layers]
    
    def set_weights_and_biases(self, weights, biases=None):
        """
        Set the weights and biases of the network
        :param weights: list of weights
        :param biases: list of biases
        """
        for layer, weight in zip(self.layers, weights):
            layer.weight.data = torch.from_numpy(weight)
        if self.bias:
            for layer, bias in zip(self.layers, biases):
                layer.bias.data = torch.from_numpy(bias)
    
    def arbitrary_update(self, input, synapse_updater):
        """
        Update the weights and biases of the network using an arbitrary update function
        :param input: input to the network
        :param synapse_update_function: function that updates the weights and biases of the network
        """
        x = input
        for layer in self.layers:
            y = torch.relu(layer(x))
            for i in range(y.shape[1]):
                for j in range(x.shape[1]):
                    if self.bias:
                        layer.weight[i,j] += synapse_updater(torch.cat([x[:,j], y[:,i], layer.weight[i,j].view(1), layer.bias[i]]))
                        layer.bias[i] += synapse_updater(torch.cat([x[:,j], y[:,i], layer.weight[i,j].view(1), layer.bias[i]]))
                    else:
                        layer.weight[i,j] += synapse_updater(torch.cat([x[:,j], y[:,i], layer.weight[i,j].view(1)]))
            x = y

class FeedForwardLearningRule(nn.Module):
    """
    A class that implements an arbitrary local memoryless learning rule
    """
    def __init__(self, hidden_layer_sizes : list, bias : bool = False):
        """
        Initialize the learning rule
        :param hidden_layer_sizes: list of number of hidden neurons in each layer
        :param bias: whether to use bias
        """
        super().__init__()
        self.bias = bias
        if bias:
            self.input_size = 4
            self.output_size = 2
        else:
            self.input_size = 3
            self.output_size = 1
        self.layers = nn.ModuleList([nn.Linear(self.input_size, hidden_layer_sizes[0], bias = bias)]) # first layer
        self.layers.extend([nn.Linear(h1, h2, bias = bias) for h1, h2 in zip(hidden_layer_sizes, hidden_layer_sizes[1:])]) # hidden layers
        self.layers.append(nn.Linear(hidden_layer_sizes[-1], self.output_size, bias = bias)) # output layer

    def forward(self, x):
        """
        Forward pass through the network
        :param x: network input
        """
        for layer in self.layers:
            x = torch.relu(layer(x))
        return x


            
        