# NER Multilanguage System

This repository contains the implementation of a simple NER System. Although the instructions were to include a language code to decide which language model to use, this implementation gets rid of this dependency, for the sake of a much simpler installation. It does not require to pre-install several language models or live download while running the script. Instead it does use a multilingual model trained by spacy.

# Installation

```
virtualenv -p python3 env
source env/bin/activate
pip install --use-deprecated=legacy-resolver -r requirements.txt 
python -m spacy download xx_ent_wiki_sm
```

# How to use the NER system

To use, in your own script you can use the following

```
from ner_system import multi_language_ner

text = "Apple is looking at buying U.K. startup for $1 billion."
entities = multi_language_ner(text)

```
