'''
m=30
print(m)

def calculate_sum(a, b):
    global m
    m = 10
    return a + b
    
# Usage
result = calculate_sum(5, 3 )
print(result) 
print(m)
'''

def check_number(num):
    return check_number(num)
    if num > 0:
        print("Positive")
    else:
        print( "Negative")
        
    #print("Zero")

print(check_number(5))

# Output: Positive



  






