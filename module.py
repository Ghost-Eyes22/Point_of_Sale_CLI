# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make teh Point of Sale Application functional.


class PointOfSale:
  def __init__(self):
    self.checkout_total = 0 # This is an example varialbe, remove it or change it as you please.
    print("\nInitializing POS system...")
  def cart(self):
    print("These Are The Items In Your Cart")

  def add(self):
    item = input("What would you like to add?")
    self.cart_item.append(item)
    print("Added", item, "to the cart")

  def checkout():
     print("1.Yes")
     print("2.No")
     print("Would you like to confirm?")
     if input == "y":
      print ("confirmed and ordering!")
     if input == "n":
      print("canceling purchace")


  def exit():
     print("exiting the system!")
   

  def start(self): # This is the function that should be used to start the application.
    print("Please select what you would like to do.")
    print("1.Show Cart")
    print("2.clear cart")
    print("3.add to cart")
    print("4.checkout")
    print("5.Exit App")


while True:
    choice = input("Enter Selection:")
    if choice == "1":
        self.cart()

    if choice == "2":
      while self.cart:
          item = self.cart.pop()
          print("Your list of items:", item)

    if choice == "3":
      while self.cart:
          item = self.cart.append()
          print("Your list of items :", item)
    
    if choice == "4":
       self.cart()
      
