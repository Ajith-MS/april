from blog.models import users,posts

def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return(user)

print(authenticate(username="Reevu",password="reev@123"))
