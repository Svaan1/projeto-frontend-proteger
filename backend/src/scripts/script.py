# +-----------------------------------------------------------+
# | script para remapear colunas no formato de dados aceito.  |
# | para utilizar o script, é necessário utilizar o arquivo   |
# | de referência que contém as colunas que serão remapeadas  |
# | e o arquivo com os dados que serão remapeados.            |
# |                                                           |
# | ref: 211104_dados.xlsx OU dados_protegerIIIeII.xlsx       |
# | dados: dados_protegeri.xlsx                               |
# +-----------------------------------------------------------+

import pandas as pd
import tkinter as tk
from tkinter import filedialog


def mess_up_data(col_to_parse, column_to_concat):
    for index, row in dados_proteger.iterrows():
        concatenated_values = ''

        for i in range(2, 6):  # 2 a 5, o 1 é o principal e não entra no 'outros mor'
            col_name = f'{column_to_concat} ({i})'

            if col_name in dados_proteger.columns and pd.notna(row[col_name]):
                concatenated_values += str(row[col_name]) + '/'

        num_slashes = concatenated_values.count('/')
        if num_slashes < 9:
            concatenated_values += '/' * (9 - num_slashes)

        dados_proteger.at[index, col_to_parse] = concatenated_values


def add_x_else_slash(col_val, index, col_name, target_value):

    if col_name not in dados_proteger.columns:
        dados_proteger[col_name] = ''

    if col_val == target_value.strip():
        dados_proteger.at[index, col_name] += 'X/'
    else:
        dados_proteger.at[index, col_name] += '/'


def add_x_else_slash2(col_val, index, col_name, target_values):
    has_target = False

    if col_name not in dados_proteger.columns:
        dados_proteger[col_name] = ''

    for target_value in target_values:
        if str(target_value.strip()) in str(col_val):
            has_target = True

    if has_target:
        dados_proteger.at[index, col_name] += 'X/'
    else:
        dados_proteger.at[index, col_name] += '/'

# ADICIONA X SE NÃO TIVER O TARGET


def add_x_else_slash3(col_val, index, col_name, target_values):
    has_target = False

    if col_name not in dados_proteger.columns:
        dados_proteger[col_name] = ''

    for target_value in target_values:
        if str(target_value.strip()) in str(col_val):
            has_target = True

    if not has_target:
        dados_proteger.at[index, col_name] += 'X/'
    else:
        dados_proteger.at[index, col_name] += '/'


column_mapping = {
    'bairro pela data': 'BAIRRO',
    'coord S': 'COORD S',
    'coord W': 'COORD W',
    'altitude': 'ALT (M)',
    # 'end': '', NÃO EXISTE
    # 'data': '', NÃO EXISTE
    'sexo': 'SEXO (1)',
    'idade': 'IDADE (1)',
    '#pessoas': 'Nº PESSOAS',
    'q1': 'MOBILIDADE (1)',
    'q2': 'DEFICIÊNCIA (1)',
    'q3': 'TRANST MENTAL (1)',
    'q4': 'AGRAVO (1)',
    # q5 NÃO EXISTE
    # q6 NÃO EXISTE
    'q7': 'PONTO APOIO',
    'q8': 'SIRENE - COMPORTAMENTO',
    # q9 NÃO EXISTE
    'q10': 'CONF SIRENE',
    'q11': 'CONF DCIVIL',

    # q12 a q16 NÃO EXISTEM

    # q17 ( ÁRVORES / BANANEIRAS / VEGETAÇÃO RASTEIRA / ÁREA DESMATADA / ÁREA AGRÍCOLA )
    # q18 NÃO EXISTE
    'q20-1': 'VERTICAL',
    'q20-2': 'HORIZONTAL',
    'q20-3': 'DIAGONAL',
    'q21': 'EMBARRIGADOS',
    'q22': 'DESLIZAMENTO HIST',
    'q23-1': 'ENCOSTA NATURAL',
    'q23-2': 'ALTURA ENCOSTA',
    'q23-3': 'INCLINAÇÃO ENC',
    'q24-1': 'TALUDE EM CORTE',
    'q24-2': 'TALUDE EM CORTE - ALT',
    'q24-3': 'INCLINAÇÃO ENC TAL',
    # q24-4  ( DISTÂNCIA BASE ENC TAL / DISTÂNCIA TOPO ENC TAL )
    'q25-1': 'ATERRO',
    'q25-2': 'ALTURA ATERRO',
    'q25-3': 'INCLINAÇÃO ATERRO',
    # q25-4 ( DISTÂNCIA BASE ATERRO / DISTÂNCIA TOPO ATERRO )
    'q26-1': 'PAREDE ROCHOSA',
    'q26-2': 'ALTURA PR',
    'q26-3': 'INCLINAÇÃO PR',
    'q27': 'ÁGUA DE CHUVA',
    'q28': 'ÁGUA SERVIDA',
    # q29 NÃO EXISTE
    'q30': 'CAIXA D´ÁGUA',
    'q31': 'TRANSBORDAMENTO',
    'q32': 'ÁGUA - PROCEDÊNCIA',
    'q33': 'ESGOTO',
    'q34': 'VAZAMENTO',
    # q35 NÃO EXISTE
    'q36': 'MINAS NO BARRANCO',
}


# Create the Tkinter root window
root = tk.Tk()
root.withdraw()

# Ask for file paths using a file dialog window
dados_proteger_path = filedialog.askopenfilename(
    title="Selecione o arquivo a ser remapeado")
dados_reference_path = filedialog.askopenfilename(
    title="Selecione o arquivo de referência")

# Load the Excel files
dados_proteger = pd.read_excel(dados_proteger_path)
dados_reference = pd.read_excel(dados_reference_path, sheet_name=1)

for col in dados_proteger.columns:
    dados_proteger.rename(columns={col: col.strip()}, inplace=True)

# Get column names from both files
dados_protegeri_columns = dados_proteger.columns.tolist()
dados_reference_columns = dados_reference.columns.tolist()

# Iterate over columns of dados_proteger
for protegeri_col in column_mapping.values():
    if protegeri_col in dados_protegeri_columns:
        ref_col = next(key for key, value in column_mapping.items()
                       if value == protegeri_col)
        # Rename the column in dados_protegeri DataFrame
        dados_proteger.rename(columns={protegeri_col: ref_col}, inplace=True)

mess_up_data('outros mor 1', 'SEXO')
mess_up_data('outros mor 2', 'IDADE')

for index, row in dados_proteger.iterrows():

    # q24-4 = DISTÂNCIA BASE ENC TAL + DISTÂNCIA TOPO ENC TAL
    dados_proteger.at[index, 'q24-4'] = f'{dados_proteger.at[
        index,
        'DISTÂNCIA BASE ENC TAL'
    ]}{dados_proteger.at[
        index,
        'DISTÂNCIA TOPO ENC TAL'
    ]}'

    # q25-4 = DISTÂNCIA BASE ATERRO + DISTÂNCIA TOPO ATERRO
    dados_proteger.at[index, 'q25-4'] = f'{dados_proteger.at[
        index,
        'DISTÂNCIA BASE ATERRO'
    ]}{dados_proteger.at[
        index,
        'DISTÂNCIA TOPO ATERRO'
    ]}'

    # q17 = ÁRVORES / BANANEIRAS / VEGETAÇÃO RASTEIRA / ÁREA DESMATADA / ÁREA AGRÍCOLA
    dados_proteger.at[index, 'q17'] = f'{dados_proteger.at[
        index,
        'ÁRVORES'
    ]};{dados_proteger.at[
        index,
        'BANANEIRAS'
    ]};{dados_proteger.at[
        index,
        'VEGETAÇÃO RASTEIRA'
    ]};{dados_proteger.at[
        index,
        'ÁREA DESMATADA'
    ]};{dados_proteger.at[
        index,
        'ÁREA AGRÍCOLA'
    ]}'

    for i in range(2, 6):
        if pd.notna(row[f'MOBILIDADE ({i})']):
            transt_mental = row[f'MOBILIDADE ({i})']

            add_x_else_slash(
                transt_mental,
                index,
                'outros mor 3',
                'NÃO ANDA - RESTRITO AO LEITO'
            )
            add_x_else_slash(
                transt_mental,
                index,
                'outros mor 4',
                'CADEIRANTE'
            )
            add_x_else_slash(
                transt_mental,
                index,
                'outros mor 5',
                'ANDA COM AUXÍLIO DE MULETA, ANDADOR OU OUTRO SUPORTE'
            )
            add_x_else_slash(
                transt_mental,
                index,
                'outros mor 6',
                'ANDA SEM SUPORTE MAS COM DIFICULDADE'
            )
            add_x_else_slash(
                transt_mental,
                index,
                'outros mor 7',
                'ANDA SEM RESTRIÇÕES'
            )
            add_x_else_slash(
                transt_mental,
                index,
                'outros mor 8',
                'SEM INFORMAÇÃO'
            )

        if pd.notna(row[f'DEFICIÊNCIA ({i})']):
            deficiencia = row[f'DEFICIÊNCIA ({i})']

            add_x_else_slash(
                deficiencia,
                index,
                'outros mor 10',
                'VISUAL'
            )
            add_x_else_slash(
                deficiencia,
                index,
                'outros mor 9',
                'AUDITIVA'
            )
            add_x_else_slash2(
                deficiencia,
                index,
                'outros mor 11',
                ['NÃO', 'NH', 'SEM INFORMAÇÃO']
            )

        if pd.notna(row[f'TRANST MENTAL ({i})']):
            transt_mental = row[f'TRANST MENTAL ({i})']

            add_x_else_slash(
                transt_mental,
                index,
                'outros mor 12',
                'SIM'
            )
            add_x_else_slash(
                transt_mental,
                index,
                'outros mor 13',
                'NÃO'
            )
            add_x_else_slash2(
                transt_mental,
                index,
                'outros mor 14',
                ['SEM INFORMAÇÃO', 'NH']
            )

        if pd.notna(row[f'AGRAVO ({i})']):
            agravo = row[f'AGRAVO ({i})']

            # como no agravo pode ser qualquer doença, não faz sentido ter um target específico,
            # então se não for nenhum dos valores, adiciona X na coluna de "SIM"
            add_x_else_slash3(
                agravo,
                index,
                'outros mor 15',
                ['SEM INFORMAÇÃO', 'NH', 'NÃO']
            )
            add_x_else_slash(
                agravo,
                index,
                'outros mor 16',
                'NÃO'
            )
            add_x_else_slash2(
                agravo,
                index,
                'outros mor 17',
                ['SEM INFORMAÇÃO', 'NH']
            )

        # Colunas que não existem no arquivo com os dados
        dados_proteger['outros mor obs'] = 'SEM INFORMAÇÃO'
        dados_proteger['end'] = 'endereco ficticio'
        dados_proteger['data'] = '01/01/2021'
        dados_proteger['escolaridade'] = 'SEM INFORMAÇÃO'
        dados_proteger['q5'] = 'SEM INFORMAÇÃO'
        dados_proteger['q6'] = 'SEM INFORMAÇÃO'
        dados_proteger['q9'] = 'SEM INFORMAÇÃO'
        dados_proteger['q12 A'] = 'SEM INFORMAÇÃO'
        dados_proteger['q12 B'] = 'SEM INFORMAÇÃO'
        dados_proteger['q12 C'] = 'SEM INFORMAÇÃO'
        dados_proteger['q13'] = 'SEM INFORMAÇÃO'
        dados_proteger['q14-1'] = 'SEM INFORMAÇÃO'
        dados_proteger['q14-2'] = 'SEM INFORMAÇÃO'
        dados_proteger['q14-3'] = 'SEM INFORMAÇÃO'
        dados_proteger['q14-4'] = 'SEM INFORMAÇÃO'
        dados_proteger['q14-5'] = 'SEM INFORMAÇÃO'
        dados_proteger['q14-6'] = 'SEM INFORMAÇÃO'
        dados_proteger['q14-7'] = 'SEM INFORMAÇÃO'
        dados_proteger['q14-8'] = 'SEM INFORMAÇÃO'
        dados_proteger['q14-9'] = 'SEM INFORMAÇÃO'
        dados_proteger['q15'] = 'SEM INFORMAÇÃO'
        dados_proteger['q16'] = 'SEM INFORMAÇÃO'
        dados_proteger['q18'] = 'SEM INFORMAÇÃO'
        dados_proteger['q29'] = 'SEM INFORMAÇÃO'
        dados_proteger['q35'] = 'SEM INFORMAÇÃO'
        dados_proteger['IVGE'] = 0
        dados_proteger['result - IVGE'] = 'SEM INFORMAÇÃO'
        dados_proteger['D1.3'] = 0
        dados_proteger['D9.1'] = 0
        dados_proteger['D9.2'] = 0
        dados_proteger['D10'] = 0
        dados_proteger['D14.1'] = 0
        dados_proteger['D15'] = 0
        dados_proteger['D16'] = 0
        dados_proteger['D17'] = 0
        dados_proteger['IVEE'] = 0
        dados_proteger['result - IVEE'] = 'SEM INFORMAÇÃO'
        dados_proteger['M3'] = 0
        dados_proteger['M4'] = 0
        dados_proteger['M6'] = 0
        dados_proteger['M8'] = 0
        dados_proteger['m6-i'] = 0
        dados_proteger['m6-ii'] = 0
        dados_proteger['M5-i'] = 0
        dados_proteger['M5-ii'] = 0
        dados_proteger['M5-iii'] = 0
        dados_proteger['M4-i'] = 0
        dados_proteger['M4-ii'] = 0
        dados_proteger['M4-iii'] = 0
        dados_proteger['M4-iv'] = 0
        dados_proteger['M4-v'] = 0
        dados_proteger['M3-i'] = 0
        dados_proteger['M3-ii'] = 0
        dados_proteger['M3-iii'] = 0
        dados_proteger['M3-iv'] = 0
        dados_proteger['M3-v'] = 0
        dados_proteger['m3-vi'] = 0
        dados_proteger['m3-vii'] = 0
        dados_proteger['m3-viii'] = 0
        dados_proteger['m3-ix'] = 0
        dados_proteger['m3-x'] = 0
        dados_proteger['m3-xi'] = 0
        dados_proteger['m3-xii'] = 0
        dados_proteger['m3-xiii'] = 0
        dados_proteger['m3-xiv'] = 0
        dados_proteger['m3-xv'] = 0
        dados_proteger['m3-xvi'] = 0
        dados_proteger['m3-xvii'] = 0
        dados_proteger['m3-xviii'] = 0
        dados_proteger['m3-xix'] = 0
        dados_proteger['coord S2'] = 0
        dados_proteger['coord W2'] = 0

    # vai de 3 a 22, apesar de so ter dados ate 17, eh necessario preencher ate 22
    for j in range(3, 23):
        col = f'outros mor {j}'

        if col not in dados_proteger.columns:
            dados_proteger[col] = ''

        concatenated_values = dados_proteger.at[index, col]

        # ADICIONA '/' ATÉ TER 9 BARRAS!!!
        num_slashes = concatenated_values.count('/')
        if num_slashes < 9:
            concatenated_values += '/' * (9 - num_slashes)

        dados_proteger.at[index, col] = concatenated_values

dados_proteger.to_excel(
    filedialog.asksaveasfilename(
        title="Salvar arquivo remapeado", defaultextension="xlsx", initialfile="dados_proteger"),
    sheet_name='dados',
    index=False
)
