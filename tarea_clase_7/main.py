from decorators import validar_argumentos_enteros


@validar_argumentos_enteros
def add(a, b):
    """ Función que suma dos números enteros

    Args:
        a (int): valor a sumar 1
        b (int): valor a sumar 2

    Regresa:
        int: resultado de la suma de a + b

    Ejemplos de uso:

    >>> add(1, 2)
    3
    """
    return a + b


print(f'Nombre de la función: {add.__name__}')
print(f'Docstring de la función: {add.__doc__}')
print(f'Resultado de la suma add(1, 2): {add(1, 2)}')
print('Resultado de la suma add(1.1, 2):')
try:
    print(f'{add(1.1, 2)}')
except TypeError:
    print("Todos los argumentos deben ser enteros.")
