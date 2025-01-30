
# Simples API Gateway com FastAPI

***"Construir um simples API Gateway com FastAPI é uma tarefa bastante direta. O FastAPI é um framework moderno e rápido para construir APIs com Python, e ele é ideal para criar um API Gateway devido à sua simplicidade e desempenho."***

### Um API Gateway é um componente de software que atua como um ponto de entrada único para um conjunto de serviços de backend em uma arquitetura de microserviços. Ele desempenha um papel crucial na gestão e orquestração de chamadas de API, oferecendo uma série de funcionalidades que melhoram a eficiência e a segurança das comunicações entre clientes e serviços.
## Principais Funções de um API Gateway:

- Roteamento de Solicitações: O API Gateway direciona as solicitações dos clientes para os serviços apropriados, simplificando a comunicação.
- Agregação de Respostas: Ele pode combinar respostas de múltiplos serviços em uma única resposta, reduzindo a quantidade de chamadas que o cliente precisa fazer.
- Autenticação e Autorização: O API Gateway pode gerenciar a autenticação de usuários e a autorização de acesso a serviços, centralizando a segurança.- 
- Controle de Tráfego: Permite implementar políticas de limitação de taxa (rate limiting) e controle de acesso, ajudando a proteger os serviços contra abusos.
- Monitoramento e Logging: Facilita o monitoramento do tráfego de API e a coleta de logs, permitindo uma melhor análise de desempenho e identificação de problemas.
- Transformação de Dados: Pode modificar as solicitações e respostas, como converter formatos de dados ou adicionar cabeçalhos.

## Vantagens do Uso de um API Gateway:

- Simplicidade: Os clientes interagem com um único ponto de entrada, simplificando a arquitetura.
- Segurança: Centraliza a segurança, reduzindo a superfície de ataque.
- Desempenho: Pode melhorar o desempenho através de caching e otimização de chamadas.
- Escalabilidade: Facilita a escalabilidade, permitindo que novos serviços sejam adicionados sem impactar os clientes.

## Exemplos de Ferramentas de API Gateway:

- Kong
- AWS API Gateway
- NGINX
- Traefik
- FastAPI (como mencionado anteriormente, pode ser usado para criar um API Gateway simples)


## Instalação
```bash
  git clone https://github.com/Rodrigo-Kelven/Simples_API_Gateway
  cd Simples_API_Gateway
  docker-compose up --build
```

## Acesse as aplicações nos seguintes URLs:

    Service A: http://localhost:8000/docs#/
    Service B: http://localhost:8001/docs#/
    Service C: http://localhost:8002/docs#/

## Para testar a rota do API Gateway que chama o Service A, você pode acessar:

    http://localhost:8080/service_a/items

## Para testar a rota do API Gateway que chama o Service B, você pode acessar:

    http://localhost:8080/service_b



# Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.;)

## Autores
- [@Rodrigo_Kelven](https://github.com/Rodrigo-Kelven)


