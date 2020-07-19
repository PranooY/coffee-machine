
class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu')
        coffee_choice = input()
        if coffee_choice == 'back':
            return
        if coffee_choice == '1':
            self.check_deduct(250, 0, 16, 4)
        elif coffee_choice == '2':
            self.check_deduct(350, 75, 20, 7)
        elif coffee_choice == '3':
            self.check_deduct(200, 100, 12, 6)

    def check_deduct(self, water_deduct, milk_deduct, beans_deduct, money_add):
        if self.water - water_deduct < 0:
            print('Sorry not enough water!')
            return

        if self.milk - milk_deduct < 0:
            print('Sorry not enough milk!')
            return

        if self.beans - beans_deduct < 0:
            print('Sorry not enough coffee!')
            return

        print('I have enough resources, making you a coffee!')
        self.water -= water_deduct
        self.milk -= milk_deduct
        self.beans -= beans_deduct
        self.money += money_add
        self.cups -= 1

    def fill(self):
        print('Write how many ml of water do you want to add:')
        water_add = int(input())
        print('Write how many ml of milk do you want to add:')
        milk_add = int(input())
        print('Write how many grams of coffee beans do you want to add:')
        beans_add = int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        cups_add = int(input())
        self.water += water_add
        self.milk += milk_add
        self.beans += beans_add
        self.cups += cups_add

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def display_stats(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')


if __name__ == "__main__":
    my_coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == 'buy':
            my_coffee_machine.buy()
        elif action == 'fill':
            my_coffee_machine.fill()
        elif action == 'take':
            my_coffee_machine.take()
        elif action == 'remaining':
            my_coffee_machine.display_stats()
        elif action == 'exit':
            break
