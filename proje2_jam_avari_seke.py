

import random

emtiyaz=(0)
list_emtiyazat=[1,-1,-2,2,-3,3,4,-4,-5,5,-6,6,7]
while True:
    menu_game=input("1.start 2.marhale 2 3.marhale 3 4.marhale4 5.marhale5  6.moshahede emtiaz 7.exit : ")
    
    match menu_game:
        case"1":
            emtiyaz_marhale_1=random.choice(list_emtiyazat)
            emtiyaz+=emtiyaz_marhale_1
            print("emtiyaze marhale aval :",emtiyaz_marhale_1)
        case"2":   
            emtiyaz_marhale_2=random.choice(list_emtiyazat)
            emtiyaz+=emtiyaz_marhale_2
            print("emtiyaze marhale dovom :",emtiyaz_marhale_2)

        case "3" :  

            emtiyaz_marhale_3=random.choice(list_emtiyazat)
            emtiyaz+=emtiyaz_marhale_3
            print("emtiyaze marhale sevom :",emtiyaz_marhale_3)

           
        case "4" :       
            emtiyaz_marhale_4=random.choice(list_emtiyazat)
            emtiyaz+=emtiyaz_marhale_4
            print("emtiyaze marhale chaharom:",emtiyaz_marhale_4)

           
        case"5" :
            emtiyaz_marhale_5=random.choice(list_emtiyazat)
            emtiyaz+=emtiyaz_marhale_5
            print("emtiyaze marhale marhale panjom  :",emtiyaz_marhale_5)
            print("!!!!!!!!!")
           

        case"6":
            print("emtiyaze nahayi  :",emtiyaz)  

        case"7":
            break

           
                

                
