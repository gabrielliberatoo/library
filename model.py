class Price:
    """Classe abstrata para representar diferentes tipos de preços."""
    
    def get_charge(self, days_rented: int) -> float:
        pass

    def get_frequent_renter_points(self, days_rented: int) -> int:
        pass


class RegularPrice(Price):
    """Preço para livros regulares."""
    pass


class NewReleasePrice(Price):
    """Preço para lançamentos."""
    pass


class ChildrenPrice(Price):
    """Preço para livros infantis."""
    pass


class Book:
    REGULAR: int = 0
    NEW_RELEASE: int = 1
    CHILDREN: int = 2

    def __init__(self, title: str, price_code: int):
        self.title = title
        self.price = self.create_price(price_code)  # Agora usamos self.price em vez de self.price_code
    
    def create_price(self, price_code: int):
        """Factory method para criar o objeto Price correto."""
        if price_code == Book.NEW_RELEASE:
            return NewReleasePrice()
        elif price_code == Book.CHILDREN:
            return ChildrenPrice()
        return RegularPrice()
    
    def get_charge(self, days_rented: int) -> float:
        """Delega o cálculo para a classe Price."""
        return self.price.get_charge(days_rented)

    def get_frequent_renter_points(self, days_rented: int) -> int:
        """Delega o cálculo para a classe Price."""
        return self.price.get_frequent_renter_points(days_rented)


class Rental:
    def __init__(self, book: Book, days_rented: int):
        self.book = book
        self.days_rented = days_rented

    def get_amount(self) -> float:
        """Delega para o método get_charge da classe Book."""
        return self.book.get_charge(self.days_rented)

    def get_frequent_renter_points(self) -> int:
        """Delega para o método get_frequent_renter_points da classe Book."""
        return self.book.get_frequent_renter_points(self.days_rented)
        
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
