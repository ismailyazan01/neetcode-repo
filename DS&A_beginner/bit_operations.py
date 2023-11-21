# Bitwise operations and bit counting example

# Bitwise AND operation
n = 1 & 1

# Bitwise OR operation
n = 1 | 0

# Bitwise XOR operation
n = 0 ^ 1

# Bitwise NOT operation
n = ~n

# Left shift operation
n = 1
n = n << 1

# Right shift operation
n = n >> 1


def countBits(n):
    """
    Count the number of set bits (1s) in the binary representation of an integer.

    Parameters:
    - n (int): The input integer.

    Returns:
    - int: The count of set bits in the binary representation of n.
    """
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1
    return count


# Example Usage:

# Count the number of set bits in the binary representation of 15
result_count_bits = countBits(15)
print(f"Number of Set Bits in 15: {result_count_bits}")

# Count the number of set bits in the binary representation of 7
result_count_bits_7 = countBits(7)
print(f"Number of Set Bits in 7: {result_count_bits_7}")
