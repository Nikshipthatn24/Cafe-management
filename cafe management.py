class Cafe:
    total=[]
    amount=0
    print(''
      'WELCOME TO OUR RESTAURANT\n\n'
      'PIZZA : Rs100 \n'
      'PASTA : Rs150 \n'
      'BURGER : Rs150 \n'
      'SALAD : Rs70 \n'
      'COFFEE : Rs50 \n '
      'TEA : Rs40\n')

    def order(self):
        global quantity


        o = input('Enter your item : ').upper()

        quantity = int(input('How much is required : '))
        price= int(input('The price of the item is : '))

        if (o =='PIZZA' and price==100) or( o=='PASTA' and price== 150) or (o=='BURGER' and price=='150' )or (o=='SALAD' and price==70 )or (o== 'COFFEE' and price==50 )or (o=='TEA' and price==40):
            self.quantity = price * quantity
            self.total.append(self.quantity)
            print('********************************************')
            print(f'order of {o} has been added')
            cafe.order1()
        else:
            print(' Either the item or price is not  properly')
            cafe.order()

    def order1(self):
        while True:
            print('********************************************')
            o = input('Do you want to order(y/n) : ').upper()
            if o=='Y':
                cafe.order()

            elif o=='N':
                print('Thank you')
                cafe.display()
                exit()

            else:
                print('Please enter properly')


    def display(self):

        print('********************************************')
        totals=sum(self.total)


        print(f'The total amount is {totals}')

cafe=Cafe()
cafe.order()





