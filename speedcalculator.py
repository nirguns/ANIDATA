from time import * #imports time
import random as r #imports random which works as r

def mistake(paratest,usertest): #function which check mistakes
   error = 0
   #compares beteween users input and paragraph and shows either mistake or not
   for i in range(len(paratest)):
       try:
           if paratest[i] != usertest[i]:
               error =error+1
       except:
           error =error+1
   return error

#function for time
def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s #it gets time by subtracting start time and end time
    time_R = round(time_delay,2) #it roundsup time into 2 digit/second
    speed = len(userinput)/ time_R #it test the length of user'sinput
    return round(speed)
#looping to replay the programme   yes
while True:
    ck = input ("ready to test : yes / no: ")
    if ck == "yes":
        test = ["The quick brown fox jumps over the lazy dog",
        "my name is nirgun sachidananda subedi",
        "nirgunsubedi343@gmail.com"
        "anihortes"]
        test1 = r.choice(test) #ransomies beteween three in dictionary
        print("*****TYPING SPEED CALCULATOR*****")
        print (test1) #print the text which is to be input by user
        print() #these 2 prints the blank spaces
        print()
        time_1 = time() #it imports the time before start
        userinput = input("enter: ")
        time_2 = time() #it imports the time after input

        print('speed : ' , speed_time(time_1,time_2,userinput),"w/s") #print the speed
        print("error : " , mistake(test1,userinput)) #print the error
    elif ck == 'no':
        print ("thanks for visiting :)")
        break

    else:
        print("wrong input")
