class Soda:

    def __init__(self, additive=''):
        self.additive = additive  
        

    def show_my_drink(self):
        if self.additive:
            print('Газировка с {self.additive}')
        else:
            print('Эхх, классика...')    


s = Soda()
s.show_my_drink()