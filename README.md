# 📰 NYT Data Pipeline (em construção)

Este projeto é um pipeline de dados em desenvolvimento que extrai informações da API do New York Times, transmite via Kafka e processa com Apache Spark, salvando os resultados em arquivos Parquet.

> ⚠️ **Status**: Em construção — ainda não está finalizado. Algumas partes estão funcionando, mas o projeto está em fase de testes e melhorias.

---

## 📦 Visão geral

Este pipeline realiza:

1. **Extração de dados** da [API do New York Times](https://developer.nytimes.com/)
2. **Envio dos dados** para o Apache Kafka usando um Producer em Python
3. **Processamento em tempo real** com Apache Spark Structured Streaming
4. **Armazenamento dos dados** transformados em formato Parquet

---

## 🧰 Tecnologias utilizadas

- Python 3.11
- Apache Kafka
- Apache Spark 3.5.0
- Docker & Docker Compose
- PyArrow + Pandas (para leitura dos dados gerados)
- Kafka UI (para monitoramento dos tópicos)

