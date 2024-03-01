
      # The deposit method makes a deposit into the
      # account
def deposit(self, amount):
    self.__balance += amount

      # The withdraw method withdraws an amount
      # from the account.

def withdraw(self, amount):
  if amount > 0 and amount <= self.__balance:
    self.__balance -= abs(amount)
            
  else:
    print('Insufficent funds or invalid negative number')


      # The get_balance method returns the
      # account balance.

def get_balance(self):
    return self.__balance



  def __str__(self):
    return 'The balance is $' + format(self.__balance, ',.2f')
