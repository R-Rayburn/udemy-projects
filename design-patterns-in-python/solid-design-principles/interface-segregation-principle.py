# ISP
# - Don't stick too many methods to values

# Don't want these showing up for devs on code complete
class Machine:
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, documnet):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        pass

class OldFashionedPrinter(Machine):
    def print(self, documnet):
        # OK
        pass
    def fax(self, document):
        pass # no op 
        # - can be problematic due to this still showing even though we don't utilize it.
    def scan(self, document):
        raise NotImplementedError('Printer cannot scan')
        # Ok if the user can code to detect this error.
        # Problem if it is a larger application, cause can cause crashes
        # Can add comments like """Not Supported""", but still problemeatic


# Let's split the interface out
class Printer:
    @abstractmethod
    def print(self, documnet):
        pass
class Faxer:
    @abstractmethod
    def fax(self, document):
        pass
class Scannner:
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass

# To allow an interface where they don't have to
#  do multiple interface inheritance
class MultiFunctionDevice(Printer, Scanner)
    @abstractmethod
    def print(self, documnet):
        pass

    @abstractmethod
    def scan(self, document):
        pass

# This uses this as a decorator that takes in printer
#  and scanner objects, and uses this classes methods
#  to call the same methods of the items passed in
class MultiFuncionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)