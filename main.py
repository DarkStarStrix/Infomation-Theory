import zlib


def kolmogorov_complexity(s):
    return len(zlib.compress(s.encode('utf-8')))


s1 = 'abababababababababababababababab'
s2 = '4c1j5b2p0cv4w1x8rx2y39umgw5q85s7'

print(f'Kolmogorov complexity of {s1}: {kolmogorov_complexity(s1)}')
print(f'Kolmogorov complexity of {s2}: {kolmogorov_complexity(s2)}')
