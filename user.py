## TODO:Abstract a class
## OOP feature:
## 1. Encapsulation
## 2. Abstraction
## 3. Inheritance
## 4. Polymorphism
class User():
	num_users = 0
	users = []   

	def __init__(self, name, email, password, id, roles):
		self.name = name
	    self.email = email
	    self.password = password
	    self.id = User.num_users
	    self.roles = roles

	def _save(self, user):#_ means do not use this method outside the class
	 	self.users.append(user)

	def update(self, user):
	 	#Get user and update

	def _delete(self, user):
		#get user and delete

class Admin(User): #Inheriting from the User class
	def __init__(self, name, email, password):
		super.__init__(name=name, email=email, password=password)
