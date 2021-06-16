class Category:
  #set up the class with a name, balance, and ledger
  def __init__(self,name):
    self.name=name
    self.balance=0
    self.ledger=[]
    self.spent=0
  #add some money to the balance, and record it in the ledger
  def deposit(self,amount,description=""):
    self.balance+=amount
    self.ledger.append({"amount":amount, "description":description})
  #spend some money(if it is available) and record it in the ledger
  #otherwise dont break your budget
  def withdraw(self,amount,description=""):
    if self.balance>=amount:
      self.balance-=amount
      self.spent+=amount
      #store amount as a negative number
      neg_amount=amount*-1
      self.ledger.append({"amount":neg_amount, "description":description})
      return True
    else:
      return False
  #Tell the user how much money they have in the budget
  def get_balance(self):
    return self.balance
  #let the user move money around
  def transfer(self, amount,target):
    if self.balance>=amount:
      self.withdraw(amount,"Transfer to "+target.name)
      target.deposit(amount,"Transfer from "+self.name)
      return True
    else:
      return False
  #Let the user check their funds
  def check_funds(self,amount):
    return self.balance>=amount 
  #Handle print function
  def __str__(self):  
    output=""
    header_output=""
    #figure out how many stars to have before name
    stars_before=(30-len(self.name))//2
    #add the stars before
    for i in range(stars_before):
      header_output+="*"
    #add the name
    header_output+=self.name
    #add stars after
    for i in range(30-len(header_output)):
      header_output+="*"
    #print our beautiful starry header
    output+=header_output+"\n"
    #Now for the ledger items
    for entry in self.ledger:
      entry_output=""
      #get only the first 23 characters of the description
      desc_string=entry.get("description")[0:23]
      entry_output+=desc_string
      #add spaces up to 23 characters
      for i in range(23-len(desc_string)):
        entry_output+=" "
      #handle the first 4 digits of the amount
      #we only need to take care of 4 because there are 7 characters remaining and the last 3 will always be the decimal
      amount_list=str(entry.get("amount")).split(".")
      amount_string=amount_list[0][:4]
      #add spaces to keep it right aligned
      for i in range(4-len(amount_string)):
        entry_output+=" "
      #add the decimal point
      amount_string+="."
      #if there is a decimal add it
      if len(amount_list)>1:
        amount_string+=amount_list[1]
      #handle adding decimal 0s
        if len(amount_list[1])==1:
          amount_string+="0"
      else:
        amount_string+="00"
      entry_output+=amount_string
      output+=entry_output+"\n"
    #Handle the total line
    #split the balance to ensure we have a decimal
    total_string=str(self.balance).split(".")
    #check for decimal
    if len(total_string)<2:
      total_string.append("00")
    elif len(total_string[1])<2:
      total_string[1]+="0"
    total_string= ".".join(total_string)
    output += "Total: "+total_string
    return output



def create_spend_chart(categories):
  #First we need to calculate the percentage spent on each category
  #figure out the total spent
  total_spent = 0
  for category in categories:
    total_spent+=category.spent
  #then store the percentage in an array
  category_perc=[]
  for category in categories:
    category_perc.append(category.spent/total_spent)
  #start building the chart
  output="Percentage spent by category\n"
  #make the body
  for i in range(11):
    #add spaces for alignment
    if(i>0):
      output+=" "
      if i == 10:
        output+=" "
    #labels for y axis
    output+=str(100-(i*10))+"|"
    for j in range(len(categories)):
      #add the bars or spaces
      if category_perc[j]>= 1-(i/10):
        output+=" o "
      else:
        output+="   "
    #end the line with an extra space for testing
    output+=" \n"
  #add spacing for bottom axis
  output+="    "
  #add the bottom axis lines
  for i in range(len(categories)):
    output+="---"
  #one extra line for tests and end the line
  output+="-\n"
  #figure out the longest category name
  label_length=0
  for c in categories:
    if len(c.name)>label_length:
      label_length=len(c.name)
  for i in range(label_length):
    #add spaces for labels
    output+="    "
    #check if each category's name is long enough
    for category in categories:
      if len(category.name)>i:
        output+=" "+ category.name[i]+" "
      #otherwise add spaces
      else:
        output+="   "
    #add extra space and end line
    output+=" \n"
  #remove final line break for tests
  output=output[:-1]
  return output
