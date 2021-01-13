class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for item in self.iterable:
            self.pos = 0
            self.neg = 0

            self.pos = list(map(lambda p: p(item), self.funcs)).count(True)
            self.neg = len(self.funcs) - self.pos

            if self.judge == multifilter.judge_any and multifilter.judge_any(self.pos, self.neg):
                yield item
            elif self.judge == multifilter.judge_half and multifilter.judge_half(self.pos, self.neg):
                yield item
            elif self.judge == multifilter.judge_all and multifilter.judge_all(self.pos, self.neg):
                yield item
