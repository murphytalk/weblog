#!/usr/bin/bash


for p in content/*.rst;do
    #convert structureText hyper link to ReStructureText hyper link
    sed -E -i -e 's/"(.*)":(http:\/\/([a-z]|\.|[0-9]|[A-Z]|_|&|%|#|\/|-|=|\?|~)*)/ `\1 <\2>`_ /g'  $p
    #convert <img/> html to ReStructureText image 
    sed -E -i -e 's/<img *src="(\/.*)">/\n.. image:: {filename}\/images\1\n   :align: center\n/g' $p
    sed -E -i -e 's/<img *src="(http:\/.*)">/\n.. image:: \1\n   :align: center\n/g' $p
done
