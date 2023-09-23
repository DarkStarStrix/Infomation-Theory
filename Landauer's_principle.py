# Calculate the landauer's principle for a given circuit

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


# Define the function to calculate the landauer's principle
class Landauer:
    def __init__(self, circuit, T, V, R):
        self.Q = None
        self.circuit = circuit
        self.T = T
        self.V = V
        self.R = R

    def calc(self):
        # Calculate the landauer's principle
        self.Q = self.circuit * self.T * self.V * self.V * self.R
        return self.Q

    def plot(self):
        # Plot the landauer's principle
        plt.plot(self.T, self.Q, 'r-')
        plt.xlabel('Temperature (K)')
        plt.ylabel('Landauer\'s principle (J)')
        plt.title('Landauer\'s principle')
        plt.show()


# find the minimum value of the landauer's principle
def find_min(Q, T):
    min_Q = min(Q)
    min_T = T[Q.index(min_Q)]
    return min_Q, min_T


# find the landauer's principle for a given temperature of a circuit
def find_Q(T, circuit, V, R):
    Q = []
    for i in range(len(T)):
        Q.append(circuit * T[i] * V * V * R)
    return Q


# plot the temperature of that minimum landauer's principle make it interactive
def plot_min(T, Q, min_T, min_Q):
    plt.plot(T, Q, 'r-')
    plt.plot(min_T, min_Q, 'bo')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Landauer\'s principle (J)')
    plt.title('Landauer\'s principle')
    plt.show()


# main function
def main():
    # Define the circuit
    circuit = 1
    # Define the temperature
    T = [i for i in range(1, 1000)]
    # Define the voltage
    V = 1
    # Define the resistance
    R = 1
    # Calculate the landauer's principle
    landauer = Landauer(circuit, T, V, R)
    Q = landauer.calc()
    # Plot the landauer's principle
    landauer.plot()
    # Find the minimum value of the landauer's principle
    min_Q, min_T = find_min(Q, T)
    # Find the landauer's principle for a given temperature of a circuit
    Q = find_Q(T, circuit, V, R)
    # Plot the temperature of that minimum landauer's principle
    plot_min(T, Q, min_T, min_Q)


if __name__ == '__main__':
    main()
