
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
  pip install -r requirements.txt
```
### Atençao a esta parte! Ela é crucial para o funcionamento da API.
```bash
  Você terá que subir 3 instâncias, por que? 
  Porque o service_a e o service_b são dois serviços diferentes.
  Então abra 3 janelas no seu terminal e excute esta sequência de comandos.
  uvicorn api_gateway:app --host 0.0.0.0 --port 8000
  uvicorn service_a:app --host 0.0.0.0 --port 8001
  uvicorn service_b:app --host 0.0.0.0 --port 8002
```

# Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.;)

## Autores
- [@Rodrigo_Kelven](https://github.com/Rodrigo-Kelven)

## Melhorias

- ### Autenticação e Autorização:
    - Implemente um sistema de autenticação, como OAuth2 ou JWT, para garantir que apenas usuários autorizados possam acessar a API.
    - Centralize a autorização para controlar o acesso a diferentes serviços

- ### Otimização do Roteamento:
    - Utilize técnicas de balanceamento de carga para distribuir as solicitações entre múltiplos serviços, melhorando a eficiência e a resiliência.
    - Considere a implementação de um mecanismo de fallback para redirecionar solicitações em caso de falha de um serviço.

- ### Caching:
    - Adicione caching para respostas frequentes, utilizando Redis ou Memcached, para reduzir a latência e a carga nos serviços de backend.
    - Defina políticas de expiração para garantir que os dados em cache sejam atualizados conforme necessário.

- ### Monitoramento e Logging:
    - Integre ferramentas de monitoramento, como Prometheus ou Grafana, para acompanhar o desempenho da API e identificar gargalos.
    - Implemente um sistema de logging detalhado para registrar erros e eventos importantes, facilitando a depuração.

- ### Documentação:
    - Utilize ferramentas como Swagger ou Redoc para gerar documentação interativa da API, facilitando o uso por desenvolvedores.
    - Mantenha a documentação atualizada com exemplos de uso e descrições claras dos endpoints.

- ### Testes Automatizados:
    - Crie uma suíte de testes automatizados para garantir que a API funcione conforme esperado e para detectar regressões rapidamente.
    - Considere testes de carga para avaliar como a API se comporta sob diferentes níveis de tráfego.

- ### Tratamento de Erros:
    - Implemente um sistema de tratamento de erros que retorne mensagens de erro claras e significativas para os usuários.
    - Utilize códigos de status HTTP apropriados para diferentes tipos de falhas.

- ### Versionamento da API:
    - Considere implementar versionamento na API para permitir atualizações sem quebrar a compatibilidade com clientes existentes.
    - Utilize um padrão de URL que inclua a versão, como /api/v1/....

- ### Segurança:
    - Aplique práticas de segurança, como validação de entrada e proteção contra ataques comuns (ex: SQL Injection, XSS).
    - Considere o uso de HTTPS para proteger a comunicação entre clientes e a API.

- ### Feedback do Usuário:
    - Colete feedback dos usuários da API para identificar áreas de melhoria e novas funcionalidades que podem ser adicionadas.


## Documentação da API

#### Rota da API Service_a

```http
  GET /service-a/{item_id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Ex: 1` | `int` | **Obrigatório**. Passagem de número inteiro |

#### Rota da API Service_b

```http
  GET /service-b/{item_id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Ex: 2`      | `int` | **Obrigatório**. Passagem de número inteiro |
