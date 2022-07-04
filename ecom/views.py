from ecom.models import users,products,carts
def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    userdata=[user for user in users if user["username"]==username and user["password"]==password]
    return userdata
user=authenticate(username="Ajith MS",password="ajithms@123")