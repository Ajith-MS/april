from blog.models import users, posts


# authenticate
def authenticate(**kwargs):
    username = kwargs.get("username")  # get used to remove the error
    email = kwargs.get("email")
    user_data = [user for user in users if user["username"] == username and user["email"] == email]
    return user_data


user = authenticate(username="Bret", email="Sincere@april.biz")
# if user:
#     print("login success")
# else:
#     print("Invalid Authentication")

session = {}


def login_required(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args, **kwargs)
        else:
            print("U must login")

    return wrapper


@login_required
def logged_user():
    username = session.get("user")
    userId = [user["id"] for user in users if user["username"] == username][0]
    return userId


class SignInView:
    def post(self, *args, **kwargs):
        username = kwargs.get("username")
        email = kwargs.get("email")
        user = authenticate(username=username, email=email)
        if user:
            print("Sign In Success")
            session["user"] = username
        else:
            print("Invalid Credentials")


@login_required
def logout(*args, **kwargs):
    session.pop("user")


class PostListView:
    @login_required
    def get(self, *args, **kwargs):
        return posts


class MyPostsView:
    @login_required
    def get(self, *args, **kwargs):
        userId = logged_user()
        my_post = [post for post in posts if post["userId"] == userId]
        return my_post


usr = SignInView()
usr.post(username="Bret", email="Sincere@april.biz")

mp = MyPostsView()
print(mp.get())


class PostCreateView():
    @login_required

    def post(self, *args, **kwargs):
        userId = logged_user()
        title = kwargs.get("title")
        body = kwargs.get("body")
        data = {
            "userId":userId,
                       "title":title,
                                 "body":body
        }
        posts.append(data)
        print("post created successfully")


usr = SignInView()
usr.post(username="Bret", email="Sincere@april.biz")
pst = PostCreateView()
pst.post(title="mypost", body="this is my new post")
mp = MyPostsView()
print(mp.get()[-1])

class PostDetailsView():
    @login_required
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        qs=[p for p in posts if p.get("id")==post_id]
        return qs

    @login_required
    def put(self,id,*args,**kwargs):
        post=[p for p in posts if p.get("id")==id][0]
        title=kwargs.get("title")
        body=kwargs.get("body")
        post[title]=title
        post[body]=body
        print(post)

detail=PostDetailsView()
print(detail.get(post_id=5))

detail.put(id=10,title="my new post is",body="this is my new post")




