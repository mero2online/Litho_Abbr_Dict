import re
from Dict import wordsFromDict, specialWordsFromDict

matchedWords = {}
misMatchedWords = []


def splitText(str, words, specialWordsDic):
    misMatchedWords.clear()
    # clean string
    strTwo = replace_all(str, specialWordsDic)
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


def replaceWords(words=dict, text=str, specialWordsDic=dict):
    text = replace_all(text, specialWordsDic)
    keys = words.keys()
    for i in keys:
        text = re.sub(rf'\b{i}\b', words[i], text)

    finalText = replace_all(text, specialWordsDic)
    matchedWords.clear()
    return finalText


def convertText(text, dicToUse):
    wordsFromDictReverted = {v: k for k, v in wordsFromDict.items()}
    wordsDic = wordsFromDict if dicToUse == 'FROM_ABBR' else wordsFromDictReverted

    specialWordsFromDictReverted = {
        v: k for k, v in specialWordsFromDict.items()}
    specialWordsDic = specialWordsFromDict if dicToUse == 'FROM_ABBR' else specialWordsFromDictReverted

    splitText(text, wordsDic, specialWordsDic)
    if len(misMatchedWords) > 0:
        return misMatchedWords
    finalText = replaceWords(matchedWords, text, specialWordsDic)
    print(finalText)
    return finalText


def replace_all(text=str, dic=dict):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text
