#Finally!Let's code something in Python!
name=input("Hello there!What's your name?      ")
print("Ahhh... such a nice name!")
print("Hello ",name,"! How may I help you today?")
help=input(" ")
print("Oh, I see...")
class Coffee:
    def __init__(self,name,price):
        self.name= name
        self.price=price 
class Lets_Order:
    def __init__(self):
        self.items=[]
    def addingitems(self,coffee):
        self.items.append(coffee)
        print(f"We added {coffee.name} to your order!")
    def total(self):
        return sum(item.price for item in self.items)
    def ShowOrder(self):
        if not self.items:
            print("No items ordered!")
            return
        print("\nYour Order:")
        for i, item in enumerate(self.items,1):
            print(f"{i}.{item.name} - Rs.{item.price}") 
        print(f"Total: Rs.{self.total()}\n")
    def checkout(self):
        if not self.items:
            print("Your cart is empty dude :(")  
            return
        self.ShowOrder()
        confirm=input("Proceed to checkout?(Yes/No): ").strip().lower()
        if confirm== 'yes':
            print("Order confirmed!Thankyou!")
            self.items.clear()
        else:
            print("Checkout cancelled.")
def main():
        menu=[
            Coffee("Espresso",250),
            Coffee("Macha Latte",350),
            Coffee("Cappuccino",300),
            Coffee("Americano",200),
        ]
        order=Lets_Order()
        while True:
            print("\n- Shino's Cafe Menu <3\n")
            for i,coffee in enumerate(menu,1):
                print(f"{i}.{coffee.name} - Rs.{coffee.price}")
            print("5. View Order")
            print("6. Checkout")
            print("7.EXIT")
            choice=input("Choose an option: ")
            if choice in ['1','2','3','4']:
                order.addingitems(menu[int(choice)-1])
            elif choice=='5':
                order.ShowOrder()
            elif choice=='6':
                order.checkout()
            elif choice=='7':
                print("Thankyou so much for your valuable time! Visit again!")
                break
            else:
                print("Invalid choice!Please try again.")
if __name__=="__main__":
    main()
        