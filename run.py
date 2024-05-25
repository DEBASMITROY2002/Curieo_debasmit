from log_management_utils import *
import sys

if __name__ == "__main__":
    log_manager = LogManager()

    # Read input from input.txt from arguments

    input_file = "input.txt"
    args = sys.argv
    if len(args) > 1:
        input_file = args[1]

    outputs = []
    with open(input_file, "r") as f:
        for line in f:
            output = log_manager.query(line.strip())
            outputs.append(output)

    # Output to output.txt
    with open("output.txt", "w") as f:
        for output in outputs:
            f.write(output + "\n")