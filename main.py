def run():
    """
        Los Doctrings son estas cadenas de caracteres escritas entres triples
        comillas dobles " o triples comillas simples ', se usan principalmente
        para documentar partes del codigo como funciones o clases.
        Se recomienda escribir la documentacion en ingles y sin usar caracteres
        especiales como acentos o ñ.
    """

    print("Hola mundo!") # Este es un comentario de una sola linea
    # este tipo de comentarios se pueden usar arriba o abajo de una linea de codigo
    # En la linea de abajo se usa otro tipo de string el cual se escribe dentro
    # de comillas simples '' y es equivalente a los strings que se escriben con comillas dobles ""
    print('Hello world!') # tambien se pueden usar al final de una linea, para no afectar su ejecucion


if __name__ == '__main__':
    # La linea superior hace referencia al punto de entrada del programa (entry point)
    run() # Esta linea ejecuta la funcion run, la cual contiene la parte principal del programa


# Por lo general es mala practica escribir muchos comentarios a menos que sean totalmente requeridos
# en este ejemplo se usan asi a modo de ilustrar su uso.
# Por ultimo, hay que observar que el contenido de todo este archivo es totalmente equivalente a escribir
# las siguientes lineas sin identacion, ya que la ejecucion produce el mismo resultado
# print("Hola mundo!")
# print('Hello world!')
