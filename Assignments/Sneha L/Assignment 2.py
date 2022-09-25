import random
while(1):
    Temp = random.randrange(0,100)
    Humid = random.randrange(0,100,10)
    print("sensed Temperature: %d degree Celsius "% Temp)
    print("sensed Humidity: %d Percentage" % Humid)
    if Temp>=60:
        print("Wake up the alarm...danger!")
    else:
        print("Temperature is normal")    
    if Humid<30:
        print("Low Humid")
    elif Humid>30:
        if Humid<=50:
            print("Humid is normal")
        else :
            print("Humid is high")
    else:
        exit()
