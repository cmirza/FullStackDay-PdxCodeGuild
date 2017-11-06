'''
Lab 28 - Socks
Mix of types and colors
'''

import random  # import random module

sock_types = ['ankle', 'crew', 'calf', 'thigh']  # list of possible socks

sock_colors = ['black', 'white', 'blue']  # list of possible colors

my_socks = {}  # dictionary of socks you have

sock_matches = {}  # dictionary of sock matches

sock_loners = {}  # dictionary of sock loners


# Run a loop 100 times for each sock, randomly picking a type and color of sock. Then iterate for that combo or add
# combo to dictionary
for socks in range(100):
    sock_type = ((random.choice(sock_colors)), (random.choice(sock_types)))
    if sock_type in my_socks:
        my_socks[sock_type] += 1
    else:
        my_socks[sock_type] = 1

# Run a loop over the dictionary of socks owned, do floor division on total to get sock matches and assign value in
# sock matches dictionary, then do modulus on total to get sock loners and assign value in sock loners dictionary
for socks in my_socks:
    sock_matches[socks] = my_socks[socks] // 2
    sock_loners[socks] = my_socks[socks] % 2

# print result for socks owned, sock matches and sock loners
print('Socks owned', my_socks)
print('Sock pairs', sock_matches)
print('Loner socks', sock_loners)
