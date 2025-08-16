import requests
from datetime import datetime, timedelta
from confluent_kafka import Producer
import json

api_key = 'SENHA'
start_date = datetime(2025, 7, 14)
end_date = datetime(2025, 7, 16)

# Configurações do Kafka
conf = {'bootstrap.servers': 'kafka1:29092,kafka2:29093,kafka3:29094'}
producer = Producer(conf)

current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime('%Y-%m-%d')
    url = f"https://api.nytimes.com/svc/books/v3/lists/overview.json?published_date={date_str}&api-key={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        # Iterar sobre as listas e os livros para enviar cada um individualmente
        for lista in data['results']['lists']:
            for book in lista['books']:
                # Mapear os campos da API para o formato esperado pelo Spark
                livro = {
                    "rank": book['rank'],
                    "title": book['title'],
                    "author": book['author'],
                    "publisher": book['publisher'],
                    "weeks_on_list": book['weeks_on_list'],
                    "description": book['description'],
                    "isbn13": book['primary_isbn13'],
                    "amazon_url": book['amazon_product_url'],
                    "book_image": book['book_image']
                }
                
                # Converter o dicionário do livro para JSON e enviar
                mensagem_json = json.dumps(livro).encode('utf-8')
                producer.produce('nyt-books', value=mensagem_json)
                
        print(f"Dados do dia {date_str} enviados ao Kafka com sucesso!")
    else:
        print(f"Erro em {date_str}: {response.status_code}")
    
    current_date += timedelta(days=1)

producer.flush()
print("Todos os dados foram enviados ao Kafka com sucesso!")
