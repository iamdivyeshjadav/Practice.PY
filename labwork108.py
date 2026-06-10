class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Admin(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role

    def show(self):
        print("Username:", self.username)
        print("Email:", self.email)
        print("Role:", self.role)

admin = Admin("Divyesh", "divyesh@gmail.com", "Administrator")
admin.show()
'''
Output:
Username: Divyesh
Email: divyesh@gmail.com
Role: Administrator
'''