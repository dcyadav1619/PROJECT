# -*- coding: utf-8 -*-
"""Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17JYQXMdAwO6ERrgdAGWhBWhHw17spy1D
"""

class admin():
  def __init__(self,id='123',password='password'):
    self.id = '123'
    self.password = 'password'
  def login(self):
    self.admin_id = input('enter admin ID : ')
    self.pwd = input('enter password : ')
    if self.id == self.admin_id and self.password==self.pwd:
     
      return "logged in"
    else:
       return 'incorrect id or password'  
  def add_food_details(self):
    n = int(input('How many number food items details added : '))
    self.food_data = {}
    for i in range(n):
     self.food_name=input('enter name of food : ')
     self.quantity=input('enter quantity of food in ml/gm/pieces : ')
     self.price=input('enter price of food : ')
     self.discount=input('enter discount on food price : ')
     self.item = {'food_name':self.food_name,'quantity':self.quantity,'price':self.price,'dicount':self.discount}
     self.food_data[i] = self.item
    print(self.food_data) 
  def edit_food_details(self):
    print('do you want to edit food details YES / NO')
    c = input()
    if c == 'YES':
      n = int(input('How Many number food items should be edited : '))
      for i in range(n):
        self.food_id = int(input('enter food id for edit items : '))
        self.food_name=input('enter name of food : ')
        self.quantity=input('enter quantity of food in ml/gm/pieces : ')
        self.price=input('enter price of food : ')
        self.discount=input('enter discount on food price : ')
        self.item = {'food_name':self.food_name,'quantity':self.quantity,'price':self.price,'dicount':self.discount}
        self.food_data[self.food_id] = self.item
        print(self.food_data)
  def remove_item(self):
    print('do you want to edit food details YES / NO')
    c = input()
    if c == 'YES':
      food_id = int(input('Enter the id of food to be remove : '))
      del self.food_data[food_id]
      print(self.food_data)
  def all_food_items(self):
        return self.food_data   
   
               
class user(admin):
   def __init__(self):
    self.food_data={0: {'food_name': 'Tandoori Chicken', 'quantity': '4', 'price': '240', 'dicount': '5'}, 1: {'food_name': 'Vegan Burger', 'quantity': '1', 'price': '320', 'dicount': '10'}, 2: {'food_name': 'Truffle Cake', 'quantity': '500', 'price': '900', 'dicount': '15'}}
   def user_registration(self):
      print('You are on registration Page')
      self.full_name = input('Enter full Name : ')
      self.mobile_no = input('Enter Mobile No. : ')
      self.email = input('Enter Email ID : ')
      self.address = input('enter adress : ')
      self.password = input('enter password : ')
      print('Registration successful')
   def user_login(self):
     print('You are on login Page')
     self.login_email = input('Enter Email ID : ')
     self.login_password = input('Enter login password : ')
     if self.login_email==self.email and self.login_password == self.password:
       print('logged in ')
       return 'logged in'
     else:
       print('Incorrect email or password')  
   def new_order(self):
     print(self.food_data)
     self.choice = list(map(int,input('Enter Your Order food_ID from above list : ').split()))
     print('Your selection are : ', self.choice)
     for i in self.choice:
       if i in self.food_data:
         print('your order placed ', self.food_data[i])
   def order_history(self):
         print('your order history ')  
         for i in self.choice:  
           if i in self.choice:       
             print(self.food_data[i])
   def update_profile(self):
     print('enter details to update : ')
     self.full_name = input('Enter full Name : ')
     self.mobile_no = input('Enter Mobile No. : ')
     self.address = input('enter adress : ')
     self.password = input('enter password : ')           

admin1 = admin()
a = admin1.login()
print(a)
if a in 'logged in':
 print('yes') 
 admin1.add_food_details()  
 admin1.edit_food_details()
 admin1.remove_item()
 admin1.all_food_items()


user1=user()

user1.user_registration()
b = user1.user_login()
if b in 'logged in':
  print('yes')
  user1.new_order()
  user1.order_history()
  user1.update_profile