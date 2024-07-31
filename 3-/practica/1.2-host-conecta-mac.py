import nmap

# Crear un objeto nmap
nm = nmap.PortScanner()

# Definir la red que se va a escanear
red = '192.168.1.0/24'

# Realizar el escaneo de host
nm.scan(hosts=red, arguments='-sn')

# Obtener la información de los host conectados
for host in nm.all_hosts():
    print('Host:', host)
    if'mac' in nm[host]['addresses']:
        print('MAC Address:', nm[host]['addresses']['mac'])
    else:
        print('MAC Address: No disponible')
    if 'hostnames' in nm[host] and len(nm[host]['hostnames']) > 0:
        print('Hostname:', nm[host]['hostnames'][0]['name'])
    else:
        print('Hostname: No disponible')
    print('Estado:', nm[host]['status']['state'])
    print('---')