class Mobile:
    def functionalities(self):
        funs={"phnlog":"call","phn":"recharge","phnmsg":"message"}
        return funs
class Apps(Mobile):
    def functionalities(self):
        fun=super().functionalities()
        fun["insta"]="reel post chat"
        fun["BGMI"]="play game"
        return fun


ap=Apps()
print(ap.functionalities())