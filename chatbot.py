print("welcome")

print("do you want to know about bhawna and shital")

x=input("enter your answer in yes or no: ")

if x=="yes":
    print("nice")
    name=input("enter name (bhawna/shital): ")
    if name=="bhawna" or name=="shital":
        print("deatils of",name)
        favourite_movie=input(name+"'s favourite movie do you want to know? ")
        if favourite_movie=="yes":
            if name=="bhawna":
                print("ghajini is bhawna's favourite movie")
            elif name=="shital":
                print("shersha is shital's favourite movie")
            favourite_colour=input(name+"'s favourite colour do you want to know? ")
            if favourite_colour=="yes":
                if name=="bhawna":
                    print("bhawna's favourite colour is black")
                elif name=="shital":
                    print("shital's favourite colour is black and blue")
                hobbise=input(name+"'s hobbise do you want to no? ")
                if hobbise=="yes":
                    if name=="bhawna":
                        print("writing , photography and dancing")
                    elif name=="shital":
                        print("Travelling and Trekking")
                    weight=input("whose weight you want to know? ")
                    if weight=="yes":
                        if name=="bhawna":
                            print("bhawna's weight is 44 kg")
                        elif name=="shital":
                            print("shital's weight is 43kg")
                    elif weight=="no":
                        print("ok")
                    else:
                        print("don't understand")
                elif hobbise=="no":
                    print("ok")
                else:
                    print("don't understand")
            elif favourite_movie=="no":
                print("ok")
            else:
                print("don't understand")
        elif favourite_movie=="no":
            print("ok")
        else:
            print("don't understand")
    else:
        print("don't understand")
elif x=="no":
    print("ok")
else:
    print("don't understand")