#importando biblioteca pandas
import pandas as pd

#aplicando a leitura e escolhendo o arquivo
dataframe = pd.read_excel("./pessoas.xlsx")

#imprimindo a tabela
print(f'\nTodos os dados: \n {dataframe}\n')