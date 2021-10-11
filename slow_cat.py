from cat import Cat


class SlowCat(Cat):
    meow_message = 'meeoow'
    _speed = 100
    _color = ''

    def __init__(self, color):
        self._color = color

    def _meow(self):
        print(self.meow_message)

    def run(self):
        print('Slow cat run')
