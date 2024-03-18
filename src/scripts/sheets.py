import pandas

from datetime import datetime

TWO_DIGIT_DATE_FORMAT = '%d/%m/%y'
FOUR_DIGIT_DATE_FORMAT = '%d/%m/%Y'

RESIDENT_QUESTION_RESULTS = {
    # Restrição de Mobilidade - range(3, 9)
    3: 'NÃO ANDA - RESTRITO AO LEITO',
    4: 'CADEIRANTE',
    5: 'ANDA COM AUXÍLIO DE MULETA, ANDADOR OU OUTRO SUPORTE',
    6: 'ANDA SEM SUPORTE MAS COM DIFICULDADE',
    7: 'ANDA SEM RESTRIÇÕES',
    8: 'SEM INFORMAÇÃO',
    9: 'DEFICIENTE AUDITIVO',
    10: 'DEFICIENTE VISUAL',
    11: 'SEM INFORMAÇÃO',
    12: 'SIM',
    13: 'NÃO',
    14: 'SEM INFORMAÇÃO',
    15: 'SIM',
    16: 'NÃO',
    17: 'SEM INFORMAÇÃO',
    18: 'NENHUMA',
    19: 'ENSINO FUNDAMENTAL',
    20: 'ENSINO MÉDIO',
    21: 'FACULDADE',
    22: 'SEM INFORMAÇÃO',
}

def transform_file_data(file):
    dataframe = pandas.read_excel(file, sheet_name='dados')

    forms = []
    residents = []

    for index, row in dataframe.iterrows():

        forms.append(get_current_form(row))
        residents.append(get_residents(row))

    return forms, residents
            
def get_current_form(row):
    current_form = {}

    date = row['data']
    if is_valid(date):
        
        if type(date) is datetime:
            current_form['date'] = date.date()
        if type(date) is str:
            try:
                current_form['data'] = datetime.strptime(date, TWO_DIGIT_DATE_FORMAT).date()
            except:
                current_form['data'] = datetime.strptime(date, FOUR_DIGIT_DATE_FORMAT).date()
    
    district = row['bairro pela data']
    if is_valid(district, str):
        current_form['district'] = district

    address = row['end']
    if is_valid(address, str):
        current_form['address'] = address.title()
    
    coord_s = row['coord S2']
    if is_valid(coord_s, float):
        current_form['coord_s'] = coord_s

    coord_w = row['coord W2']
    if is_valid(coord_w, float):
        current_form['coord_w'] = coord_w

    altitude = row['altitude']
    if is_valid(altitude, int):
        current_form['altitude'] = altitude

    ivge = row['IVGE']
    if is_valid(ivge, int):
        current_form['ivge'] = ivge

    ivee = row['IVEE']
    if is_valid(ivee, int):
        current_form['ivee'] = ivee
    
    return current_form

def get_residents(row):
    residents = []
    
    # Get Main Resident
    main_resident = {}

    sex = row['sexo']
    if is_valid(sex, str):
        main_resident['sex'] = sex[0].upper()
    
    age = row['idade']
    if is_valid(age, int):
        main_resident['age'] = age

    education = row['escolaridade']
    if is_valid(education, str):
        main_resident['education'] = education
        
    residents.append(main_resident)

    # Get secondary residents
    number_of_residents = row['#pessoas']

    if not is_valid(number_of_residents, int):
        return residents
    
    for resident in range(number_of_residents):
        current_resident = {}

        current_resident['mobility_restriction'] = find_marked_option(row, current_resident, resident, range(3, 9))
        current_resident['sensory_impairment'] = find_marked_option(row, current_resident, resident, range(9, 12))
        current_resident['mental_disorder'] = find_marked_option(row, current_resident, resident, range(12, 15))
        current_resident['health_injury'] = find_marked_option(row, current_resident, resident, range(15, 18))
        current_resident['education'] = find_marked_option(row, current_resident, resident, range(18, 23))

        residents.append(current_resident)

    return residents

def find_marked_option(row, current_resident, resident, option_range):
    for option_number in option_range:
        current_option = row[f'outros mor {option_number}']

        result = current_option.split("/")[resident]

        if result.lower() == 'x':
            return RESIDENT_QUESTION_RESULTS[option_number]

def is_valid(value, instance=None):
    if pandas.isnull(value):
        return False
    
    if instance and not type(value) is instance:
        return False
    
    if type(value) is str and value.startswith('#'):
        return False
    
    return True


