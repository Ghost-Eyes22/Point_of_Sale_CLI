# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make teh Point of Sale Application functional.


class PointOfSale:
  def __init__(self):
    self.checkout_total = 0 # This is an example varialbe, remove it or change it as you please.
    print("\nInitializing POS system...")
    self.cart = []
    self.prices = []


  def cart(self):
    if len(self.cart) == 0:
      print("Your cart is empty)")
      return
    for i in range(0,len(self.cart)):
      print(self.cart[i], ": $", self.prices[i])
    
  def add(self):
    product = input("What item would you like to add?")
    self.cart.append(product)
    price = float(input("how much does this item cost"))
    print(product, price)
    return

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
    print("2.add to cart")
    print("3.checkout")
    print("4.Exit App")


    while True:
      choice = input("Enter Selection:")

      if choice == "1":
        self.cart()

      if choice == "2":
        self.get_user_items()
        print("Your list of items:")

      if choice == "3":
        self.cart()
        print("Caculating all of your items")
        print("Your list of items :", self.cart())
      
      if choice == "4":
        break        
