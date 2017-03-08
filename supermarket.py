class supermarket:
	   product=4000
	   customer=200

	   def _init_ (self,customer,product):

		   self.customer=customer
		   self.product= product
		   milk=supermarket(customer=20,product=200)
			
class customer(supermarket):

	   def _init_(self,id,quantity):

	     	self.id=id
	     	self.quantity=quantity

	     	if milk<=0:
         		print("not valied")

           elif milk>200:
         		print("wrong figures")

         	else :
         		print("customer")


class product(supermarket):

	   def _init_(self,id,price):

	     	self.id=id
	     	self.price=price

         	if milk<=0:
         		print("not valied")

         	else milk>200:
         		print("wrong figures")

