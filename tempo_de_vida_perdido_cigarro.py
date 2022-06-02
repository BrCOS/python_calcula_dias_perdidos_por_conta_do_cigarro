quantidade = int(input('Digite a quantidade de cigarros que você fuma por dia: '))
tempo = int(input('Digite por quantos anos você fuma: '))

sum = quantidade * (tempo * 365)

minutos_perdidos = sum * 10

subtracao = (minutos_perdidos/60)/24

print('Você perdeu %.2f dias de vida.'%subtracao)