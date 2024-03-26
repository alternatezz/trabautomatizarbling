import random

# Defina var1
var1 = 90

# Gere um valor aleatório entre 1 e 1,15 com apenas duas casas decimais
diff = round(random.uniform(1, 1.15), 2)

# Calcule var2 tal que var1 - var2 seja igual ao valor aleatório gerado acima
var2 = var1 - diff

# Imprima var2
print("Valor de var2:", var2)
