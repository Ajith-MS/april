def admin_permission_required(fn):
    def inner_fun(*args, **kwargs):
        user = kwargs.get("user")
        if user.role != "admin":
            raise Exception("Permission denied")
        else:
            return fn(*args, **kwargs)
        return inner_fun


class User:
    def set_user(self,username,role):
        self.username =username
        self.role =role

    def print_Details(self):
        print(self.username, self.role)


class AddCourse:
    @admin_permission_required
    def set_Addvalues(self, *args, **kwargs):
        self.user= kwargs.get("user")
        self.course_name = kwargs.get("course_name")

    def print_Details(self):
        print(self.course_name)


class AddBatch:
    @admin_permission_required
    def set_Values(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.course = kwargs.get("course")
        self.batch_name = kwargs.get("batch_name")

    def print_Details(self):
        print(self.batch_name)


user = User()
add_course = AddCourse()
add_batch = AddBatch()
user.set_user("Ajith ms", "admin")
add_course.set_Addvalues("Django")
add_batch.set_Values("April_batch")
user.print_Details()
add_course.print_Details()
add_batch.print_Details()