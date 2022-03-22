import re
from Dict import wordsFromDict

matchedWords = {}
misMatchedWords = []


def splitText(str, words):
    misMatchedWords.clear()
    # clean string
    strTwo = str.replace('-', ' ').replace('in part', 'in_part')
    pat = re.compile(r'[^a-zA-Z /_]+')
    str = re.sub(pat, '', strTwo)
    print(str)
    # split string
    splits = str.split()

    # for loop to iterate over words array
    for split in splits:
        lowerSplit = split.lower()
        if lowerSplit in words:
            matchedWords[split] = words[lowerSplit].upper(
            ) if split.isupper() else words[lowerSplit].title() if split.istitle() else words[lowerSplit]
        else:
            misMatchedWords.append(split)
    print(matchedWords)
    print(misMatchedWords)


def replaceWords(words, text):
    text = text.replace('in part', 'in_part')

    keys = words.keys()
    for i in keys:
        text = text.replace(i, words[i])
        text = text.replace('-', ' ')

    text = text.replace('_', ' ')
    matchedWords.clear()
    return text


def convertText(text, dicToUse):
    wordsFromDictReverted = {v: k for k, v in wordsFromDict.items()}
    wordsDic = wordsFromDict if dicToUse == 'FROM_ABBR' else wordsFromDictReverted
    splitText(text, wordsDic)
    if len(misMatchedWords) > 0:
        return misMatchedWords
    text = replaceWords(matchedWords, text)
    print(text)
    return text
