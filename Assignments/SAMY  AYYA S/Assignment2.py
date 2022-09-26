import random
while(1):
    t=random.randrange(0,100)
    h=random.choice(range(30,90,1))
    print("The Humidity recorded is %d Percentage" %h)
    print("The Temperature recorded is %d degree Celsius" %t)
    if h>30:
        if h<60:
            print("Normal humidity")
        else:
            print("High humidity")
            
    else:
        print("Low humidity")
    if t>57:
        print("Temperature is high")
        print("Alarm is ON")
    else:
        print("Temperature is normal")
        print("Alarm is OFF")
    print("==============================================")    
    exit()
        
