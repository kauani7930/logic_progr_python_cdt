# import json

# json_string = """[

# {
# "nome_serie" : "Amor da minha vida",
# "lançada" : "22 de novembro de 2024",
# "temporadas" : "1 temporada",
# "episódios" : "10 episódios",
# " Asssistir" : "disney"
# },
# {
# "nome_serie" : "Bem-vindos ao Éden",
# "lançada" : " 6 de maio de 2022",
# "temporadas" : "2 temporadas",
# "episódios" : "10 episódios",
# " Asssistir" : "netflix"
# },
# {
# "nome_serie" : "Euphoria",
# "lançada" : "  16 de junho de 2019",
# "temporadas" : "2 temporadas",
# "episódios" : "10 episódios",
# " Asssistir" : ": HBO, Disney+ Hotstar, OSN"
# }
# ]

# """

import json

dados = {'nome' : 'Joao Silva','idade':30,'cidade':'Sao paulo','servico':'premium'}

json_string = json.dump(dados)

print(json_string)