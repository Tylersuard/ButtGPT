import time
import random

print("""██████╗ ██╗   ██╗████████╗████████╗     ██████╗ ██████╗ ████████╗
██╔══██╗██║   ██║╚══██╔══╝╚══██╔══╝    ██╔════╝ ██╔══██╗╚══██╔══╝
██████╔╝██║   ██║   ██║      ██║       ██║  ███╗██████╔╝   ██║   
██╔══██╗██║   ██║   ██║      ██║       ██║   ██║██╔═══╝    ██║   
██████╔╝╚██████╔╝   ██║      ██║       ╚██████╔╝██║        ██║   
╚═════╝  ╚═════╝    ╚═╝      ╚═╝        ╚═════╝ ╚═╝        ╚═╝   
""")

sentence = "Butt "

_ = input("Welcome to ButtGPT!  Please enter your query: ")

for i in range(random.randint(50,75)):
    sentence+="butt "
    
sentence += "butt."


def print_streaming(sentence, delay=0.01):
    for word in sentence.split():
        print(word, end=' ', flush=True)
        time.sleep(delay)
    print()

# Usage
print_streaming(sentence, delay=0.5)
