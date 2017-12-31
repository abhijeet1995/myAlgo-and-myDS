class Knapsack:
    @classmethod
    def max_of(cls,a,b):
        if a>b:
            return a
        else:
            return b

    @classmethod
    def knapsack(cls, weight, value, capacity):
        if len(weight)==0 or capacity==0:
            return 0
        else:
            return cls.max_of((value[len(value)-1]+cls.knapsack(weight[:len(weight)-1], value[:len(weight)-1], capacity-weight[len(weight)-1])), cls.knapsack(weight[:len(weight)-1], value[:len(weight)-1], capacity))

print(Knapsack.knapsack([10,20,30],[60,100,120],30))
