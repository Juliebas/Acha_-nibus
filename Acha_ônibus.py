import requests
import pandas as pd

JAN = [[i] for i in range (1, 32)]
FEV = [[i] for i in range (1, 30)]
MAR = [[i] for i in range (1, 32)]
ABR = [[i] for i in range (1, 31)]
MAI = [[i] for i in range (1, 32)]
JUN = [[i] for i in range (1, 31)]

MES = [JAN, FEV, MAR, ABR, MAI, JUN]

df = pd.DataFrame(columns=["Data","Grupo","Lote", "Empresa", "Linha", "Passageiros", "Pagtes Em Dinheiro", "Passageiros Comum e VT", "Passageiros Pgts Bu Comum M", "Passageiros Pagtes Estudante", "Passageiros Pgts Bu Est Mensal	Passageiros Pgts Bu Vt Mensal", "Passageiros Pagantes", "Passageiros Int Ônibus->Ônibus	Passageiros Com Gratuidade", "Passageiros Com Gratuidade Est", "Tot Passageiros Transportados"])

for j in MES:
    for i in j:
        if j == JAN:
            m = "JAN"
        if j == FEV:
            m = "FEV"
        if j == MAR:
            m = "MAR"
        if j == ABR:
            m = "ABR"
        if j == MAI:
            m = "MAI"
        if j == JUN:
            m = "JUN"
        link = f"https://www.prefeitura.sp.gov.br/cidade/secretarias/upload/{str(i[0]).zfill(2)}{m}2024.xls"
        print(link)
        df1 = pd.read_excel(link)
        print(df1)
        coluna = df1[df1["Linha"] == "802210 - CID UNIV/METRO BUTANTA"]
        df.insert(coluna)
        print(df)


