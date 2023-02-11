url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

# obs: var[A:B] a entrada A é inclusiva, isto é adiciona a string
#               mas a entrada B é exclusiva, significa que excluir a string

# Fatiando a string até o '?'
url_base = url[0:19]
print(url_base)

# Fatiando a string do '?' até o final
url_parametros = url[20:36]
print(url_parametros)
