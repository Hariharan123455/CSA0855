def sumsquare(l):
    odd_sum = 0
    even_sum = 0
    
    for number in l:
        if number % 2 == 0:  
            even_sum += number ** 2
        else:  
            odd_sum += number ** 2
            
    return [odd_sum, even_sum]

