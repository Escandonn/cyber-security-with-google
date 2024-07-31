import nmap

# Creamos un objeto nmap
nm = nmap.PortScanner()

# Definimos la red que queremos escanear
red = '192.168.1.0/24'

# Realizamos el escaneo de descubrimiento de hosts
nm.scan(hosts=red, arguments='-sP')

# Obtenemos los hosts que están disponibles
hosts_list = nm.all_hosts()

# Imprimimos la lista de hosts
print('Hosts conectados a la red:')
for host in hosts_list:
    print(host)