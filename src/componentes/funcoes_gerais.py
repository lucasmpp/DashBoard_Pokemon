def filtragem(dados, tipo, geracao, lendario):
  todos_tipo = dados.type1.unique()
  todos_ger = dados.generation.unique()
  todos_leg = dados.is_legendary.unique()

  tipo = tipo or todos_tipo
  geracao = geracao or todos_ger
  lendario = lendario or todos_leg

  dados = dados[(dados['type1'].isin(tipo)) | (dados['type2'].isin(tipo))]
  dados = dados[dados.generation.isin(geracao)]
  dados = dados[dados.is_legendary.isin(lendario)]

  return dados, tipo