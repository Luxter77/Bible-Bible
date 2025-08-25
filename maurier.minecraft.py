import json, pprint, os, textwrap, glob, math

from tqdm.auto import tqdm

word = "Bible"

TARGET = ".\\books\\"
PROB_SIZE_MOD = 1.5
SPLITTER_ARGS = {
    "width":                20,
    "tabsize":              4,
    "fix_sentence_endings": True,
    "break_long_words":     True,
    "replace_whitespace":   True,
    # here
    "initial_indent":       '',
    "subsequent_indent":    '',
    "expand_tabs":          True,
    "drop_whitespace":      True,
    "break_on_hyphens":     True,
    "max_lines":            None,
    "placeholder":          ' [...]'
}

def chunks(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def paginate(bookc: list) -> list:
    return [ 
        str("{\"text\":\""+ ('\\n'.join(page).replace('  ', ' ').replace('\n', '')) + "\"}") for page in chunks(
            lst = sum( [ textwrap.wrap(bcc, **SPLITTER_ARGS) for bcc in bookc ], list() ),
            n   = 14
            ) ]

[os.remove(f) for f in glob.glob(TARGET + '*.json')]

a = [ f'{line}\\n' for line in open(f"{word}_bible.txt", mode="r", encoding="utf-8").read().split(' \n') if (word.lower() in line.lower())]

for count, book in enumerate(tqdm(chunks(lst=a, n=int(math.sqrt(len(a))/PROB_SIZE_MOD)))):
    o = {
        "author": "Spam Co.",
        "title": f"La Santa {word} Bibla, Tomo °{count + 1}",
        "display": {
            "Lore": [f"La {word} Biblia es una colección o recopilación de libros sagrados, que contiene las historias, doctrinas, códigos y tradiciones que orientan a los {word}-anos, con base en la tradición {word}uria (Antiguo {word}-mento) y el anuncio del Evangelio (Nuevo {word}-mento)."]
            },
        "pages": paginate(book)
    }

    json.dump(o, open(TARGET + f'Holly_{word}_Bible_Volume_{count + 1}.json', 'w', encoding='utf-8'), indent=4)

print(o)
print(count)
