import random
while(1):
    a=random.randrange(0,100)
    b=random.choice(range(30,90,1))
    print("The Humidity recorded is %d Percentage" %b)
    print("The Temperature recorded is %d degree Celsius" %a)
    if b>30:
        if b<60:
            print("Normal humidity")
        else:
            print("High humidity")
            
    else:
        print("Low humidity")
    if a>57:
        print("Temperature is high")
        print("Trigger the alarm")
    else:
        print("Temperature is normal")
    print("============================================================")    
    exit()
        
