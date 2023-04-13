def update_book_stock(sender, instance, **kwargs):
    """ Función para el Signal, actualizamos el stock si se elimina un prestamo """
    instance.book.stock = instance.book.stock + 1
    instance.book.save()
