class Book:
    """
    @brief Represents a book.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        pages (int): The number of pages in the book.
    """

    def __init__(self, title, author, pages):
        if pages <= 0:
            raise ValueError("Pages must be positive.")
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        """
        @brief Returns a summary of the book.

        @return A string containing the book title and author.
        """
        return f"'{self.title}' by {self.author}"

    def reading_time(self, pages_per_hour):
        """
        @brief Calculates estimated reading time.

        @param pages_per_hour Pages the reader can read per hour.
        @return Estimated reading time in hours.

        @throws ValueError if pages_per_hour is non-positive.
        """
        if pages_per_hour <= 0:
            raise ValueError("Pages per hour must be positive.")
        return self.pages / pages_per_hour


class Student:
    """
    @brief Represents a student.

    Attributes:
        name (str): The name of the student.
        student_id (int): The ID of the student.
        grades (list): A list of numeric grades.
    """

    def __init__(self, name, student_id, grades=None):
        self.name = name
        self.student_id = student_id
        self.grades = grades or []
        self._validate_grades()

    def _validate_grades(self):
        """
        @brief Validates that grades are within the acceptable range (0-100).
        """
        if not all(0 <= grade <= 100 for grade in self.grades):
            raise ValueError("Grades must be between 0 and 100.")

    def average(self):
        """
        @brief Calculates the average grade.

        @return The average grade or None if no grades.
        """
        return sum(self.grades) / len(self.grades) if self.grades else None

    def is_passing(self, threshold=60):
        """
        @brief Checks if the student is passing.

        @param threshold The minimum passing grade (default 60).
        @return True if average grade >= threshold, otherwise False.
        """
        avg = self.average()
        return avg is not None and avg >= threshold


class BankAccount:
    """
    @brief Represents a bank account.

    Attributes:
        account_holder (str): Name of the account holder.
        balance (float): Current balance of the account.
    """

    def __init__(self, account_holder, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance must be non-negative.")
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """
        @brief Deposits amount into the account.

        @param amount The deposit amount.
        @return Updated balance.

        @throws ValueError if amount <= 0.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        @brief Withdraws amount from the account.

        @param amount The withdrawal amount.
        @return Updated balance.

        @throws ValueError if amount <= 0 or if amount exceeds balance.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """
        @brief Retrieves the current balance.

        @return Current balance as a float.
        """
        return self.balance
