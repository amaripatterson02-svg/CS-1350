# hw_oop_module2_patterson_amari.py
from abc import ABC, abstractmethod
import math

# -------------------------
# Problem 1: Shape classes
# -------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"This is a {self.__class__.__name__}"

    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        print(f"{name} must be positive!")
        return False

class Circle(Shape):
    def __init__(self, radius):
        if not Shape.validate_positive(radius, "radius"):
            raise ValueError("radius must be positive")
        self.radius = radius

    def area(self):
        # use π = 3.14159 per spec
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        if not Shape.validate_positive(width, "width"):
            raise ValueError("width must be positive")
        if not Shape.validate_positive(height, "height"):
            raise ValueError("height must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if not Shape.validate_positive(side1, "side1"):
            raise ValueError("side1 must be positive")
        if not Shape.validate_positive(side2, "side2"):
            raise ValueError("side2 must be positive")
        if not Shape.validate_positive(side3, "side3"):
            raise ValueError("side3 must be positive")
        # Optional: Could also check triangle inequality here; not required by spec
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        # Could check isinstance(shape, Shape) but spec didn't require; we'll accept any duck-typed shape
        self.shapes.append(shape)

    def total_area(self):
        total = 0.0
        for s in self.shapes:
            total += s.area()
        return total

    def total_perimeter(self):
        total = 0.0
        for s in self.shapes:
            total += s.perimeter()
        return total

# -------------------------
# Problem 2: Pizza classes
# -------------------------
class Pizza:
    price_list = {'small': 10, 'medium': 15, 'large': 20}
    topping_price = 2

    def __init__(self, size, toppings):
        if not Pizza.validate_size(size):
            raise ValueError("Invalid pizza size")
        self.size = size.lower()
        self.toppings = toppings[:]  # copy

    def calculate_price(self):
        base = Pizza.price_list[self.size]
        tcost = len(self.toppings) * Pizza.topping_price
        return base + tcost

    def __str__(self):
        # Example: "large pizza with 3 toppings - $26"
        return f"{self.size} pizza with {len(self.toppings)} toppings - ${self.calculate_price()}"

    @classmethod
    def create_margherita(cls, size):
        return cls(size, ['cheese', 'tomato', 'basil'])

    @classmethod
    def create_pepperoni(cls, size):
        return cls(size, ['cheese', 'pepperoni'])

    @classmethod
    def create_veggie(cls, size):
        return cls(size, ['cheese', 'mushrooms', 'peppers', 'onions'])

    @staticmethod
    def validate_size(size):
        return size and size.lower() in ['small', 'medium', 'large']

class PizzaOrder:
    total_orders = 0

    def __init__(self):
        PizzaOrder.total_orders += 1
        self.order_number = PizzaOrder.total_orders
        self.order_id = f"ORDER_{self.order_number:03d}"
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total(self):
        total = 0
        for p in self.pizzas:
            total += p.calculate_price()
        return total

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    def __str__(self):
        return f"Order {self.order_id} - Total: ${self.get_total()}"

class OrderManager:
    @staticmethod
    def create_order_from_string(order_string):
        """
        Parse string like 'large pepperoni, small margherita'
        """
        order = PizzaOrder()
        items = [item.strip() for item in order_string.split(",") if item.strip()]
        for item in items:
            parts = item.split()
            if len(parts) < 2:
                raise ValueError(f"Can't parse order item '{item}'")
            size = parts[0].lower()
            pizza_type = " ".join(parts[1:]).lower()
            if pizza_type == "margherita":
                pizza = Pizza.create_margherita(size)
            elif pizza_type == "pepperoni":
                pizza = Pizza.create_pepperoni(size)
            elif pizza_type in ["veggie", "vegetarian"]:
                pizza = Pizza.create_veggie(size)
            else:
                # unknown type - raise error per cautious behavior
                raise ValueError(f"Unknown pizza type '{pizza_type}' in item '{item}'")
            order.add_pizza(pizza)
        return order

    @staticmethod
    def format_receipt(order):
        lines = []
        lines.append("=== RECEIPT ===")
        lines.append(f"Order: {order.order_id}")
        lines.append("Items:")
        for p in order.pizzas:
            lines.append(f"{p}")
        lines.append(f"Total: ${order.get_total()}")
        lines.append("===============")
        return "\n".join(lines)

# -------------------------
# Problem 3: Duration class
# -------------------------
class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # Accept overflow values; convert to normalized h,m,s
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("hours, minutes, and seconds must be non-negative")
        total = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
        # normalize into h,m,s
        h = total // 3600
        rem = total % 3600
        m = rem // 60
        s = rem % 60
        self.hours = h
        self.minutes = m
        self.seconds = s

    @property
    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        parts = []
        if self.hours:
            parts.append(f"{self.hours}h")
        if self.minutes:
            parts.append(f"{self.minutes}m")
        if self.seconds:
            parts.append(f"{self.seconds}s")
        if not parts:
            return "0s"
        return " ".join(parts)

    def __repr__(self):
        return f"Duration({self.hours}, {self.minutes}, {self.seconds})"

    def __add__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        total = self.total_seconds + other.total_seconds
        return Duration(0, 0, total)

    def __sub__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        diff = self.total_seconds - other.total_seconds
        if diff <= 0:
            return Duration(0, 0, 0)
        return Duration(0, 0, diff)

    def __mul__(self, multiplier):
        if not isinstance(multiplier, int):
            raise TypeError("Can only multiply Duration by integer")
        if multiplier < 0:
            raise ValueError("Multiplier must be non-negative")
        total = self.total_seconds * multiplier
        return Duration(0, 0, total)

    # Comparison operations (based on total_seconds)
    def __eq__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return self.total_seconds == other.total_seconds

    def __lt__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return self.total_seconds < other.total_seconds

    def __le__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return self.total_seconds <= other.total_seconds

# -------------------------
# Test your code (main)
# -------------------------
if __name__ == "__main__":
    # Problem 1 tests
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)

    print("Individual Shapes:")
    for shape in [circle, rectangle, triangle]:
        print(f" {shape.describe()}")
        print(f" Area: {shape.area():.2f}")
        print(f" Perimeter: {shape.perimeter():.2f}")

    collection = ShapeCollection()
    collection.add_shape(circle)
    collection.add_shape(rectangle)
    collection.add_shape(triangle)
    print(f"\nCollection Totals:")
    print(f" Total Area: {collection.total_area():.2f}")
    print(f" Total Perimeter: {collection.total_perimeter():.2f}")

    print("\nTesting validation:")
    try:
        bad_circle = Circle(-5)
    except:
        print(" Correctly rejected negative radius")

    # Problem 2 tests (pizza)
    pizza1 = Pizza.create_margherita("large")
    pizza2 = Pizza.create_pepperoni("medium")
    pizza3 = Pizza.create_veggie("small")
    print("\nIndividual Pizzas:")
    for pizza in [pizza1, pizza2, pizza3]:
        print(f" {pizza} - ${pizza.calculate_price()}")

    order1 = PizzaOrder()
    order1.add_pizza(pizza1)
    order1.add_pizza(pizza2)
    print(f"\n{order1}")

    print("\nOrder from string:")
    order2 = OrderManager.create_order_from_string(
        "large pepperoni, small margherita, medium veggie"
    )
    print(OrderManager.format_receipt(order2))
    print(f"\nTotal orders created: {PizzaOrder.get_total_orders()}")

    # Problem 3 tests (Duration)
    d1 = Duration(1, 30, 45)
    d2 = Duration(0, 45, 30)
    d3 = Duration(2, 15, 0)
    print("\nDurations:")
    print(f" d1 = {d1}")
    print(f" d2 = {d2}")
    print(f" d3 = {d3}")

    print("\nArithmetic:")
    print(f" d1 + d2 = {d1 + d2}")
    print(f" d3 - d1 = {d3 - d1}")
    print(f" d2 * 3 = {d2 * 3}")

    print("\nComparisons:")
    print(f" d1 == d2? {d1 == d2}")
    print(f" d1 < d3? {d1 < d3}")
    print(f" d2 <= d1? {d2 <= d1}")

    durations = [d3, d1, d2]
    durations.sort()
    print("\nSorted durations:")
    for d in durations:
        print(f" {d}")

    print("\nOverflow test:")
    d4 = Duration(0, 90, 90)  # Should become 1h 31m 30s
    print(f" Duration(0, 90, 90) = {d4}")
    print(f"\nRepr: {repr(d1)}")
