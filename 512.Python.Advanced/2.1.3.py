class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, arg):
        if int(arg) > 0:
            list.append(self, arg)
        else:
            raise NonPositiveError
