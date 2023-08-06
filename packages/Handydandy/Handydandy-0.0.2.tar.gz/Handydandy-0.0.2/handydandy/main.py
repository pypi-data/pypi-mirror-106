class handydandy:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  def printc(text, color):
    print(f'{color}{text}{handydandy.colors.ENDC}')
  def asksq(question, defaultanswer):
    x = input(f'{question}:\n({defaultanswer}) ')
    if x == "":
      y = defaultanswer
    else:
      y = x
    return(y)
  def askstandardquestion(question, defaultanswer):
    handydandy.asksq(question, defaultanswer)
  def pause():
    input("press enter to continue\n")
  def quitpause(reason):
    input("press enter to quit\n")
    quit(reason)
  def quitask(reason):
    quitaskv1 = handydandy.input.asksq("do you want to quit:  (y/n)", "y")
    if quitaskv1 == "y":
      quit(reason)
    else:
      return()
  def ask(question):
    input(question)