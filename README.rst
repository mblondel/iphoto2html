.. -*- mode: rst -*-

iphoto2html
===========

Generate a static html gallery for your iPhoto library.

Usage
-----

To generate static html files for your iPhoto library, type::

    iphoto2html ~/Pictures/iPhoto\ Library/

This will generate an `html/` folder in your iPhoto library.  To visualize the
result, just open up `~/Pictures/iPhoto\ Library/html/index.html` in a web
browser.

By design, all images in the generated html use relative paths. This means that
you can **backup** your iPhoto library to an external hard drive or to a remote
server and the static html gallery will still work.

By default, clicking on thumbnails in the gallery will display master copies of
the pictures. Since pictures can easily reach 3 MB or more, pictures will be
slow to load if you intend to share the html gallery over Internet. To solve
this problem, you may alternatively generate the gallery with the `--dresize`
(dynamic resize) option, as follows::

    iphoto2html ~/Pictures/iPhoto\ Library/ --dresize

When using this option, pictures will be dynamically resized on the server
side.  This requires PHP with the GD module installed on the server.

Installation
------------

To install iphoto2html from pip, type::

    pip install https://github.com/mblondel/iphoto2html/archive/master.zip

To install iphoto2html from source, type::

  git clone https://github.com/mblondel/iphoto2html.git
  cd iphoto2html
  sudo python setup.py install


Dependencies
------------

Python 2.7

License
-------

Apache 2.0

Author
------

Mathieu Blondel, 2014

Google Inc., 2010 (`phoshare <https://code.google.com/p/phoshare/>`_ project)
