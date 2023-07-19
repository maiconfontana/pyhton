import pandas as pd
import re

# Carregando os dados. Supomos que seus dados estejam em um arquivo Excel (.xlsx).
df = pd.read_excel('clientes.xlsx')

# Definindo as expressões regulares para email e telefone.
email_regex = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
phone_regex = r"\(\d{2}\) \d{4,5}-\d{4}"

# Criação de conjuntos para armazenar emails e telefones únicos.
emails = set()
phones = set()

# Iterando através de cada linha do DataFrame.
for _, row in df.iterrows():
    
    # Para a coluna Email.
    if pd.notnull(row['Email']):
        for email in re.findall(email_regex, row['Email']):
            # Adicionando o email em minúsculas ao conjunto.
            emails.add(email.lower())
    
    # Para as colunas de Telefone.
    for phone_col in ['Telefone comercial', 'Telefone celular', 'Telefone']:
        if pd.notnull(row[phone_col]):
            for phone in re.findall(phone_regex, row[phone_col]):
                phones.add(phone)

# Convertendo os conjuntos para DataFrames e salvando como arquivos Excel.
emails_df = pd.DataFrame(list(emails), columns=['Emails'])
emails_df.to_excel('emails_unicos.xlsx', index=False)

phones_df = pd.DataFrame(list(phones), columns=['Telefones'])
phones_df.to_excel('telefones_unicos.xlsx', index=False)
