import random
while(1):
    T = random.randrange(0,100)
    H = random.randrange(0,100,5)
    print("sensed Temperature: %d degree Celsius "% T)
    print("sensed Humidity: %d Percentage" % H)
    if T>=57:
        print("Alert alarm!!!!!")
    else:
        print("Temperature is normal")    
    if H<30:
        print("Low Humid")
    elif H>30:
        if H<=50:
            print("Humid is normal")
        else :
            print("Humid is high")
    else:
        exit()
