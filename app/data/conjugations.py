import pandas as pd

def load_conjugations():
    conjugations = {}
    df = pd.read_excel('app/assets/conjugation_data.xlsx')
    for _, row in df.iterrows():
        eng_inf = row['EnglishInfinitive']
        eng_pres = row['EnglishPresent']
        eng_past = row['EnglishPast']
        eng_fut = row['EnglishFuture']
        eng_pres_pt = row['EnglishPresentParticle']
        eng_past_pt = row['EnglishPastParticle']
        ten_inf = row['TenandiInfinitive']
        ten_pres = row['TenandiPresent']
        ten_past = row['TenandiPast']
        ten_fut = row['TenandiFuture']
        ten_pres_pt = row['TenandiPresentParticle']
        ten_past_pt = row['TenandiPastParticle']

        conjugations[eng_inf] = {
            
        }
        conjugations[eng_past] = {
            'tenandi_past': ten_past
        }
        # TODO create access point for every value in conjugations for search functionality

    return conjugations

conjugation_data = load_conjugations()

# TESTING
