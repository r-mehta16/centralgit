def is_prime_number(num):

    for i in range(2, num):
        if(num%i==0):
            return False

    return True


print("is 7 prime "  + str(is_prime_number(7)))
print("is 8 prime " + str(is_prime_number(8)))
