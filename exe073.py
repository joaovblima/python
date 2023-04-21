'''tabela_premier = ("Arsenal", "Manchester City", "Manchester United", "NewCastle", "Tottenham", "Aston Villa", "Brighton & Hove Albion"
, "Liverpool", "Brentford", "Fulham", "Chelsea", "Crystal Palace", "Wolverhampton", "Bournemouth", "West Ham", "Leeds United", "Everton")
'''
tabela_premier = ("Arsenal", "Manchester City", "Manchester United", "NewCastle", "Tottenham", "Aston Villa", "Brighton & Hove Albion"
, "Liverpool", "Brentford", "Fulham", "Chelsea", "Crystal Palace", "Wolverhampton", "Bournemouth", "West Ham", "Leeds United", "Everton")
print("-="*15)
print(f"Essa é atualmente a tabela de classificação da Premier league:\n",  {tabela_premier})
print("-="*15)
print(f"Os 5 primeiros colocados são: {tabela_premier[0:5]}.")
print("-="*15)
print(f"Os 4 ultimos colocados são {tabela_premier[13:18]}")
print("-="*15)
print("Aqui está a tabela organizada em ordem alfabética:\n", (sorted(tabela_premier)))