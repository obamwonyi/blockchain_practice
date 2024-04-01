import hashlib

# The Hash functions expect bytes as input: then encode() method turns
# strings to bytes
input_bytes = b"dan"
# bitcoin uses double(2) sha256
# ethereum uses keccak256
output = hashlib.sha3_256(input_bytes)
# this would print out the hexadecimal value of the digest
print(output.hexdigest())