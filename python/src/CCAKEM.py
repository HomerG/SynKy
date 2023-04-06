class Kyber:
    def KeyGen(self):
        print("hello - Decapsulation")

    def Encapsulation(self):
        print("hello - Decapsulation")

    def Decapsulation(self):
        print("hello - Decapsulation")
        return 0

class Kyber512(Kyber):
    def __int__(self):
        # Parameter Specification
        self.k = 2
        self.n = 256
        self.q = 3329
        self.du = 10
        self.dv = 3
        self.eta = 2
        self.delta = 2^(-178)
class Kyber768(Kyber):
    def __int__(self):
        # Parameter Specification
        self.k = 3
        self.n = 256
        self.q = 3329
        self.du = 10
        self.dv = 4
        self.eta = 2
        self.delta = 2^(-164)
class Kyber1024(Kyber):
    def __int__(self):
        # Parameter Specification
        self.k = 4
        self.n = 256
        self.q = 3329
        self.du = 11
        self.dv = 5
        self.eta = 2
        self.delta = 2^(-174)