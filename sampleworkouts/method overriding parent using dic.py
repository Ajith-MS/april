class Parent:
    def functionalities(self):
        self.funs = {"mobile": "vivo", "scooty": "vespa", "tv": "BPL"}
        return self.funs


class Child(Parent):
    def functionalities(self):
        fun= super().functionalities()
        fun["car"] = "BMW"
        return fun


c = Child()
print(c.functionalities())
