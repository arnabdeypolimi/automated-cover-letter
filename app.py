import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-c', type=str)
parser.add_argument('-l', type=str)
parser.add_argument('-t', type=str)
parser.add_argument('-s', type=str)
args=parser.parse_args()

with open("coverletter_new.tex","r") as file:
    text_file=file.read()
company=str(args.c)
location=str(args.l)
title=str(args.t)
sentence=str(args.s)

kv={'company_name':company, 'company_location':location, 'job_title':title, 'sentence':sentence}

for key, value in kv.items():
    text_file=text_file.replace('$'+key+'$',value)

output_name=kv['company_name']+'_cover.'
with open(output_name+'tex',"w") as f:
    f.write(text_file)

cmd='xelatex '+output_name+'tex'
os.system(cmd)
ls=['log','aux','tex','out']
for l in ls:
    os.remove(output_name+l)