import pandas as pd

def load_dictionary():
    dictionary = {}
    df = pd.read_excel('app/assets/dictionary_data.xlsx')
    for _, row in df.iterrows():
        english = row['English']
        tenandi = row['Tenandi']
        part_of_speech = row['PartOfSpeech']
        eng_ex = row['EnglishExample']
        ten_ex = row['TenandiExample']
        
        dictionary[tenandi] = {
            'english': english,
            'part_of_speech': part_of_speech,
            'english_example': eng_ex,
            'tenandi_example': ten_ex
        }
        
        dictionary[english] = {
            'tenandi': tenandi,
            'part_of_speech': part_of_speech,
            'english_example': eng_ex,
            'tenandi_example': ten_ex
        }

        # TODO create access point for every value in dictionary for search funtionality

    return dictionary

dictionary_data = load_dictionary()

#TESTING
result = dictionary_data.get('hello')
print(result['tenandi'])
