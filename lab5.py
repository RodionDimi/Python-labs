class Rocket:

    def __init__(self, fuel_level, total_weight,engine_running):      
        # Динамические поля (переменные объекта)
        self.fuel_level = fuel_level
        self.total_weight = total_weight
        self.engine_running = engine_running

    
    
    #Обычный метод, который расходует count кг топлива
    #Если после этого топливо ещё осталось, то выводит True, и наоборот(False)
    def spend_fuel(self, count):

        self.total_weight -= count
        self.fuel_level -= count 
        
        if self.fuel_level > 0:         #Топлива достаточно
            self.engine_running = True
            return True

        else:                           #Топлива недостаточно
            self.fuel_level=0
            self.engine_running = False    
            return False   


    #Обычный метод, выводящий текущее количество топлива
    def get_fuel_level(self):
        return f'Текущее количество топлива: {self.fuel_level}'

    #Обычный метод, выводящий текущую общую массу   
    def get_total_weight(self):
        return f'Текущая масса ракеты: {self.total_weight}'

    #Обычный метод, определяющий работает ли двигатель
    def get_is_engine_running(self):
        return f'Состояние двигателя(True-работает, False-заглох): {self.engine_running}'    


#Тестовая ракета
def Main():
    Test = Rocket(184000, 200000, True)
    k=0

    while (Test.fuel_level) > 0: 
        k+=1
        print(k,'минута')
        Test.spend_fuel(10000)
        print(Test.get_fuel_level())
        print(Test.get_total_weight())
        print(Test.get_is_engine_running())
        if Test.fuel_level == 0:
            print("Мы падаем:))")
        print()


Main()
