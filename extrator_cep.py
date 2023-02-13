endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 21440-120"

# Regular Expression -- RegEx
import re  
# Buscando padrão
# 5 dígitos + hífen (opcional) + 3 dígitos
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)
else:
    print('Nao encontrado')