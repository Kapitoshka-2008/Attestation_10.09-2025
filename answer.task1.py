class Book:
    """Книга с названием, количеством, ценой и автором."""

    def __init__(self, title: str, quantity: int, price: float, author: str) -> None:
        self.title: str = title
        self.author: str = author
        self.quantity: int = int(quantity)
        self._price: float = 0.0
        self.price = price  # через setter для валидации

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Цена не может быть меньше нуля!")
        self._price = float(value)

    def __add__(self, other: "Book") -> "Book":
        if not isinstance(other, Book):
            return NotImplemented
        total_quantity = self.quantity + other.quantity
        # Если по каким-то причинам общее количество 0, оставим среднюю цену как 0
        weighted_price = (
            0.0
            if total_quantity == 0
            else (self.price * self.quantity + other.price * other.quantity) / total_quantity
        )
        combined_title = f"{self.title} + {other.title}"
        combined_author = f"{self.author} & {other.author}" if self.author != other.author else self.author
        return Book(combined_title, total_quantity, weighted_price, combined_author)

    def __lt__(self, other: "Book") -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.price < other.price

    def __gt__(self, other: "Book") -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.price > other.price

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return (
            self.title == other.title
            and self.author == other.author
            and self.quantity == other.quantity
            and self.price == other.price
        )

    def __str__(self) -> str:
        return f"{self.title} (Количество: {self.quantity}, Цена: {self.price:.2f})"

    def __repr__(self) -> str:
        return self.__str__()
