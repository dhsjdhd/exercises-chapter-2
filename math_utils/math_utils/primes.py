def isprime(n):
    if n == 1:
        return False
    elif n ==2:
        return True
    else:
        a =2
        while a < n:
            if n%a==0:
                return False
                break
            a=a+1
        else:
            return True
            
