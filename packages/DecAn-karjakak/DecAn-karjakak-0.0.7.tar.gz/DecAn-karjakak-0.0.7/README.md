# DecAn
## Tool to Analyze and Deconstruct chars in a text
### [Under-Development]

## Installation
```
pip install DecAn-karjakak
```
## Usage
**For analyzing text file or sentences**
```Console
decan -a path\text.txt 
```
**For search chars or words in text file or sentences**
```Console
decan -a "The Best is yet to come, yeayyy!!!" -s "Best" e y

# result:
"Best": {1: ((4, 8),)}
"Best" is 1 out of total 7 words!

'e': {5: (2, 5, 13, 22, 26)}
'e' is 5 out of total 34 chars!

'y': {5: (12, 25, 28, 29, 30)}
'y' is 5 out of total 34 chars!
```
**For Deconstruct text file or sentences to json file**
```Console
# The text file, save as json filename, and save to a directory path.
decan -d path\text.txt text path\dir 
```
**For Constructing the deconstructed text that save in json file**
```Console
decan -c path\text.json
```
## Note
* **Still development process**

