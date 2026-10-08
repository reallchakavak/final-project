


list_nomarat=[]
while True:
    menu_nomarat=input("1.sabte nomre  2.namayesh nomarat  3.hazfe nomre   4.miyangin nomarat va grade   5.exit:")
    while True:
        match menu_nomarat:
            case"1":
                nomre_doros=float(input("nomre ra vared konid : "))
                if 0 > nomre_doros  or nomre_doros> 20 :
                    print(" nomarat ra sahih vared konid !!!")
                    break
                else :
               
                    list_nomarat.append(nomre_doros)
                    break
                

            case"2":
                print(list_nomarat)
        
                break

            case"3":
                
                nomre_hazfi = float(input("nomre ra baraye hazf vared konid: "))

                if nomre_hazfi in list_nomarat:
                    list_nomarat.remove(nomre_hazfi)
                    print("nomre hazf shod.")
                    break
                else:
                    print("in nomre dar list vojod nadarad.")

         

            case"4":
                majmoe_nomarat=sum(list_nomarat)
                miyangin_nomarat=majmoe_nomarat/len(list_nomarat)
                print("miyangin nomarat : ",miyangin_nomarat)


                if miyangin_nomarat>20 or miyangin_nomarat<0:
                    print("wrong score.")
                if 17<=miyangin_nomarat<=20 :
                    print("A")
                    
                        
                if 14<=miyangin_nomarat<17 :
                    print("B")
                  
                if 10<=miyangin_nomarat<14:
                    print("C") 
                   
                if 0<=miyangin_nomarat<10 :
                    print("abqate.")

                break

            case"5":
                break
            

       
                

