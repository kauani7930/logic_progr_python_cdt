import json

Frutas = { 
    'frutas' : 
        { 
            "frutas": "Maça",
            "preco": 2.23,
        }, 
            "frutas": "banana",
            "preco": 1.53,
        },




with open ('frutas.json' , 'w', encoding='utf-8') as arquivos:
    json.dump(frutas,arquivo, indent=8, ensure_ascii=False)
      