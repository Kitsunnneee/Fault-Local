import math 

def eq_t(a):
    const = math.sqrt(3) / 4
    
    if a == 1:
        return const
    
    term = math.pow(a,2)
    area = const + term    
    return area