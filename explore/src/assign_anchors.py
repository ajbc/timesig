import sys, string

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_help():
    print "[q] or [quit] to exit the system"
    print "[return/enter] to move to next potential anchor"
    print "[a] to flag an anchor"

forbidden = string.ascii_lowercase

doc_filename = sys.argv[1]
anchors_filename = sys.argv[2]

anchors = set()
for line in open(anchors_filename):
    anchors.add(line.strip().lower())

doc = open(doc_filename).readlines()
for lineno in range(len(doc)):
    line = doc[lineno].strip()
    linel = doc[lineno].strip().lower()
    for anchor in anchors:
        v = linel.find(anchor)
        if v != -1 and \
            not (linel[v-1] in forbidden if v != 0 else False) and \
            not (linel[v+len(anchor)] in forbidden if v+len(anchor) < len(linel) else False):
            print "-"*80
            print str(lineno-3) + ':\t' + doc[lineno - 3].strip()
            print str(lineno-2) + ':\t' + doc[lineno - 2].strip()
            print str(lineno-1) + ':\t' + doc[lineno - 1].strip()
            print str(lineno) + ':\t' + \
                line[:v] + '\033[92m' + line[v:v+len(anchor)] + '\033[0m' + line[v+len(anchor):]
            print str(lineno+1) + ':\t' + doc[lineno + 1].strip()
            print str(lineno+2) + ':\t' + doc[lineno + 2].strip()
            print str(lineno+3) + ':\t' + doc[lineno + 3].strip()
            print "-"*80
            is_anchor = raw_input("\n> : ")
            if not is_anchor:
                print "\n\n\n"
                continue
            elif is_anchor == 'quit' or is_anchor == 'q':
                exit()
            elif is_anchor == 'a':
                print "found an anchor!"
                print "\n\n\n"
            else:
                print_help()
                is_anchor = raw_input("\n> : ")
