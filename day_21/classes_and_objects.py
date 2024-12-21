from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        # Initialize the Statistics class with a dataset
        self.data = data

    def count(self):
        # Return the number of elements in the dataset
        return len(self.data)

    def sum(self):
        # Return the sum of all elements in the dataset
        return sum(self.data)

    def min(self):
        # Return the smallest element in the dataset
        return min(self.data)

    def max(self):
        # Return the largest element in the dataset
        return max(self.data)

    def range(self):
        # Return the range (max - min) of the dataset
        return self.max() - self.min()

    def mean(self):
        # Return the mean (average) of the dataset
        return self.sum() / self.count()

    def median(self):
        # Return the median of the dataset
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            # If even number of elements, average the two middle elements
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def mode(self):
        # Return the mode (most frequent value) and its count
        frequency = Counter(self.data)
        max_count = max(frequency.values())
        mode = [key for key, count in frequency.items() if count == max_count]
        return {'mode': mode[0], 'count': max_count}

    def var(self):
        # Return the variance of the dataset
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()

    def std(self):
        # Return the standard deviation of the dataset
        return math.sqrt(self.var())

    def freq_dist(self):
        # Return the frequency distribution as a percentage for each unique value
        frequency = Counter(self.data)
        total_count = self.count()
        return [(round((count / total_count) * 100, 1), value) for value, count in frequency.items()]

    def describe(self):
        # Return a detailed statistical description of the dataset
        return f"""Count: {self.count()}
Sum: {self.sum()}
Min: {self.min()}
Max: {self.max()}
Range: {self.range()}
Mean: {self.mean()}
Median: {self.median()}
Mode: ({self.mode()['mode']}, {self.mode()['count']})
Variance: {self.var()}
Standard Deviation: {self.std()}
Frequency Distribution: {self.freq_dist()}"""

# Example usage:
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
print('Frequency Distribution: ', data.freq_dist())
print(data.describe())

class PersonAccount:
    def __init__(self, firstname, lastname):
        # Initialize the PersonAccount class with the account holder's first and last name
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []  # List of tuples (amount, description)
        self.expenses = []  # List of tuples (amount, description)

    def total_income(self):
        # Calculate the total income by summing all income amounts
        return sum(amount for amount, _ in self.incomes)

    def total_expense(self):
        # Calculate the total expense by summing all expense amounts
        return sum(amount for amount, _ in self.expenses)

    def account_info(self):
        # Return a summary of the account information
        return f"Account Holder: {self.firstname} {self.lastname}\nTotal Income: {self.total_income()}\nTotal Expense: {self.total_expense()}\nBalance: {self.account_balance()}"

    def add_income(self, amount, description):
        # Add a new income entry with amount and description
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        # Add a new expense entry with amount and description
        self.expenses.append((amount, description))

    def account_balance(self):
        # Calculate the account balance by subtracting total expenses from total income
        return self.total_income() - self.total_expense()

# Example usage:
account = PersonAccount("John", "Doe")
account.add_income(5000, "Salary")
account.add_income(200, "Freelancing")
account.add_expense(1500, "Rent")
account.add_expense(300, "Groceries")

print(account.account_info())