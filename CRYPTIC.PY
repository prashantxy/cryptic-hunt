# List of encoded numbers
encoded_numbers = [
    150, 164, 164, 160, 163, 72, 57, 57, 141, 162, 143, 150, 151,
    166, 145, 56, 151, 143, 163, 56, 165, 143, 151, 56, 145, 144,
    165, 57, 155, 154, 57, 155, 141, 143, 150, 151, 156, 145, 55,
    154, 145, 141, 162, 156, 151, 156, 147, 55, 144, 141, 164, 141,
    142, 141, 163, 145, 163, 57, 150, 157, 165, 163, 151, 156, 147,
    57, 150, 157, 165, 163, 151, 156, 147, 56, 144, 141, 164, 141
]

# Convert each number to its ASCII character if within printable ASCII range
decoded_message = ''.join(chr(num) if 32 <= num <= 126 else '?' for num in encoded_numbers)

print(decoded_message)