import os
import time

def Formatter() -> None:
    success = 0
    failure = 0
    
    with open("tokens.txt", "r") as input_file, open("formatted_tokens.txt", "w") as output_file:
        for line in input_file:
            line = line.strip()
            
            if ":" in line:
                token_parts = line.split(":")
                new_token = token_parts[-1] + "\n"
                output_file.write(new_token)
                success += 1
                print(f"formatted {line[:25]}")
                time.sleep(0.0001)

            else:
                output_file.write(line + "\n")
                failure += 1
                print("failed  formatting")
                time.sleep(0.0001)

    print(f"succes: {succes} tokens")
    print(f"failure: {failure}  tokens")

if __name__ == "__main__":
    Formatter()
