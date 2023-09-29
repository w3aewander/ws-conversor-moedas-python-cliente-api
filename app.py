#--*--charset: utf-8 --*--


import requests

url = "https://www.wmomodavix.com.br/api/public/?"

resp_dolar = requests.get(url+"dolar")
resp_euro = requests.get(url+"euro")
resp_bitcoin = requests.get(url+"bitcoin")

print("\n==================================================\n")
print("\n=     Prgrama para conversão entre moedas        =\n")
print("\n=     consumindo API com taxas atualizadas       =\n")
print("\n==================================================\n\n")


print("Código da resposta: {0}\n".format(resp_dolar.status_code))
print("\n=========================================================")
print("Valor do Dólar do dia:{0}\n".format(resp_dolar.content))
print("Valor do Euro do dia: {0}\n" . format(resp_euro.content))
print("Valor do Bitcoin do dia: {0}\n".format(resp_bitcoin.content))


valor_em_dolares = float(input("\nDigite o valor em dólares:"))
taxa_dolar = float(resp_dolar.content)

valor_em_euros = float(input("\nDigite o valor em euros:"))
taxa_euro = float(resp_euro.content)

valor_em_bitcoins = float(input("\nDigite o valor em bitcoins:"))
taxa_bitcoin = float(resp_bitcoin.content)


valor_em_reais = valor_em_dolares * taxa_dolar
print("\n{0} dólares convertido em reais: {1}".format(valor_em_dolares, valor_em_reais))

valor_em_reais = valor_em_euros * taxa_euro
print("\n{0} euros convertido em reais: {1}".format(valor_em_euros, valor_em_reais))

valor_em_reais = valor_em_bitcoins * taxa_bitcoin
print("\n{0} bitcoins convertido em reais: {1}".format(valor_em_bitcoins, valor_em_reais))

print("\n==================================================")
print("\n=     Fim do Script de conversão de moedas       =")
print("\n==================================================\n")
