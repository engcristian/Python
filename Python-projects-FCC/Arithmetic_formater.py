'''
For to check the function working, run the file Main_Arithmetic.py, it's possible change values for
the arithmetic problems.
'''

def arithmetic_arranger(problems, soluçãos=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  linha1 = ""
  linha2 = ""
  linha3 = ""
  linha4 = ""
  
  for i, problem in enumerate(problems):
    num1, op, num2 = problem.split()

    if not op in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."

    if not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits."

    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    if op == "+":
      solução = int(num1) + int(num2)
    else:
      solução = int(num1) - int(num2)

    num_length = len(max([num1,num2], key=len))

    linha1 += num1.rjust(num_length+2)
    linha2 += op + num2.rjust(num_length+1)
    linha3 += "-" * (num_length + 2)
    linha4 += str(solução).rjust(num_length+2)

    if i < len(problems)-1:
      linha1 += "    "
      linha2 += "    "
      linha3 += "    "
      linha4 += "    "

  problema_vertical = linha1 + "\n" + linha2 + "\n" + linha3

  if soluçãos:
    problema_vertical += "\n" + linha4

  return problema_vertical
  