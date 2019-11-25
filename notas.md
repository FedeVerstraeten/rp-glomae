# Notas de uso de RedPitaya:

Todas las notas a continuación son un resumen de problemas y soluciones (workaround) que se han encontrado durante el uso de *[RedPitaya STEMLab 125-10](https://www.redpitaya.com/f130/STEMlab-board)*.

## Información general PCHost:

La computadora (PCHost) utilizada para realizar el desarrollo y las pruebas tiene las siguientes especificaciones:

```
Processor: Intel(R) Core(TM) i3-4005U CPU 64 bits @ 1.70GH.
Memory: 8GB RAM DDR4.
Storage: Disco magnético de 500GB de 7200RPM.
OS: Linux
Distributor ID: Ubuntu
Description: Ubuntu 14.04.2 LTS
Release: 14.04
Codename: Trusty Tahr
```

## Notas

- Las memorias SD suelen corromperse y fallan incluso en el proceso de grabado de una nueva. Probar con diversas memorias de distintos tamaños hasta lograr que cargue el sistema operativo.

- Utilizar *Google Chrome* como browser para levantar la interfaz gráfica (mediante el server `nginx`). Con Mozilla Firefox suele fallar.

- Configurar la conexión LAN como *link-local* desactivando DHCP Automático (si lo estuviere).
```
[802-3-ethernet]
duplex=full
mac-address= <MAC_ADDRESS_PC_HOST>

[connection]
id=RedPitaya
uuid=cdc3942d-4241-48b9-8151-8cf98d75ce76
type=802-3-ethernet

[ipv6]
method=link-local

[ipv4]
method=link-local
```
- En la PC Host se puede estar conectado en simultáneo sin inconvenientes vía Wi-Fi (con proxy configurado en un browser) y mediante cable Ethernet a la RedPitaya (accediento con Chrome).

- Para acceder mediante la terminal de debug, conectar el adaptador USB-to-TTL a los pines que están al lado del puerto hembra USB de la RedPitaya de la forma: RXD->Rx, TXD->Tx, GND->GND. Ejecutar luego en la PC Host la terminal mediante el comando `miniterm.py /dev/ttyUSB0 115200` adecuando la dirección del dispositivo y el Baud-Rate según sea necesario.

- Para ejecutar un comando vía python desde la PC Host, previamente hay que ejecutar dentro de RedPitaya el comando `systemctl start redpitaya_scpi.service` o bien ingresando desde el browser a `http://rp-f0477c.local/scpi_manager/` y activar *SCPI Server* donde nos indicará la IP y el puerto por donde podremos conectarnos con scripts externos (ejemplos: Python, Matlab, etc.). Verificar que el servicio esté corriendo correctamente con `systemctl status redpitaya_scpi.service`.
