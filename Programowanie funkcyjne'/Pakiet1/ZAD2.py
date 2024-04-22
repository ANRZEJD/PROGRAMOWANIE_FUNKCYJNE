def make_multiplier(multiplier):
    def multiplier_function(x):
        return x * multiplier
    
    return multiplier_function
