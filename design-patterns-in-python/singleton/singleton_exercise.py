def is_singleton(factory):
    return factory() is factory()
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not

