'''
Lab 28 - Socks
'''

import random  # import random module

sock_types = ['ankle', 'crew', 'calf', 'thigh']  # list of possible socks

my_socks = {'ankle': 0, 'crew': 0, 'calf': 0, 'thigh': 0}  # dictionary of socks you have

sock_matches = {'ankle': 0, 'crew': 0, 'calf': 0, 'thigh': 0}  # dictionary of sock matches

sock_loners = {'ankle': 0, 'crew': 0, 'calf': 0, 'thigh': 0}  # dictionary of sock loners


# Run a loop 100 times for each sock, randomly picking a type of sock and iterating the total for that sock
for socks in range(100):
    sock = random.choice(sock_types)
    my_socks[sock] += 1

# Run a loop over the dictionary of socks owned, do floor division on total to get sock matches and assign value in
# sock matches dictionary, then do modulus on total to get sock loners and assign value in sock loners dictionary
for socks in my_socks:
    sock_matches[socks] = my_socks[socks] // 2
    sock_loners[socks] = my_socks[socks] % 2

# print result for socks owned, sock matches and sock loners
print(my_socks)
print(sock_matches)
print(sock_loners)
