import definiciones.clientes
import definiciones.banco


clinete5 = definiciones.clientes.Clientes('pipito mendez', 18, '1234567', 'example@gmail.com', 'calle falsa 123')
# print(clinete5)

banco1 = definiciones.banco.Banco.options(name='galicia')
# print(banco1)

banco1 = definiciones.banco.Banco.depositar_money(deposito=100, sucursales='sucursal', date="11:11")
# print(banco1)

