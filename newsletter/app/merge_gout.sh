#!/bin/bash
# Usage : bash newsletter/app/merge_gout.sh <veille.md> <brut_gout.md>
# Fusionne en tête les sujets « avec du goût » et les marque 🍿.
f="$1"
r=$(python3 newsletter/app/merge_brut.py "$f" "$2" --en-tete | tail -1); echo "$r"
python3 - "$f" "$r" <<'EOF'
import re,sys,ast
p=sys.argv[1];k=ast.literal_eval(sys.argv[2].split(' ajout')[0]);t=open(p).read().split('\n');c={'R':0,'B':0,'F':0}
for i,l in enumerate(t):
    m=re.match(r'([RBF])\d+\. \*\*🆕 ',l)
    if m and c[m.group(1)]<k[m.group(1)]:
        c[m.group(1)]+=1; t[i]=l.replace('**🆕 ','**🍿 ',1)
open(p,'w').write('\n'.join(t))
EOF
