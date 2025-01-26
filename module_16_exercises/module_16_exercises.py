## 💻 Classes Exercises

### Exercises: Level 1

''' 1. Python has the module called _statistics_ and we can use this module to do all the statistical calculations. 
However, to learn how to make function and reuse function let us try to develop a program, which calculates 
the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation).
In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample.
You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class.
Check the output below. '''

class statistics:
    def __init__(self, numbers):
        self.numbers = numbers

    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        sort_number = sorted(self.numbers)
        n = len(sort_number)
        if n % 2 == 1:
            return sort_number[n // 2]  
        else:
            return (sort_number[n // 2 - 1] + sort_number[n // 2]) / 2

    def calculate_mode(self):
        frequency = {}
        for num in self.numbers:
            frequency[num] = frequency.get(num, 0) + 1
            max_count = max(frequency.values())
            mode = [num for num, count in frequency.items() if count == max_count]
            return mode if len(mode) != len(self.numbers) else None

    def calculate_range(self):
        return max(self.numbers) - min(self.numbers)
    
    def calculate_variance(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.numbers) / len(self.numbers)
    
    def calculate_std(self):
        variance = self.calculate_variance()
        return variance ** 0.5  # Standard deviation is the square root of the variance
        
    def min(self):
        return min(self.numbers)

    def max(self):
        return max(self.numbers)

    def count(self):
        return len(self.numbers)

    def percentile(self, p):
        sorted_data = sorted(self.numbers)
        index = (p / 100) * len(sorted_data)
        if index.is_integer():
            return sorted_data[int(index) - 1]
        else:
            lower_index = int(index)
            return (sorted_data[lower_index] + sorted_data[lower_index + 1]) / 2

    def frequency_distribution(self):
        frequency = {}
        for num in self.numbers:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        return frequency

### Exercises: Level 2

'''1. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and
it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods.
Incomes is a set of incomes and its description. The same goes for expenses.'''

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    @property
    def total_income(self):
        return sum(self.incomes.values())

    @property
    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        print(f"Name: {self.firstname} {self.lastname}")
        print(f"Total Income: ${self.total_income:.2f}")
        print(f"Total Expense: ${self.total_expense:.2f}")
        print(f"Account Balance: ${self.account_balance():.2f}")
        print("Incomes:")
        for income, amount in self.incomes.items():
            print(f"- {income}: ${amount:.2f}")
        print("Expenses:")
        for expense, amount in self.expenses.items():
            print(f"- {expense}: ${amount:.2f}")

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def account_balance(self):
        return self.total_income - self.total_expense
