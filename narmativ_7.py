class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    def __str__(self):
        return f"{self.name} - {self.description} - {self.price} so'm"
    
class Starter(Dish):
    def __init__(self, name, description, price):
        super().__init__(name, description, price)

class MainCourse(Dish):
    def __init__(self, name, description, price, vegetarian=False, gluten_free=False):
        super().__init__(name, description, price)
        self.vegetarian = vegetarian
        self.gluten_free = gluten_free

    def __str__(self):
        extra = []
        if self.vegetarian:
            extra.append("Vegetarian")
        if self.gluten_free:
            extra.append("Gluten-Free")
        return f"{super().__str__()} {'(' + ', '.join(extra) + ')' if extra else ''}"


class Dessert(Dish):
    def __init__(self, name, description, price, vegetarian=False, gluten_free=False):
        super().__init__(name, description, price)
        self.vegetarian = vegetarian
        self.gluten_free = gluten_free

    def __str__(self):
        extra = []
        if self.vegetarian:
            extra.append("Vegetarian")
        if self.gluten_free:
            extra.append("Gluten-Free")
        return f"{super().__str__()} {'(' + ', '.join(extra) + ')' if extra else ''}"
    
class Menu:
    def __init__(self):
        self.dishes = []
    def add_dish(self, dish):
        self.dishes.append(dish)
    def remove_dish(self, name):
        for dish in self.dishes:
            if dish.name.lower() == name.lower():
                self.dishes.remove(dish)
                print(f"{name} menyudan o'chirildi.")
                return
        print(f"{name} menyuda yo'q")
    def display_menu(self):
        if not self.dishes:
            print("Menyuda hozircha bo'sh")
        else:
            print(" MENYU ")
            for dish in self.dishes:
                print(dish)

class Order:
    def __init__(self):
        self.items = []
    def add_item(self, dish):
        self.items.append(dish)
    def total_price(self):
        total = 0
        for dish in self.items:
            total += dish.price
        if total > 100.000:
            print("Buyurtma 100,000 so'mdan oshdi 10% chegirma qilindi.")
            total *= 0.9
        return total
    def summary(self):
        if not self.items:
            print("Buyurtma bo'sh")
            return
        print(" BUYURTMANGIZ ")
        for dish in self.items:
            print(dish)
        print(f"Jami SUMMA: {self.total_price():,.0f}")

def main():
    menu = Menu()
    order = Order()
    while True:
        print("1. Yangi taom qo'shish")
        print("2. Taomni o'chirish")
        print("3. Menyuni ko'rish")
        print("4. Buyurtma qilish")
        print("5. Dasturdan chiqish")
        choice = input("Tanlovni kiriting (1-5): ")
        if choice == "1":
            name = input("Taom nomi: ")
            description = input("Tavsif: ")
            price = int(input("Narxi (so'm): "))
            dish_type = input("Taom turi (starter, main, dessert): ").lower()

            if dish_type == "starter":
                dish = Starter(name, description, price)
            elif dish_type == "main":
                veg = input("Vegetarianmi? (ha/yo'q): ").lower() == "ha"
                gluten = input("Gluten-free? (ha/yo'q): ").lower() == "ha"
                dish = MainCourse(name, description, price, veg, gluten)
            elif dish_type == "dessert":
                veg = input("Vegetarianmi? (ha/yo'q): ").lower() == "ha"
                gluten = input("Gluten-free? (ha/yo'q): ").lower() == "ha"
                dish = Dessert(name, description, price, veg, gluten)
            else:
                print("Noto'g'ri taom turi.")
                continue
            menu.add_dish(dish)
            print(f"{name} menyuga qo'shildi.")
        elif choice == "2":
            name = input("O'chiriladigan taom nomi: ")
            menu.remove_dish(name)
        elif choice == "3":
            menu.display_menu()
        elif choice == "4":
            menu.display_menu()
            name = input("Buyurtma qilmoqchi bo'lgan taom nomini kiriting: ")
            for dish in menu.dishes:
                if dish.name.lower() == name.lower():
                    order.add_item(dish)
                    print(f"{name} buyurtmangizga qo'shildi.")
                    break
            else:
                print(f"{name} menyuda topilmadi.")
            view_total = input("Buyurtmani ko'rishni istaysizmi? (ha/yo'q): ").lower()
            if view_total == "ha":
                order.summary()
        elif choice == "5":
            print("Dastur tugatildi.")
            break
        else:
            print("Noto'g'ri tanlov.")
    main()
