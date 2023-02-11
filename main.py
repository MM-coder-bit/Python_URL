url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
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

# método len() para buscar o valor desejado
parametro_busca = 'moedaDestino'
i_parametro = url_parametros.find(parametro_busca) # buscando na str principal, a str de busca
i_valor = i_parametro + (len(parametro_busca) + 1) # encontrando o index inicial do valor desejado (y = x + (len(x) + 1))
i_E_comercial = url_parametros.find('&',i_valor) # encontrando o '&' apartir do primeiro index da str desejada

# Se retorna -1 significa que não há '&', então busque até o fim da linha
if i_E_comercial == -1:
    valor = url_parametros[i_valor:] # método de fatiamento
# Senão retorna até o '&'
else:
    valor = url_parametros[i_valor:i_E_comercial]
print(valor)