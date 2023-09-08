import metapy


#* Getting Started

# tell MeTa to log to stderr so you can get process output when running long-running function calls
metapy.log_to_stderr()

# Create a document
doc = metapy.index.Document()

# Add content to document
doc.content("I said that I can't believe that it only costs $19.95! I could only find it for more than $30 before.")


#* Tokenization

# Create tokenizer object 
tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
# tok = metapy.analyzers.LengthFilter(tok, min=2, max=30)
# tok = metapy.analyzers.ListFilter(tok, 'lemur-stopwords.txt', metapy.analyzers.ListFilter.Type.Reject)
# tok = metapy.analyzers.Porter2Filter(tok)
tok = metapy.analyzers.LowercaseFilter(tok)

# Set up the content for the tokenizer by using the content of the document
tok.set_content(doc.content())

# create a list of tokens given the content passed
tokens = [token for token in tok]

# look at the list of tokens created 
# print(tokens)

ana = metapy.analyzers.NGramWordAnalyzer(2, tok)
print(doc.content())
bigrams = ana.analyze(doc)
print(bigrams)

