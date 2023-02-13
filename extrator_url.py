import re
class ExtratorURL:
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self,url):
        if type(url) == str:                 # Verifica se é uma str
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:                     # por baixo dos panos o python executa o método bool()
            raise ValueError('URL vazia')

        # Verifica se a str é extamente como descrito
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio') # entre ('<str>') busca na string a palavra completa
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('URL não é valida')

    def get_url_base(self):
        # Encontrando o '?'
        i_interrogacao = self.url.find('?')
        # Fatiando a string até o '?'
        url_base = self.url[:i_interrogacao] 
        return url_base

    def get_url_parametros(self):
        # Encontrando o '?'
        i_interrogacao = self.url.find('?')
        # Fatiando a string do '?' até o final
        url_parametros = self.url[(i_interrogacao + 1):]
        return url_parametros

    def get_valor_parametro(self,parametro_busca):
        i_parametro = self.get_url_parametros().find(parametro_busca) # buscando na str principal, a str de busca
        i_valor = i_parametro + (len(parametro_busca) + 1) # encontrando o index inicial do valor desejado (y = x + (len(x) + 1))
        i_E_comercial = self.get_url_parametros().find('&',i_valor) # encontrando o '&' apartir do primeiro index da str desejada

        # Se retorna -1 significa que não há '&', então busque até o fim da linha
        if i_E_comercial == -1:
            valor = self.get_url_parametros()[i_valor:] # método de fatiamento
        # Senão retorna até o '&'
        else:
            valor = self.get_url_parametros()[i_valor:i_E_comercial]
        return valor

extrator_url = ExtratorURL('http://www.bytebank.com.br/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar')
valor_quantidade = extrator_url.get_valor_parametro("moedaDestino")
print(valor_quantidade)