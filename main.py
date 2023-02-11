url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

#--------------------------------------------------------------------------------------------------------#
# O operador de fatiamento [a:b], utilizado para obter uma substring desde o índice a até o índice b - 1 
# da string original. Lembrando que b - 1 pois o segundo argumento do fatiamento é exclusivo.
#--------------------------------------------------------------------------------------------------------#

# Fatiando a string até o '?'
url_base = url[0:19]
print(url_base)

# Fatiando a string do '?' até o final
url_parametros = url[20:36]
print(url_parametros)
