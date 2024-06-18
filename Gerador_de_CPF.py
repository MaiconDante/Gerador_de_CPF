# GERANDO DÍGITOS PARA CPF !!!

import random

qtd_cpf = input("Digite a quantidade de CPF'S que gostaria que fosse gerado: ")

while qtd_cpf.isdigit() == False:
    qtd_cpf = input("Isso não é um número, digite apenas números: ")
    
# CÁLCULO DO PRIMEIRO DÍGITO DO CPF !!!

for _ in range(int(qtd_cpf)):

  cpf_nine_digit = ""

  for i in range(9):
    cpf_nine_digit += str(random.randint(0, 9))
  totalizer = 0

  for i, value in enumerate(cpf_nine_digit,-10):
    totalizer += abs((i * int(value)))

  calc_first_digit = (totalizer * 10) % 11

  if calc_first_digit > 9:
    result = 0
  else:
    result = calc_first_digit

# CÁLCULO DO SEGUNDO DÍGITO DO CPF !!!

  cpf_eleven_digit = cpf_nine_digit+str(result)
  totalizer_2 = 0

  for i, value in enumerate(cpf_eleven_digit,-11):
    totalizer_2 += abs((i * int(value)))

  calc_second_digit = (totalizer_2 * 10) % 11

  if calc_second_digit > 9:
    result2 = 0
  else:
    result2 = calc_second_digit

  new_cpf = cpf_eleven_digit+str(result2)
  mask = new_cpf[:3]+"."+new_cpf[3:6]+"."+new_cpf[6:9]+"-"+new_cpf[9:11]
  print(">"*17)
  print("|   CPF GERADO  |")
  print("|---------------|")
  print(f"|{mask} |")
  print("|---------------|")
  print("<"*17)