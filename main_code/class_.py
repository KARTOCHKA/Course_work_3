class Tranzaction():
    def __init__(self, date, desc, from_, to, summ, cur):
        self.date = date
        self.desc = desc
        self.from_ = from_
        self.to = to
        self.summ = summ
        self.cur = cur

    def __repr__(self):
        print(f"{self.date} {self.desc}\n{self.from_} -> {self.to}\n{self.summ} {self.cur}")
