import functools


def validar_argumentos_enteros(function):
    """ Decorador que valida que todos los argumentos de una función
        sean enteros.

    Args:
        function (function): Función a decorar

    Raises:
        TypeError: Error cuando alguno de los argumentos no es entero

    Regresa:
        function: Llamada a la función con los argumentos enteros
    """
    print("Entrando al decorador")

    @functools.wraps(function)
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError
        return function(*args)
    return wrapper
