num = input("Voer een gatal in om te kijken of het een priemgetal is:")
num = int(num)

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is geen priemgetal")
           print(i,"keer",num//i,"is",num)
           break
   else:
       print(num,"is een priemgetal")
       
else:
   print(num,"is geen priemgetal")
