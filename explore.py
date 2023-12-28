import random

choice = ''

while choice != 'q' and choice != 'quit':
  choice = input("\n'loop' demo, 'string' demo, or 'random' demo? ").lower()
  if choice == 'loop':
    print("how fast can you add all integers from 1 to 1000?")
    print("Not as fast as Python! Starting...")
    ans = 0
    for i in range(1, 1001):
      ans += i
    print("...and done. The answer is ", ans)
  elif choice == 'string':
    ans = input("Type some words: ")
    print("That has", len(ans), "letters")
    print(ans.upper())
    print(ans.lower())
    print(ans.title())
  elif choice == 'random':
    ans = random.randint(1,100)
    print("Here's a random number:", ans)
    ans = random.uniform(-10, 10)
    print("Here's a random decimal:", ans)
    