import uuid
import random
import string

# Function to generate random text
def generate_random_text(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Number of UUID-random text pairs to generate
num_pairs = 10000000

# Generate UUID-random text pairs
uuid_text_pairs = [(str(uuid.uuid4()), generate_random_text(10)) for _ in range(num_pairs)]

# Write pairs to a file
output_file = "uuid_randomtext_pairs.txt"
with open(output_file, "w") as f:
    for uuid_text_pair in uuid_text_pairs:
        f.write(f"{uuid_text_pair[0]} {uuid_text_pair[1]}\n")