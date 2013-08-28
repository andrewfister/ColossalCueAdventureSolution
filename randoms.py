random = 6
randoms = [random]
for n in range(10):
    random = ((69069 * random + 1) % pow(2,32))
    randoms.append(random % 36)

print randoms
