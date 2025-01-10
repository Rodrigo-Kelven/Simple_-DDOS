# Uma simples forma de enviar infinitos pacotes UDP para um alvo
***Isso foi criaco para fins educacionais ;)***
Para enviar vários pacotes UDP para um alvo você pode usar este simples script em Python. O UDP (User Datagram Protocol) é um protocolo sem conexão que permite o envio de pacotes de dados sem a necessidade de estabelecer uma conexão prévia.

## Explicação do Script

  - Importação de Módulos: O script importa os módulos socket para comunicação de rede e time para gerenciar intervalos entre envios.
  - Função enviar_pacotes_udp:
    
        - Cria um socket UDP.
        - Envia uma mensagem para o endereço IP e porta especificados pelo usuário.
        - Utiliza um loop para enviar o número desejado de pacotes, com um intervalo definido entre eles.
  - Entrada do Usuário: O script solicita ao usuário o IP do destino, a porta, o número de pacotes a serem enviados e o intervalo entre os envios.

## Considerações

  - Ambiente de Rede: Certifique-se de que a rede permite tráfego UDP e que o destinatário está preparado para receber os pacotes.
  - Testes Locais: Você pode testar localmente configurando um servidor UDP simples que escute na mesma máquina ou em outra máquina na mesma rede.
  - Segurança: O envio de pacotes UDP pode ser utilizado em cenários legítimos ou maliciosos (como ataques DDoS), portanto, use com responsabilidade.

## Instalação e Execução

## Clone o repositório

```bash
  git clone https://github.com/Rodrigo-Kelven/UDP-Flood
```
    
## Entre no diretório do projeto e de a permissão

```bash
  cd UDP-Flood
  chmod +x flood_UDP.py
```

## Inicie o script

```bash
  pyhton flood_UDP.py
```

# Contribuições

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.

## Autores

- [@Rodrigo_Kelven](https://github.com/Rodrigo-Kelven)
