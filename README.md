# Desafio Python
> Desafio em python usando docker, django e com integração S3 da AWS.

1.	Container docker DB em postgres;
2.	Container docker Web em python usando django;
3.	Network para ter conexões entre ambos os container;
4.	Container Web ser dependente do DB;
5.	Integração com S3 da AWS (boto3 e django-storage);
6.	Usando migrate;
7.	Iniciando testes unitários;

## Configuração para Desenvolvimento
Ter instalado docker-compose na máquina e executar os seguinte comando:

docker-compose up -d --build (buildar o app, acesse: http://localhost:8000/app/)
docker-compose ps (verificar se está no ar)
docker exec -it web bash (executar o test: python manage.py test app)
python manage.py check (se esta tudo OKA)
python manage.py collectstatic (Subir no S3 AWS)

## Meta

Matheus Santos – [@matheusmmjs](https://www.linkedin.com/in/...) – matheusmatmac@hotmail.com

Sem licença.

[https://github.com/matheusmmjs/github-link](https://github.com/matheusmmjs/)

## Contributing

1. Faça o _fork_ do projeto (<https://github.com/matheusmmjs/python-django-S3/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_