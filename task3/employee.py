class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self):
        return self.salary * 0.10  


class Manager(Employee):
    def __init__(self, name, salary, management_level):
        super().__init__(name, salary)
        self.management_level = management_level
    
    def calculate_bonus(self):
        base_bonus = super().calculate_bonus()
        if self.management_level > 3:
            return base_bonus + (self.salary * 0.05)  
        return base_bonus


class Developer(Employee):
    def __init__(self, name, salary, know_javascript):
        super().__init__(name, salary)
        self.know_javascript = know_javascript
    
    def calculate_bonus(self):
        base_bonus = super().calculate_bonus()
        if self.know_javascript:
            return base_bonus + (self.salary * 0.03)  
        return base_bonus

manager = Manager("Иван Иванов", 100000, 4)
developer = Developer("Петр Петров", 80000, True)

manager_bonus = manager.calculate_bonus()
developer_bonus = developer.calculate_bonus()

print(f"Менеджер {manager.name}:")
print(f"  Зарплата: {manager.salary} руб.")
print(f"  Уровень руководства: {manager.management_level}")
print(f"  Премия: {manager_bonus} руб.")
print(f"  Общий доход: {manager.salary + manager_bonus} руб.")
print()

print(f"Разработчик {developer.name}:")
print(f"  Зарплата: {developer.salary} руб.")
print(f"  Владеет JavaScript: {'Да' if developer.know_javascript else 'Нет'}")
print(f"  Премия: {developer_bonus} руб.")
print(f"  Общий доход: {developer.salary + developer_bonus} руб.")