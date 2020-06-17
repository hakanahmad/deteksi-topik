def clean_tweet(text):
    text = text.strip().lower()
    text = re.sub('((https?://[^\s]+)|(www\.[^\s]+))','',text)
    text = re.sub('@[^\s]+','',text)
    text = re.sub(r'#([^\s]+)',r'',text)
    pattern = re.compile(r'(.)\1{1,}',re.DOTALL)
    text = pattern.sub(r'\1\1',text)
    text = re.sub('[0-9]','',text)
    text = re.sub('[\s]+',' ',text)
    tokenizer = re.compile(r'(?u)\b\w\w+\b')
    token = []
    for tex in tokenizer.findall(text):
        if (tex not in stopword and len(tex)>=3):
            token.append(tex)
        else:
            continue
    text = ' '.join(token)
    return text