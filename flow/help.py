def pass_to_normal(lista):

    for word in lista:
        new_value = ''
        for index, uppercase in enumerate(map(str.isupper, word)):
            if index != 0 and uppercase:
                new_value += '_' + word[index].lower()
            else:
                new_value += word[index].lower()
        print(f'{" "*8}{new_value} = models.')



def to_model(lista):
    dictionary = {'varchar': 'CharField',
                  'datetime':'DateTimeField',
                  'date': 'DateField',

                  'numeric': 'IntegerField',
                  'char': 'Varchar'
    }
    for word in lista:
        word_, rest = word.split('(')
        number, _ = rest.split(')')
        field = dictionary[word_.lower()]
        print(f"{field}(max_length={number})")


if __name__ == '__main__':
    lista = [ 'RecordIndicator',
            'PreviousTransCode',
            'PreviousRetServiceOrder',
            'CurrentTransCode',
            'CurrentRetServiceOrder']
    lista1 = ['Numeric(3)', 'Char(1)', 'Varchar(15)', 'Char(1)', 'Varchar(15)']
    to_model(lista1)
    #pass_to_normal(lista)
