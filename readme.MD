# Aplicação simplificada de servidor para Chats em Python!

## Versão 0.1

Foram desenvolvidas três entidades, as quais são:

- Servidor (Hub): O servidor é um aplicativo Python Flask que atua como um hub para endereços IP. Ele ouve solicitações POST HTTP de clientes e armazena seus endereços IP e números de porta. Ele também ouve solicitações GET HTTP de clientes e retorna uma lista de todos os endereços registrados. Finalmente, ele ouve solicitações DELETE HTTP de clientes e remove o endereço correspondente de sua lista.

- Host (WebSocket Server): O host é um servidor Python WebSocket que ouve conexões WebSocket de outros clientes. Uma vez conectado, ele espera por mensagens de entrada e as envia de volta para o remetente.

- Cliente: O cliente é um script Python que se registra no servidor (Hub) enviando uma solicitação POST HTTP com seu endereço IP e número de porta. Ele então obtém a lista de endereços registrados enviando uma solicitação GET HTTP para o servidor. Finalmente, ele inicia uma conexão WebSocket com o primeiro endereço da lista e envia mensagens de ida e volta com o host.
