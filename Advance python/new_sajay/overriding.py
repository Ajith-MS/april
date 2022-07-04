class Ide:
    def functionalities(self):
        funs=["read","write","delete"]
        return funs
class Pycharm(Ide):
    def functionalities(self):
        fun=super().functionalities()
        fun.append("execute")
        fun.append("debug")
        return fun
class Vscode(Ide):
    def functionalities(self):
        funs=super().functionalities()
        funs.append("vsc")
        funs.append("formatting")
        return funs
p=Pycharm()
print(p.functionalities())
vsc=Vscode()
print(vsc.functionalities())
