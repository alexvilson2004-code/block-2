class BankAccount:
    """Базовый класс обычного банковского счёта."""

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def show_info(self) -> None:
        """Выводит информацию о счёте."""
        print(f"Владелец: {self.owner}, баланс: {self.balance:.2f} ₽")

    def deposit(self, amount: float) -> None:
        """Пополняет счёт."""
        if amount <= 0:
            print("Сумма пополнения должна быть положительной.")
            return

        self.balance += amount
        print(f"Счёт пополнен на {amount:.2f} ₽.")

    def withdraw(self, amount: float) -> None:
        """Снимает деньги, если на счёте достаточно средств."""
        if amount <= 0:
            print("Сумма снятия должна быть положительной.")
        elif amount > self.balance:
            print("Недостаточно средств.")
        else:
            self.balance -= amount
            print(f"Снято {amount:.2f} ₽.")


class SavingsAccount(BankAccount):
    """Накопительный счёт с неснижаемым остатком."""

    def __init__(
        self,
        owner: str,
        balance: float = 0,
        minimum_balance: float = 1_000,
    ):
        # Инициализируем поля базового класса.
        super().__init__(owner, balance)
        self.minimum_balance = minimum_balance

    def show_info(self) -> None:
        """Переопределённый метод вывода информации."""
        print("Накопительный счёт:")
        # Вызываем метод базового класса.
        super().show_info()
        print(f"Неснижаемый остаток: {self.minimum_balance:.2f} ₽")

    def withdraw(self, amount: float) -> None:
        """Снимает деньги, сохраняя неснижаемый остаток."""
        if amount <= 0:
            print("Сумма снятия должна быть положительной.")
        elif self.balance - amount < self.minimum_balance:
            print("Операция отменена: должен остаться неснижаемый остаток.")
        else:
            # Само снятие выполняет метод базового класса.
            super().withdraw(amount)


def main() -> None:
    """Демонстрирует работу базового и производного классов."""

    print("=== Обычный банковский счёт ===")
    account = BankAccount("Анна", 5_000)
    account.show_info()
    account.deposit(1_000)
    account.withdraw(2_000)
    account.show_info()

    print("\n=== Накопительный счёт ===")
    savings = SavingsAccount("Иван", 10_000, minimum_balance=3_000)

    # Вызов переопределённого метода.
    savings.show_info()

    # Вызов унаследованного метода.
    savings.deposit(2_000)

    # Вызов переопределённого метода, который использует метод базового класса.
    savings.withdraw(4_000)
    savings.withdraw(6_000)

    savings.show_info()


if __name__ == "__main__":
    main()
