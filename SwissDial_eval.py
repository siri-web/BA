import json
from collections import defaultdict

counter = {'ch_sg_words': 0, 'ch_sg_unique': set(), 'ch_sg_utterances': 0,
           'ch_be_words': 0, 'ch_be_unique': set(), 'ch_be_utterances': 0,
           'ch_gr_words': 0, 'ch_gr_unique': set(), 'ch_gr_utterances': 0,
           'ch_zh_words': 0, 'ch_zh_unique': set(), 'ch_zh_utterances': 0,
           'ch_vs_words': 0, 'ch_vs_unique': set(), 'ch_vs_utterances': 0,
           'ch_bs_words': 0, 'ch_bs_unique': set(), 'ch_bs_utterances': 0,
           'ch_ag_words': 0, 'ch_ag_unique': set(), 'ch_ag_utterances': 0,
           'ch_lu_words': 0, 'ch_lu_unique': set(), 'ch_lu_utterances': 0}
character_counter = {'ch_sg': defaultdict(int), 'ch_be': defaultdict(int), 'ch_gr': defaultdict(int),
                     'ch_zh': defaultdict(int), 'ch_vs': defaultdict(int), 'ch_bs': defaultdict(int),
                     'ch_ag': defaultdict(int), 'ch_lu': defaultdict(int)}
unqiue_overall = set()



with open('sentences_ch_de_transcribed.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

for sentence in data:
    for dialect, transcription in sentence.items():
        if dialect + '_words' in counter.keys():
            words = transcription.split()
            counter[dialect + '_words'] += len(words)
            counter[dialect + '_unique'].update(words)
            counter[dialect + '_utterances'] += 1
            unqiue_overall.update(words)
            for character in transcription:
                character_counter[dialect][character] += 1


for key, value in counter.items():
    if type(value) == set:
        counter[key] = len(value)

print(counter)
print(len(unqiue_overall))
print("\n")
for key, value in character_counter.items():
    print(key, len(value.keys()), sum(value.values()))
