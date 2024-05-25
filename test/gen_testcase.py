import random
import string

def generate_timestamp(prev_timestamp):
    return random.randint(prev_timestamp + 1, prev_timestamp + 1000)  # Generate random timestamps greater than the previous one

def generate_log_type():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1, 100)))  # Generate random log types

def generate_input(num_samples, output_file):
    inputs = []
    prev_timestamp = 0  # Initialize previous timestamp
    for _ in range(num_samples):
        timestamp1 = generate_timestamp(prev_timestamp)
        timestamp2 = generate_timestamp(timestamp1)
        log_type1 = generate_log_type()
        log_type2 = generate_log_type()
        
        inputs.append(f"{timestamp1};{log_type1};{random.uniform(1, 100):.2f}")
        inputs.append(f"{timestamp2};{log_type2};{random.uniform(1, 100):.2f}")
        inputs.append(log_type1)
        inputs.append(f"{timestamp2};{generate_log_type()};{random.uniform(1, 100):.2f}")
        inputs.append(f"{timestamp2+1};{log_type1};{random.uniform(1, 100):.2f}")
        inputs.append(f"BEFORE {timestamp1}")
        inputs.append(f"AFTER {timestamp2}")
        inputs.append(log_type2)
        inputs.append(f"BEFORE {log_type1} {timestamp1}")
        inputs.append(f"AFTER {log_type1} {timestamp2}")
        
        prev_timestamp = max(prev_timestamp, timestamp2)  # Update previous timestamp
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(inputs))

# Generate 5 test cases and dump into a file
generate_input(5, 'test_cases.txt')