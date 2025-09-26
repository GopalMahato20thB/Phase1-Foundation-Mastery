---

## 🔹 1. `Classes-Objects`

Focus: Defining classes, attributes, methods, and creating objects.

**Exercises:**

1. Create a `Book` class with attributes `title`, `author`, and `price`. Add a method `display_info()` to print details.
2. Build a `BankAccount` class with attributes `account_number`, `balance`, and methods `deposit()` and `withdraw()`.
3. Create a `Circle` class with a method to compute area and circumference. Instantiate multiple circles with different radii.
4. Write a `Student` class with attributes `name`, `roll_no`, and `marks`. Add a method `get_grade()` that returns grade based on marks.
5. Create a `Car` class with attributes like `make`, `model`, `year`, and a method `start_engine()`.

---

## 🔹 2. `Encapsulation`

Focus: Private/protected attributes, getter/setter methods, controlled access.

**Exercises:**

1. Implement a `PasswordManager` class where the password is private (`__password`). Add methods to set and validate the password.
2. Build an `Employee` class where salary is private. Use getter and setter methods to control access.
3. Create a `Wallet` class that keeps balance private but allows methods `add_money()` and `spend_money()`. Print error if spending more than balance.
4. Implement a `User` class with private attributes `__email` and `__password`. Add methods `login(email, password)` and `update_password(new_password)`.
5. Modify `BankAccount` (from Classes-Objects) to make `balance` private, and allow only deposit/withdraw through methods.

---

## 🔹 3. `Inheritance`

Focus: Parent-child relationships, method overriding, multiple inheritance.

**Exercises:**

1. Create a base class `Animal` with method `sound()`. Inherit `Dog` and `Cat` classes that override `sound()`.
2. Make a `Vehicle` class and derive `Car` and `Bike` classes. Add a method `wheels()` to show different wheel counts.
3. Implement a `Person` class and derive `Student` and `Teacher`. Both should have different `display_info()` methods.
4. Create a `Shape` class with method `area()`. Derive `Rectangle`, `Circle`, and `Triangle` classes with proper implementations.
5. Show multiple inheritance with a `Musician` class and `Dancer` class, and derive a `Performer` class.

---

## 🔹 4. `Polymorphism`

Focus: Method overloading (via default args), method overriding, duck typing, operator overloading.

**Exercises:**

1. Create a function `add()` in a class that can add two or three numbers (using default arguments).
2. Demonstrate duck typing: Write a function `perform_sound(animal)` that works with different objects having a `sound()` method (Dog, Cat, Cow).
3. Implement operator overloading (`__add__`) for a `Vector` class so that `v1 + v2` adds their coordinates.
4. Create a `Shape` base class with method `area()`. Derive `Circle`, `Square`, and `Rectangle`, each implementing its own `area()`. Use polymorphism to calculate areas in a loop.
5. Overload the `__str__` method in a `Book` class so printing the object directly shows book details.

---

## 🔹 5. `Data-Abstraction`

Focus: Abstract Base Classes (ABC), hiding implementation details.

**Exercises:**

1. Create an abstract class `Shape` with an abstract method `area()`. Implement `Circle`, `Rectangle`, and `Triangle`.
2. Build an abstract class `Payment` with abstract methods `pay()` and `refund()`. Implement subclasses `CreditCardPayment` and `UPIPayment`.
3. Define an abstract class `Vehicle` with abstract methods `start()` and `stop()`. Implement `Car` and `Bike` subclasses.
4. Make an abstract class `Database` with methods `connect()` and `disconnect()`. Implement `MySQLDatabase` and `MongoDatabase`.
5. Create an abstract class `Appliance` with method `turn_on()`. Implement `Fan`, `Light`, and `AC`.

---

