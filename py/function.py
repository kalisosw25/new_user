import random


def password_generator(min, max):
  length_random = random.randint(min , max)
  length = length_random
  characterList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  password = []
  for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
  main_password = "".join(password)
  global answer
  answer = main_password
  #   print(main_password)
  return main_password


# def sampleFunc(arg):
#     print('you called sampleFunc({})'.format(arg))
#     print(arg)

# globals()['sampleFunc']('sample arg')

reader = open("need.txt", "r")
main_function = reader.read()
print(main_function)

f = open("need.txt", "w")
f.write("")
f.close()

# globals()['password_generator'](9 , 12)

exec(main_function)

f = open("answer.txt", "w")
f.write(answer)
f.close()
# print(answer)
