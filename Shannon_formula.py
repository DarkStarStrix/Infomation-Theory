from math import ceil, log2


def shannon_fano(probs):
    sorted_probs = sorted(probs.items(), key=lambda x: x[1], reverse=True)
    cum_prob = 0
    code = {}
    for symbol, prob in sorted_probs:
        code_length = ceil(-log2(prob))
        code[symbol] = bin(int(cum_prob * 2 ** code_length))[2:].zfill(code_length)
        cum_prob += prob
    return code


probs = {'a': 0.25, 'b': 0.25, 'c': 0.2, 'd': 0.15, 'e': 0.15}
code = shannon_fano(probs)
print(code)
