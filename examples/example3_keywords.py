from wostabfile.core import WosTabFile
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

root_path = "data/social network"
wos_fields = ["DE"]
wtf = WosTabFile(file_path=root_path)
dict_words={}

def singularize(text):
    wnl = WordNetLemmatizer()
    tokens = [token.lower() for token in word_tokenize(text)]
    lemmatized_words = [wnl.lemmatize(token) for token in tokens]
    return (' '.join(lemmatized_words)).strip()

def process_row(rows):
    global dict_words
    for ks in rows:
        wlist=ks[0]
        for w in wlist.split(";"):
            w=w.strip()
            if w=="":
                continue
            w=singularize(w)
            if w not in dict_words.keys():
                dict_words[w]=1
            else:
                dict_words[w]+=1

table = wtf.generate_table_by_folder(wos_fields,func=process_row)
dict_words =  dict(sorted(dict_words.items(),reverse=True, key=lambda item: item[1]))

print("Word\tTerm Count")
for k in list(dict_words.keys())[:20]:
    print(f'{k}\t{dict_words[k]}')
print()
print("Number of unique words: ",len(dict_words.keys()))