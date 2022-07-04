class Ide:
    def functionalities(self):
        fun=["read","write","append"]
        return fun
class Pycharm(Ide):
    def functionalities(self):
        funs=super().functionalities()
        funs.append("debug")
        funs.append("execute")
        return funs
py=Pycharm()
print(py.functionalities())
