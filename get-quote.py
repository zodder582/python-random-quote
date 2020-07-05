import random
def primary():
  print("Keep it logically awesome.")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last=13
  rnd=random.randint(0,13)
  print(quotes[rnd]+quotes[7])

if __name__== "__main__":
  primary()
