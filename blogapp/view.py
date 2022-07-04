
from blogapp.models import users,posts
#authenticate(username,password)
# username="anu"
# password="Password@123"
#get        :=retrive
#post       :=create
#put/patch  :=edit
#delete     :=delete

session={}

def signInRequired(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("You must Login!")
    return wrapper


def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user
print(authenticate(username="anu",password="Password@123"))

class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print("Success")
        else:
            print("Invalid")

class PostView():
    @signInRequired
    def get(self,*args,**kwargs):
        return posts

    @signInRequired
    def post(self,*args,**kwargs):
        userId=session["user"]["id"]
        kwargs["userId"]=userId
        posts.append(kwargs)
        print(posts)


class MyPostListView:
    @signInRequired
    def get(self,*args,**kwargs):
        print(session)
        userId=session["user"]["id"]
        print(userId)
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post


class PostDetailsView:
    @signInRequired
    def get_object(self,id):
        data=[post for post in posts if post["postId"]==id]
        return data

    @signInRequired
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post=self.get_object(post_id)
        return post

    @signInRequired
    def delete(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=[post for post in posts if post["postId"]==post_id]
        if data:
            post=data[0]
            posts.remove(post)
            print("Post Removed")
            print("length=",len(posts))

    @signInRequired
    def put(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post=self.get_object(post_id)[0]
        data=kwargs.get("data")
        post.update(data)
        print(post)


class LikeView:
    @signInRequired
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post=[post for post in posts if post["postId"]==post_id]
        if post:
            post=post[0]
            print(post)


@signInRequired
def signout(*args,**kwargs):
    user=session.pop("user")
    print(f"the user {user['username']} has been logged out")



log=SignInView()
log.post(username="akhil",password="Password@123")
print(session)


data={
    "title":"Hello this is my updated title"
}

post_detail=PostDetailsView()
# post_detail.delete(post_id=6)
# print(post_detail.get(post_id=6))
post_detail.get(post_id=6,data=data)

mypost=MyPostListView()
print(mypost.get())


# data=PostView()
# print(data.get())
# data.post(postId=9,title="hey here",content="content",liked_by=[])
#
like=LikeView()
like.get(post_id=6)

signout()