# write a code to get purchase price from the user and if the total is less than 50, add 10 or else no shipping is applied
total = float(input('enter the total of purchase'))
if total < 50 :
    print('10$ shipping will applied')
    totalpurchase = total + 10
    print('shipping will be = ' + str(totalpurchase))
else:
     print('shipping is free')
print('thanks for shopping')
