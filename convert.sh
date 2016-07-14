#!/usr/bin/bash

for p in content/*.rst;do
    sed -E -i -e 's/"(.*)":(http:\/\/([a-z]|\.|[0-9]|[A-Z]|_|&|%|#|\/|-|=|\?|~)*)/ `\1 <\2>`_ /g'  $p
done