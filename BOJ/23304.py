import math

def recursive(s):
    length = len(s)
    
    if length == 1:
        return True
    
    else:   
        next_length = math.floor(length / 2)
        head = s[:next_length]
        tail = s[-next_length:]
        
        if head == head[::-1] and tail == tail[::-1]:
            return recursive(head) and recursive(tail)
        else:
            return False

line = input().rstrip()
ret = recursive(line)

if ret:
    print("AKARAKA")
else:
    print("IPSELENTI")