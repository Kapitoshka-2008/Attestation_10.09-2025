from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def get_description(self) -> str:
        """Возвращает строковое описание товара."""
        raise NotImplementedError


class Product(AbstractProduct):
    """Базовый продукт с приватной ценой и количеством."""

    def __init__(self, title: str, quantity: int, price: float) -> None:
        self.title: str = title
        self.quantity: int = int(quantity)
        self.__price: float = 0.0
        self.set_price(price)

    def get_price(self) -> float:
        """Возвращает текущую цену."""
        return self.__price

    def set_price(self, new_price: float) -> None:
        """Устанавливает цену, проверяя, что значение не отрицательное."""
        if new_price < 0:
            raise ValueError("Цена не может быть меньше нуля!")
        self.__price = float(new_price)


class Book(Product):
    """Книга с названием, количеством, ценой и автором."""

    def __init__(self, title: str, quantity: int, price: float, author: str) -> None:
        self.author: str = author
        super().__init__(title=title, quantity=quantity, price=price)

    def __add__(self, other: "Book") -> "Book":
        if not isinstance(other, Book):
            return NotImplemented
        total_quantity = self.quantity + other.quantity
        weighted_price = (
            0.0
            if total_quantity == 0
            else (self.get_price() * self.quantity + other.get_price() * other.quantity) / total_quantity
        )
        combined_title = f"{self.title} + {other.title}"
        combined_author = f"{self.author} & {other.author}" if self.author != other.author else self.author
        return Book(combined_title, total_quantity, weighted_price, combined_author)

    def __lt__(self, other: "Book") -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.get_price() < other.get_price()

    def __gt__(self, other: "Book") -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.get_price() > other.get_price()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return (
            self.title == other.title
            and self.author == other.author
            and self.quantity == other.quantity
            and self.get_price() == other.get_price()
        )

    def __str__(self) -> str:
        return f"{self.title} (Количество: {self.quantity}, Цена: {self.get_price():.2f})"

    def __repr__(self) -> str:
        return self.__str__()

    def get_description(self) -> str:
        return f"Книга: {self.title}, Автор: {self.author}"
