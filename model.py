class Book:

    REGULAR: int = 0
    NEW_RELEASE: int = 1
    CHILDREN: int = 2

    def __init__(self, title: str, price_code: int):
        self.title = title
        self.price_code = price_code


class Rental:
    def __init__(self, book: Book, days_rented: int):
        self.book = book
        self.days_rented = days_rented

    def get_amount(self) -> float:
        """Calcula o valor do aluguel deste livro."""
        amount = 0
        if self.book.price_code == Book.REGULAR:
            amount += 2
            if self.days_rented > 2:
                amount += (self.days_rented - 2) * 1.5
        elif self.book.price_code == Book.NEW_RELEASE:
            amount += self.days_rented * 3
        elif self.book.price_code == Book.CHILDREN:
            amount += 1.5
            if self.days_rented > 3:
                amount += (self.days_rented - 3) * 1.5
        return amount

    def get_frequent_renter_points(self) -> int:
        """Calcula os pontos de fidelidade do aluguel."""
        points = 1
        if self.book.price_code == Book.NEW_RELEASE and self.days_rented > 1:
            points += 1
        return points


class Client:

    def __init__(self, name: str):
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def get_total_amount(self) -> float:
        """Calcula o valor total de todos os aluguéis do cliente."""
        return sum(rental.get_amount() for rental in self.rentals)

    def statement(self) -> str:
        total_amount = self.get_total_amount()  # Usamos o novo método
        frequent_renter_points = sum(rental.get_frequent_renter_points() for rental in self.rentals)

        result = f"Rental summary for {self.name}\n"
        for rental in self.rentals:
            result += f"- {rental.book.title}: {rental.get_amount()}\n"

        result += f"Total: {total_amount}\n"
        result += f"Points: {frequent_renter_points}"
        return result
