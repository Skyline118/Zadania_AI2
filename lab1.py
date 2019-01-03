tic1 = """\
      |  |
    --+--+--
      |  |
    --+--+--
      |  |  \n
    """
print("First tic-tac-toe board:\n" + tic1)

tic2 = """\
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  |  
    ========+========+========
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  |  
    ========+========+========
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  | \n
    """
print("Second tic-tac-toe board:\n" + tic2)

def __fizzBuzz__(n):
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

print("FizzBuzz:" + str(__fizzBuzz__(408)) + "\n")


def convert():
    f = input('Temperature F? ')
    c = (float(f) - 32)*5/9
    print('It is {0} degrees Celsius.'.format(round(c,2)))

convert()
convert()
convert()
