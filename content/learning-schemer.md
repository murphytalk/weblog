Title: Learning Scheme - atom, list and S-expression
Category: computer
Tags: scheme,lisp
Date: 2015-03-29 22:00

It looks it would be easier to go through [The Little Schemer](https://mitpress.mit.edu/books/little-schemer) first before pick up SICP, so here we go.


`atom` is the most basic building block,  it could be a letter, a string of digits, a string of characters.  Examples:


```scheme
a
1492
atom
*abc$
```


`list` is one or more atom enclosed by parentheses. Examples:


```scheme
(atom)
(atom turkey or)
((atom turkey) or)

```

All atoms and all lists are [S-expression](http://en.wikipedia.org/wiki/S-expression)s. For example, there are three S-expressions in the following example :

```scheme
(((how) are) ((you) (doing so)) far)

```

They are `((how) are)`,`((you) (doing so))` and `far`.

The `null` S-expression:

```scheme
()
```
