salario_bruto = 1000

codigo = 3

if codigo == 1:
    valor_de_desconto = salario_bruto * (30/100)
    porcetagem = "30%"
    descontado = salario_bruto - valor_de_desconto

if codigo == 2:
    valor_de_desconto = salario_bruto * (20/100)
    porcetagem = "20%"
    descontado = salario_bruto - valor_de_desconto

if codigo == 3:
    valor_de_desconto = salario_bruto * (25/100)
    porcetagem = "25%"
    descontado = salario_bruto - valor_de_desconto

print("valor do salario ja descontado:", valor_de_desconto)
print("aliquota do IR:", porcetagem)
print("salario bruto:", salario_bruto)
print("valor ja descontado:", descontado)
