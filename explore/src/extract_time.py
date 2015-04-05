import sys, re, os
from os.path import join

doc_dir = sys.argv[1]
anchors_filename = sys.argv[2]
out_filename = sys.argv[3]

anchors = set()
for line in open(anchors_filename).readlines()[1:]:
    anchors.add(line.strip().split(',')[0].lower())

out = open(out_filename, 'w+')
out.write("doc,index,anchor\n")

for doc_filename in os.listdir(doc_dir):
    docname = doc_filename.split('.')[0]
    doc_filename = join(doc_dir, doc_filename)
    doc = open(doc_filename).read()
    doc = re.sub(r'-', '', doc)
    doc = re.sub(r'\'', '', doc)
    doc = re.sub(r'[^A-Za-z ]', ' ', doc)
    doc = re.sub(r' +', ' ', doc)

    word_count = 0
    for word in doc.split(' '):
        word_count += 1
        if word.lower() in anchors and word!='may' and word!="march":
            out.write("%s,%d,%s\n" % (docname, word_count, word.lower()))
out.close()
