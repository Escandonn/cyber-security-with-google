# Ataques de Denegación de Servicio

Hola de nuevo. En este video veremos los ataques de denegación de servicio. Un ataque de denegación de servicio ataca una red o servidor y lo inunda con tráfico de red. Un ataque de denegación de servicio, o ataque DoS, interrumpe o altera las operaciones al sobrecargar la red de una empresa. Su objetivo es enviar tanta información a un dispositivo de red que este falle o no pueda responder a usuarios legítimos. Esto impide llevar a cabo las operaciones comerciales normales, lo que cuesta tiempo y dinero. Un fallo en la red también crea vulnerabilidad para otras amenazas y ataques.

## Ataque de Denegación de Servicio Distribuido (DDoS)

Un ataque de denegación de servicio distribuido, o DDoS, es un ataque DoS que usa varios dispositivos o servidores en diferentes lugares para inundar la red víctima con tráfico no deseado. Al usar muchos dispositivos, es más probable que el tráfico enviado sobrecargue el servidor de destino. Recuerda, DoS significa denegación de servicio. No importa qué parte de la red se sobrecargue, si se sobrecarga cualquier cosa, el atacante gana.

Un ejemplo desafortunado que conozco es un atacante que creó un buen paquete que hizo que un router tomara más tiempo en procesar la solicitud. Lo que sobrecargó el router no fue el volumen de tráfico, sino el paquete en sí mismo.

## Ataques DoS de Red

Ahora veremos ataques DoS de red cuyo objetivo es el ancho de banda, lo cual enlentece el tráfico. Veamos tres ataques DoS de red comunes.

### Ataque de Inundación Sincronizada (SYN Flood)

El primero se denomina ataque de inundación sincronizada. Es un ataque DoS que simula la conexión TCP e inunda el servidor con paquetes SYN. Analicemos esta definición profundizando en el handshake para crear una conexión TCP entre un dispositivo y un servidor.

1. En el primer paso del enlace, el dispositivo envía una solicitud SYN, de sincronización, al servidor.
2. El servidor responde con un paquete SYN/ACK para acusar recibo de la solicitud y abre un puerto para el paso final del enlace.
3. Cuando el servidor recibe el paquete ACK final del dispositivo, se crea una conexión TCP.

Los agentes maliciosos se aprovechan del protocolo inundando un servidor con solicitudes SYN para la primera parte del enlace. Pero si la cantidad de solicitudes SYN supera la de puertos en el servidor, el servidor se sobrecarga y deja de funcionar.

### Ataque de Inundación ICMP (Ping Flood)

Hablemos de otros dos ataques DoS comunes que usan otro protocolo, llamado ICMP. ICMP es el protocolo de mensajes de control de Internet. El ICMP es un protocolo de red que usan los dispositivos para comunicarse entre sí errores de transmisión de datos en la red. Piensen en el ICMP como un pedido de actualización de estado de un dispositivo. El dispositivo devuelve mensajes de error si hay algún problema de red. Es como si la solicitud ICMP consultara al dispositivo para comprobar que todo esté bien.

Un ataque de inundación ICMP es un ataque DoS de un atacante que envía repetidamente paquetes ICMP a un servidor de red. Esto obliga al servidor a enviar un paquete ICMP. Eventualmente, esto agota el ancho de banda para el tráfico entrante y saliente, y el servidor falla.

### Ping de la Muerte

Ambos ataques vistos hasta ahora, inundación SYN e inundación ICMP, se aprovechan de los protocolos de comunicación al enviar muchísimas solicitudes. También hay ataques que sobrecargan un servidor con una solicitud muy grande. Un ejemplo que veremos es el ping de la muerte. Un ataque de ping de la muerte es un ataque DoS que ocurre cuando un hacker hace ping a un sistema enviando un paquete ICMP grande, superior a 64 kilobytes, el tamaño máximo de un paquete ICMP correcto. Hacer ping a un servidor de red vulnerable con un paquete ICMP grande sobrecarga el sistema y hace que falle. Es como tirar una roca sobre un pequeño hormiguero. Cada hormiga puede cargar cierto peso al transportar comida. Pero si una roca cae sobre el hormiguero, aplastará muchas hormigas y la colonia no funcionará hasta cambiar de lugar.

## Conclusión

Concluimos los ataques DoS y DDoS. A continuación, hablaremos más sobre ataques de red comunes.
