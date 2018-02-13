list = [1,2,3,4,5,6,7,8,9]
print ("choose num")
print(list)
sum1=0
sum2=0
counter=0
counter2=0
while (counter !=3) :
    counter2=0
    p1=int(input("play_1 : choose number from this list :"))
    for i in range (0,len(list)):
        if p1 != list[i] :
            counter2 = counter2 + 1
    if counter2 == len(list) :
        print ("this number is maybe taken or not in the list please inter another number")
        counter2 = 0
    
    else :
        sum1=sum1 + p1
        if sum1 == 15 :
            print ("player_1 wiiiiiiinz")
            break
        else :
            list.remove(p1)
            print ("choose num")
            print (list)
            while (counter !=3) :
                counter2=0
                p2=int(input("play_2 : choose number from this list :"))
                for i in range (0,len(list)):
                    if p2 != list[i] :
                        counter2 = counter2 + 1
                if counter2 == len(list) :
                    print ("this number is maybe taken or not in the list please inter another number")
                    counter2=0
                else :
                    sum2=sum2+p2
                    if sum2 == 15 :
                        print ("player_2 wiiiiiiinz")
                        counter=3
                        break
                    else :
                        if counter==2 :
                            print ("draw -__- !!")
                            counter=3
                            break
                        else :
                            list.remove (p2)
                            print ("choose number")
                            print (list)
                            counter=counter+1
                            break
                            
