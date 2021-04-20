class Account:
     #初始化方法，创建账户
     def  __init__(self,name,password,money=0):
          self.name=name
          self.password = password
          self.money = money

       #存款   
     def deposit(self,password,money):
          if password== self.password:
               if isinstance(money,(int,float)) and money>=0:
                    self.money +=money
                    return '存款成功：%元，账户余额为:%元'%(money,self.money)
               else:
                    return '请输入正确的存款金额'
          else:
               return  '请输入正确的账户密码'
        #取款
     def withdraw(self,password,money):
          if password== self.password:
               if isinstance(money,(int,float)) and money>=0 and money<=self.money:
                    self.money -=money
                    return '取款成功：%元，账户余额为:%元'%(money,self.money)
               else:
                    return '请输入正确的取款金额'
          else:
               return  '请输入正确的账户密码'
          #查询余额
     def query(self,password):
          if password== self.password:
               return  '您的账户余额为:%元'%self.money
          else:
               return  '请输入正确的账户密码'
     def close(self,password):
          if password== self.password:
               if self.money ==0:
                    self.name=''
                    self.password = ''
                    self.money = 0
               else:
                    return  '您的账户余额不为0，请取完金额再来执行销户操作'
          else:
               return  '请输入正确的账户密码'
                    












          
          
     
