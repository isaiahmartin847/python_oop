def bit_counter(n):
    bits = 0
    for char in str(n):
        if char == "1":
                bits = bits + 1
    return bits

        
y = 110
print(bit_counter(y))