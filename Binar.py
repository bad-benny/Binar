class Binar():
    def __init__(self, var):
        self.var = var
        self.result = 0
        if var <= 0:
            self.result = 0
        elif var > 0:
            self.result = 1