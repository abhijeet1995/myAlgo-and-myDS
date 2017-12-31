class Max:
    @classmethod
    def max_of(cls, a, b):
        if a > b:
            return a
        else:
            return b

    @classmethod
    def max_mul(cls, a, count):
        if len(a) == 0 or count == 3:
            return 1
        else:
            return cls.max_of(a[-1]*cls.max_mul(a[:len(a)-1], count+1), cls.max_mul(a[:len(a)-1], count))


print(Max.max_mul([-70, -50], 0))
