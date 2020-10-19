## Instalação

```
pip instal -r requirements.txt
source venv/bin/activate
```

Para pegar a lista de bairros utilize o comando abaixo alterando os dados conforme você precisa:

```
scrapy runspider spider-cep-bairros.py -a uf='PR' -a localidade='Curitiba' -a bairro='Uberaba' -o uberaba.json
```

Isso vai retornar um `json` com a seguinte estrutura:

```
[
    {"nome": "Avenida Comendador Franco - de 5011/5012 a 7264/7265\u00a0", "bairro": "Uberaba\u00a0", "cep": "81560-000"},
    {"nome": "Avenida Comendador Franco - de 7266/7267 ao fim\u00a0", "bairro": "Uberaba\u00a0", "cep": "81560-001"},
    {"nome": "Avenida Comendador Franco 5378 ", "bairro": "Uberaba\u00a0", "cep": "81570-971"}
]
```
