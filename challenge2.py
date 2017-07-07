total = float(input('enter the total of purchase'))
if total < 50 :
    print('shipping will applied')
    shipping = total + 10
    print('shipping will be = ' + str(shipping))
else:
     print('shipping is free')
print('thanks for shopping')
