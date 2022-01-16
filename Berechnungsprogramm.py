#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

df = pd.read_csv("/Users/rea/Documents/ProgrammLotti/Stundentabelle.csv",sep=";")


Schüler = [x.strip() for x in df["Schüler"].unique()]
Lehrer = [x.strip() for x in df["Lehrer"].unique()]
Schüler_Min_Betrag = 19.50/60
Lehrer_Min_Betrag = 10/60 
# Schüler in neuen DataFrame
Minuten_ges = list()
Betrag_ges = list()

Minuten_ges_l = list()
Betrag_ges_l = list()

# Minuten gesamt
for s in Schüler:
    Min_ges = sum(df["Dauer_min"].where(df["Schüler"] == s.strip()).dropna())
    Minuten_ges.append(Min_ges)
    Bet_ges = Min_ges * Schüler_Min_Betrag
    Betrag_ges.append(Bet_ges)


# neuer Dataframe
Schüler_df = pd.DataFrame(Schüler, columns=["Schüler"])
Schüler_df["Minuten_ges"] = Minuten_ges
Schüler_df["Betrag_ges"] = Betrag_ges

Schüler_df = Schüler_df.set_index("Schüler")

# Schüler_df in csv_Datei, automatische Erstellung in Zielordner

Schüler_df.to_csv("./Schüler.csv")

# Lehrer in neuen DataFrame
for l in Lehrer:
    Min_ges = sum(df["Dauer_min"].where(df["Lehrer"] == l.strip()).dropna())
    Minuten_ges_l.append(Min_ges)
    Bet_ges = Min_ges * Schüler_Min_Betrag
    Betrag_ges_l.append(Bet_ges)


# neuer Dataframe
Lehrer_df = pd.DataFrame(Lehrer, columns=["Lehrer"])
Lehrer_df["Minuten_ges"] = Minuten_ges_l
Lehrer_df["Betrag_ges"] = Betrag_ges_l
Lehrer_df =Lehrer_df.set_index("Lehrer")

# Lehrer_df in csv_Datei, automatische Erstellung in Zielordner
Lehrer_df.to_csv("./Lehrer.csv")





