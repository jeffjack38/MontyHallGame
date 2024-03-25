# Monty Hall Problem GUI & Simulation

## Purpose
This Python project demonstrates the Monty Hall Problem through a graphical user interface (GUI) game and a simulation. The Monty Hall Problem is a probability puzzle that explores the concept of conditional probability and decision-making strategies.

## Tech Stack
- **Python**: Programming language used for the entire project.
- **tkinter**: Python's standard GUI library utilized for creating the graphical interface.
- **PyCharm**: Integrated Development Environment (IDE) used for writing, debugging, and managing the Python code.

## Skills Demonstrated
- **Abstraction**:
  - Abstraction refers to the process of simplifying complex systems by hiding unnecessary details while emphasizing essential features.
  - In the project, abstraction is demonstrated by defining classes to represent high-level entities such as the game, players, and individuals.
  - Each class abstracts away implementation details, focusing instead on providing a clear interface for interacting with the entity.
  - Example:
    ```python
    class Game(tk.Frame):
        def __init__(self, parent):
            # Constructor method to initialize the game
            ...
    ```

- **Encapsulation**:
  - Encapsulation involves bundling data and methods within a class and controlling access to them.
  - It helps in hiding the internal state of objects and only exposing necessary functionality through methods.
  - In the project, encapsulation is demonstrated by defining classes with attributes and methods, where attributes are encapsulated and accessed via methods.
  - Access to attributes can be controlled by using private or protected access modifiers.
  - Example:
    ```python
    class Person:
        def __init__(self, fname, lname):
            self._last_name = lname  # Encapsulated attribute
            ...

        def display(self):
            # Method to display person's name
            ...
    ```

- **Inheritance**:
  - Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse and creating a hierarchy of classes.
  - It enables the creation of specialized classes (subclasses) that inherit common behavior from a more general class (superclass).
  - In the project, inheritance is demonstrated by creating subclasses such as `Player`, which inherits attributes and methods from the `Person` class.
  - Example:
    ```python
    class Player(Person):
        def __init__(self, fname, lname, id):
            super().__init__(fname, lname)
            # Additional attributes and methods specific to Player class
            ...
    ```

- **Polymorphism**:
  - Polymorphism allows objects of different classes to be treated as objects of a common superclass, promoting flexibility and extensibility in the code.
  - It allows methods to be implemented in different ways in different subclasses, while still adhering to a common interface.
  - In the project, polymorphism is demonstrated by overriding methods in derived classes to customize their behavior, allowing for different implementations of common functionality.
  - Example:
    ```python
    class Person:
        def display(self):
            # Common method for displaying person's name
            ...

    class Player(Person):
        def display(self):
            # Overridden method to include player's ID
            ...
    ```
