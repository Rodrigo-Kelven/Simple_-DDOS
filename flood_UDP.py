import socket
import time

def enviar_pacotes_udp(ip_destino, porta_destino, numero_pacotes, intervalo):
    # Cria um socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i in range(numero_pacotes):
        mensagem = f"Pacote {i + 1}"
        sock.sendto(mensagem.encode(), (ip_destino, porta_destino))
        print(f"Enviado: {mensagem} para {ip_destino}:{porta_destino}")
        time.sleep(intervalo)

if __name__ == "__main__":
    # Configurações do usuário
    ip_destino = input("Digite o IP do destino: ")
    porta_destino = int(input("Digite a porta do destino (80,8080,443): "))
    numero_pacotes = int(input("Quantos pacotes deseja enviar? "))
    intervalo = float(input("Intervalo entre os pacotes (em segundos): "))

    enviar_pacotes_udp(ip_destino, porta_destino, numero_pacotes, intervalo)
