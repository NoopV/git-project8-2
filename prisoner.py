import random

def prisoner_problem(num_prisoners):
    keys = {i: None for i in range(1, num_prisoners + 1)}
    
    for prisoner in range(1, num_prisoners + 1):
        current_room = random.randint(1, num_prisoners) 
        while keys[current_room] != prisoner:  
            keys[current_room] = prisoner  
            current_room = random.randint(1, num_prisoners) 

    for key, value in keys.items():
        if key != value:
            return False 
    return True

num_prisoners = 100
result = prisoner_problem(num_prisoners)
print("모든 수감자가 자신의 방으로 들어왔는가?", result)
