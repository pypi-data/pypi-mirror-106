# PhDictionary | Best tool for language learning

This tool can help you to provide better understanding of foreign word using examples, definitions and translation.

# Installation

```bash
pip install phdictionary
```

# Usage

Importing the module
```python
from phdictionary import dictionary
```
To get the definition of a word use this code
```python
word = input()
result = dictionary.get_definition(word, 2)
print(result)
```
This function returns a turple with the definition and examples in a sentence (in this case 2 examples)

To translate from English to French
```python
word = input()
result = dictionary.get_french_english(word, 2)
print(result)
```
And vice versa

```python
word = input()
result = dictionary.get_english_french(word, 2)
print(result)
```
These functions return a turple with the translation and examples in a sentence (in this case 2 examples)

To get synonyms to a word in English use this
```python
word = input()
result = dictionary.get_synonym(word, 4)
print(result)
```
This function returns a list with the synonyms (in this case 4 synonyms and by default it returns only one synonym)

To get definitions for the list of word use the code below
```python
dictionary.get_definition_from_file(open('file.txt'), 2)
```
It generates a Word document with definitions for the each word in list with 2 examples for each (by default it is 0)

To get synonyms for the list of word use the code below
```python
dictionary.get_synonyms_from_file(open('file.txt'), 3)
```
It generates a Word document with 3 synonyms to the each word in list (by default it is 1)

To get translation from French to English for each word in the list use this
```python
dictionary.get_french_english_from_file(open('file.txt'), 3)
```
It generates a Word document with translation for the each word in list with 3 examples for each (by default it is 0)


You can find all the documentation on GitHub: https://github.com/RediIVIideR/phdictionary