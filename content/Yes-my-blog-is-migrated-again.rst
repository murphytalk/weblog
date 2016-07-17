===============================
Yes - my blog is migrated again
===============================
:category: Computer
:tags: Python, Memo
:date: 2016-07-17 01:36:57

First of all, let me count how many times this had already happened ...

#. At the very beginning, it was running on `Plone <https://plone.org/>`_
#. In `2005 </posts/2005/12/13/cong-ploneqian-yi-blogshu-ju-wan-bi/>`_ , I bumped into a simple Python web framework called "snakelets"; its author also used it to write a blog system called "frog" (of course he is playing with the names). I liked its simplicity, enhanced it to use marking syntax `StructuredText <https://wiki.python.org/moin/StructuredText/MarkUp>`_ , which was used in my original Plone site. To export the data, I didn't bother to invest time to learn Plone/Zope's API, but wrote a crawler.
#. In `2006 </posts/2006/09/23/this-site-is-powered-by-django-now>`_, it was migrated to  `Django <https://www.djangoproject.com>`_ , which was a rising star at that time. Actually author of Snakelets later said that he himself was switching to Django. I stayed with Django for quite a while, during which I added `restructuredText <http://docutils.sourceforge.net/rst.html>`_ as the new marking syntax, and wrote a directive to support `code syntax highlighting   </posts/2008/01/25/kuo-zhan-docutils>`_ .
#. In `2010 </posts/2010/08/31/blog-ported-to-gae/>`_ , it was migrated to Google App Engine. Yes this was when cloud computing becoming a buzz word ... Upgraded along with GAE for several times.
#. In 2015 I gave Github pages a try, was using `Jekyll <https://jekyllrb.com/>`_ , but did not grow enough interest to fully migrate this site.

Although I did not like Jekyll, I did get interested in the idea of static websites. Then I discovered `Pelican <http://docs.getpelican.com/>`_ , Python's answer to Jekyll, and I liked it. Meanwhile I keep feeling insecure about my data being hidden inside GAE's data store, finally I was motivated enough to write `a small script <https://bitbucket.org/murphytalk/murphylog/src/3fd9241773e97c366b5c03cb15221b350d5ed680/api.py?fileviewer=file-view-default>`_ to download all data from GAE, and started the migration. The other major reason behind this is because with a plugin, Pelican makes it easy to integrate the ipython notebooks [1]_.

So now I use Emacs to write post (wrote a small e-lisp function to automatically populate the meta data), and after my post is pushed to github, the changes will be detected by `Travis CI <https://travis-ci.org/>`_ [2]_, and get built and published automatically :) Not too shabby, isn't it ?

.. [1] Ipython notebook is rendered to use light background color for code snippet, but that does not work well with my theme. The rendered HTML has CSS embedded in it, which makes it very hard to change the style if not impossible. I ended up with a  picece of JavaScript to override the background color.


.. [2] Travis CI only has permission to use git protocol to access the repo you enabled. If there is submodule then it can only use HHTPS to access them. If you don't what to keep using git protocol in the sub models, you can configure Travis to A) disable default git submodule update B) use sed to replace git with HTTPS in submodule file and then C) git submodule update 
