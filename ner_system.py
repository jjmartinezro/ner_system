import spacy

def multi_language_ner(text):
    nlp = spacy.load("xx_ent_wiki_sm")
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append({
            'text': ent.text,
            'type': ent.label_,
            'start_pos': ent.start_char,
            'end_pos': ent.end_char
        })
    return entities

if __name__ == "__main__":
    text_en = "Apple is looking at buying U.K. startup for $1 billion."
    entities_en = multi_language_ner(text=text_en)

    print('english language entities: ', entities_en)

    text_es = "Apple está considerando comprar una startup de Inglaterra por 1 millón de libras esterlinas."
    entities_es = multi_language_ner(text=text_es)

    print('spanish language entities: ', entities_es)
