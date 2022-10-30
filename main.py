class Bank_accounts:
  def __init__(self, user_id, user_name, account_type, account_number, balance):
    self.user_id = user_id
    self.user_name = user_name
    self.account_type = account_type
    self.balance = balance

accounts_list = []

Lisa = Bank_accounts("001", "Lisa", "deposit", "111111", "1000")
Ben = Bank_accounts("002", "Ben", "saving", "222222", "2000")
Sasha = Bank_accounts("003", "Sasha", "checking", "333333", "3000")
Anna = Bank_accounts("004", "Anna", "checking", "444444", "4000")
Alex = Bank_accounts("005", "Alex", "deposit", "555555", "5000")

accounts_list.append(Lisa)
accounts_list.append(Ben)
accounts_list.append(Sasha)
accounts_list.append(Anna)
accounts_list.append(Alex)
print(accounts_list[0].user_id)