# Criar um algorítmo de um banco. Será solicitado como entrada a agencia, a conta e o valor.
# Conta Corrente: Poderá ser sacado x reais após o dinheiro na conta acabar. (o usuário indicará esse limite)
# Conta Poupança: Não poderá sacar valores após o dinheiro acabar ou pedir um valor maior que o armazenado.
# Irá criar uma classe super 'Conta' para servir como base para as outras classes. Ela não poderá ser
# instânciada.

from PYTHON_POO.AMcp import ContaPoupanca


cp = ContaPoupanca(1111, 2222, 50)
cp.sacar(25)
