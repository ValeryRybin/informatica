class Object:
    _defaults = "name", "age", "size", "colour"
    _default_value = None

    def __init__(self, **kwargs):
        self.__dict__.update(dict.fromkeys(self._defaults, self._default_value))
        self.__dict__.update(kwargs)
    def greet(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет и я {self.size} размера, и {self.colour} цвета.")

class Undead(Object):
    def __init__(self,chemcompos='None', **kwargs):                 # почему-то не заполняет _default_value приходится прописывать везде 'None'
        super().__init__(**kwargs)
        self.chemcompos = chemcompos

    def compos(self):
        print(f"Я состою из {self.chemcompos}.")

class Alive(Object):
    def __init__(self,speed='None', course='None', **kwargs):       # почему-то не заполняет _default_value приходится прописывать везде 'None'
        super().__init__(**kwargs)
        self.course = course
        self.speed = speed

    def study(self):
        print(f"Я изучаю {self.course}.")
        
    def speed_(self):
        print(f"Я {self.speed} по скорости.")

bear = Alive(name="Potapych", age=38, size='big',speed='fast')
bear.greet()  
bear = Alive(name="Potapych", age=38, size='big',course='malina')
bear.study() 
bear.speed_() 
print('--------------------------------------------------')
stone = Undead(colour='grey', size='small',name="kamen'")
stone.greet()