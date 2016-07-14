#!/usr/bin/bash


for p in content/*.rst;do
    #convert structureText hyper link to ReStructureText hyper link
    sed -E -i -e 's/"(.*)":(http:\/\/([a-z]|\.|[0-9]|[A-Z]|_|&|%|#|\/|-|=|\?|~)*)/ `\1 <\2>`_ /g'  $p
    #convert <img/> html to ReStructureText image 
    sed -E -i -e 's/<img *src="(\/.*)">/\n.. image:: {filename}\/images\1\n   :align: center\n/g' $p
    sed -E -i -e 's/<img *src="(http:\/.*)">/\n.. image:: \1\n   :align: center\n/g' $p
    sed -E -i -e 's/^NULL$//g' $p
    #convert my ..sh to ..code-block
    sed -E -i -e 's/\.\. *sh/\.\. code-block/g' $p
done

for p in content/*.md;do
    #convert [url=xxx] to MD hyper format
    sed -E -i -e 's/\[url=(.*)\](.*)\[\/url\]/\[\2\]\(\1\)/g' $p
    #del NULL line
    sed -E -i -e 's/^NULL$//g' $p
done