# Weather App — Backend

API desenvolvida com Python e FastAPI para consulta de previsão do tempo.

## Tecnologias

- Python 3
- FastAPI
- Uvicorn
- HTTPX
- OpenWeatherMap API

## Pré-requisitos

- Python 3.10 ou superior

## Instalação

**1. Clone o repositório**
```bash
git clone <url-do-repositorio>
cd weather-app-backend
```

**2. Crie o ambiente virtual**
```bash
python3 -m venv .venv
```

**3. Ative o ambiente virtual**

Mac/Linux:
```bash
source .venv/bin/activate
```

Windows:
```bash
.venv\Scripts\activate
```

**4. Instale as dependências**
```bash
pip install -r requirements.txt
```

## Configuração da chave da API

Crie um arquivo `.env` na raiz do projeto com o seguinte:

```
OPENWEATHER_API_KEY=sua_chave_aqui
```

Para obter uma chave gratuita, crie uma conta em [openweathermap.org](https://openweathermap.org/api).

## Como rodar

```bash
uvicorn main:app --reload
```

O servidor estará disponível em `http://localhost:8000`.

## Endpoints

### GET /api/weather

Retorna a previsão do tempo atual de uma cidade.

**Parâmetros**

| Parâmetro | Tipo   | Obrigatório | Descrição       |
|-----------|--------|-------------|-----------------|
| city      | string | sim         | Nome da cidade  |

**Exemplos de requisição**
```
GET http://localhost:8000/api/weather?city=London
GET http://localhost:8000/api/weather?city=São Paulo
GET http://localhost:8000/api/weather              → Quando nao houver pesquisa
GET http://localhost:8000/api/weather?city=xyzabc  → Quando digitar uma cidade inexistente
```

**Erros**

| Status | Descrição                        |
|--------|----------------------------------|
| 404    | Cidade não encontrada            |
| 422    | Parâmetro `city` não informado   |
| 502    | Erro ao consultar a API externa  |

---

### GET /api/history

Retorna o histórico das últimas cidades consultadas.

**Exemplo de requisição**
```
GET http://localhost:8000/api/history
```

## Testes

```bash
pytest tests/
```
