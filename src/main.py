# Resolve the problem!!
import re


def run():
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        message = f.read()
    
    pattern = re.compile('[a-z]')
    decryp_message = re.findall(pattern, message)
    
    solution = ''.join(decryp_message)
    print(solution)
 

if __name__ == '__main__':
    run()
