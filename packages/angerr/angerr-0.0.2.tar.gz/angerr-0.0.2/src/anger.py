class GodDammit(Exception):
  def __init__(self, message="look i can't show your anger if you don't enter the anger amount.  make sure it is a int too, lmfao. *can't believe you don't even know how to code lol*"):
    self.message = message
    super().__init__(self.message)

def anger(amount : int = None):
  """The `Anger` function.  Allows you to express anger major when your coding doesn't work.

  Paramaters:
    amount (int): the amount of your angerrrrrrrr
  
  """
  if amount == None:
    print("WHY IS CODING SO HARD")
  else:
    if type(amount) != int:
      raise GodDammit
    else:
      for i in range(amount):
        print(f"{i + 1}. WHY IS CODING SO HARD")
      if str(amount).__contains__(69) or str(amount).__contains__(420):
        print("nice\n")
      print("finally done raging.  are you?")