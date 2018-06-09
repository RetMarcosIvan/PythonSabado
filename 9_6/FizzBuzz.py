def FizzBuzz():
    
    for num in range(0,100):
        FB=""
        if(num%3==0):
            FB+="Fizz"
        if(num%5 == 0):
            FB+="Buzz"
        print str(num) + " - " + FB

print FizzBuzz()