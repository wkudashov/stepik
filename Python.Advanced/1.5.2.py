class Buffer:
    def __init__(self):
        self.current_part = []

    def add(self, *a):
        for _i in a:
            self.current_part.append(_i)
            if len(self.current_part) == 5:
                tmp = 0
                for _j in self.current_part:
                    tmp += _j
                print(tmp)
                self.current_part.clear()

    def get_current_part(self):
        return self.current_part