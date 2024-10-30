import sqlite3 as sq
import pandas as pd

def criarBanco():
    conn = sq.connect('./Banco.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS JOGO(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME TEXT NOT NULL,
            CORXPAL TEXT NOT NULL,
            VITXCOR TEXT NOT NULL,
            CORXCRU TEXT NOT NULL,
            CORXVAS TEXT NOT NULL,
            CRIXCOR TEXT NOT NULL,
            CORXBH TEXT NOT NULL,                    
            GRXCOR TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def inserirBanco(nome, jogo1, jogo2, jogo3, jogo4, jogo5, jogo6, jogo7):
    conn = sq.connect('Banco.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO JOGO (NOME, CORXPAL, VITXCOR, CORXCRU, CORXVAS, CRIXCOR, CORXBH, GRXCOR) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, jogo1, jogo2, jogo3, jogo4, jogo5, jogo6, jogo7))
    conn.commit()
    conn.close()

def selectBanco():
    conn = sq.connect('Banco.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM JOGO')
    rows = cursor.fetchall()
    conn.close()
    
    apostas = []
    for row in rows:
        id_, nome, jogo1, jogo2, jogo3, jogo4, jogo5, jogo6, jogo7 = row
        apostas.append({
            'ID': id_,
            'Nome': nome,
            'CORXPAL': jogo1,
            'VITXCOR': jogo2,
            'CORXCRU': jogo3,
            'CORXVAS': jogo4,
            'CRIXCOR': jogo5,
            'CORXBH': jogo6,
            'GRXCOR': jogo7
        })
    return apostas

criarBanco()
