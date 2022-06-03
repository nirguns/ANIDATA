email = input ("enter your email: ")
k=0
j=0
d=0
if len(email)>=8:
    if email[0].isalpha:
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i ==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("not valid!spaces/uppercase in email")
                else:
                    print("right email")        
            else:
                print ("not valid! dot is missing or in wrong position")
        else:
            print("not valid! @ is not pressent")
        
    else:
        print("not valid!alphabhets are not in email")
else:
    print("not valid due to the length ")