import metapy

seq = metapy.sequence.Sequence()

for word in ["The", "dog", "ran", "across", "the", "park", "."]:
    seq.add_symbol(word)

print(seq)

tagger = metapy.sequence.PerceptronTagger("perceptron-tagger/")
tagger.tag(seq)
print(seq)