import math

BYTE = 8
DIRECCIONES_OCUPADAS = 2
ATRIBUTOS_SUBNETEO = 4


def ajustar_por_hosts(num_hosts):
    bits_hosts = calcular_bits(num_hosts + DIRECCIONES_OCUPADAS)
    bits_red = BYTE - bits_hosts
    salto = calcular_salto(bits_hosts)
    return [bits_red, bits_hosts, salto]


def ajustar_por_red(num_redes):
    bits_red = calcular_bits(num_redes)
    bits_hosts = BYTE - bits_red
    salto = calcular_salto(bits_hosts)
    return [bits_red, bits_hosts, salto]


def calcular_bits(num):
    return int(math.ceil(math.log(num, 2)))


def calcular_salto(num_hosts):
    return calcular_posibilidades(num_hosts)


def calcular_posibilidades(num):
    return int(math.pow(2, num))


def subnetear(bits_subred, bits_hosts, salto, ip):
    num_subredes = calcular_posibilidades(bits_subred)
    num_hosts = calcular_posibilidades(bits_hosts) - 2
    subredes = []

    subred_actual = 0
    for i in range(num_subredes):
        primer_host = subred_actual + 1
        ultimo_host = primer_host + num_hosts - 1
        broadcast = ultimo_host + 1
        subredes.append([ip+str(subred_actual), ip+str(primer_host), ip+str(ultimo_host), ip+str(broadcast)])
        subred_actual += salto

    return subredes


#obtener la direccion ip
ip = input("Ingrese la direccion ip: ")

#quitar el ultimo octeto
ip_list = ip.split(".")
del ip_list[-1]

ip = ""

for octeto in ip_list:
    ip += octeto+"."

print(ip)
opc = input("Desea ajustar por [H]osts o por [R]ed? H/R ")
opc = opc.upper()

config_subneteo = list()

if(opc == "H"):
    num_hosts = int(input("Ingrese el numero de hosts: "))
    config_subneteo = ajustar_por_hosts(num_hosts)
elif(opc == "R"):
    num_subredes = int(input("Ingrese el numero de subredes: "))
    config_subneteo = ajustar_por_red(num_subredes)

print(config_subneteo)
print(subnetear(config_subneteo[0], config_subneteo[1], config_subneteo[2], ip))
