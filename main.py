url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

#--------------------------------------------------------------------------------------------------------#
# O operador de fatiamento [a:b], utilizado para obter uma substring desde o índice a até o índice b - 1 
# da string original. Lembrando que b - 1 pois o segundo argumento do fatiamento é exclusivo.
# OBS.: se o fatiamento esta sem um dos argumentos, significa que inicia/finaliza até de/ate inicio/fim da linha [:B]-[B:]
#--------------------------------------------------------------------------------------------------------#

# Encontrando o '?'
i_interrogacao = url.find('?')

# Fatiando a string até o '?'
url_base = url[:i_interrogacao] 
print(url_base)

# Fatiando a string do '?' até o final
url_parametros = url[(i_interrogacao + 1):]
print(url_parametros)
