
class Snake:
    ''' Esta es la clase snake, de tener unos parámetros de constructor, acá irían'''

    def eat(self, animal):
        ''' Toda serpiente necesita comer
        :param animal: Hoy que animal va a comer
        :type animal: str
        :return: Si la serpiente está dispuesta a comer o no
        :rtype: str
        '''
        return 'Delicious!!!' if animal is 'mouse' else 'No thanks'
