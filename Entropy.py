# code the equation for entropy:

# In[ ]:

from math import log2


def entropy(probs):
    return -sum(prob * log2(prob) for prob in probs.values())


probs = {'a': 0.25, 'b': 0.25, 'c': 0.2, 'd': 0.15, 'e': 0.15}
print(entropy(probs))


# code the equation for conditional entropy:

# In[ ]:

def conditional_entropy(probs):
    return -sum(prob * log2(prob) for prob in probs.values())


probs = {'a': 0.25, 'b': 0.25, 'c': 0.2, 'd': 0.15, 'e': 0.15}
print(conditional_entropy(probs))


# code the equation for joint entropy:

# In[ ]:

def joint_entropy(probs):
    return -sum(prob * log2(prob) for prob in probs.values())


prob = {'a': 0.25, 'b': 0.25, 'c': 0.2, 'd': 0.15, 'e': 0.15}
print(joint_entropy(prob))
