class Mobile:
    def Properties(self):
        props=["recharge","call","play music","set alarm"]
        return props
class Apps(Mobile):
    def Properties(self):
        prop=super().Properties()
        prop.append("Play games")
        prop.append("chat")
        prop.append("video call")
        return prop

Ap=Apps()
print(Ap.Properties())