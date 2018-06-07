def fatorial( n ):
    fat = count = 1
    
    if ( n < 0 ):
        return 0
    
    if ( n == 0 ):
        return 1
    
    while ( count <= n ):
        fat = fat * count
        count += 1
        
    return fat
    