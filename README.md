python.org
==========

[![Build Status](https://next.travis-ci.com/proevo/pythondotorg.png?token=rzZWMj7qjjfKoW211CMz&branch=master)](https://next.travis-ci.com/proevo/pythondotorg)

The new python.org!

Getting going
-------------

Requires :sparkles:Python 3.3!:sparkles: (`brew install python3`)

You'll want a virtualenv. Python 3.3 actually includes virtualenv built-in,
so you can do:

    $ pyvenv-3.3 <env>
    $ source <env>/bin/activate
    (etc)

But you can also use your existing virtualenv/wrapper:

    $ mkvirtualenv --python=python3.3 <env>

And then it's the standard:

    $ pip install -r requirements.txt
    $ ./manage.py syncdb

You may need to specify the pip version, even with the virtualenv activated:

    $ pip-3.3 install -r requirements.txt

This expects a local database named "python.org". If you need to change it:

    $ export DATABASE_URL=postgres://user:pass@host:port/dbname

### Python 3.3 and OSX 10.8.2

Homebrew's recipe for python3.3 has some difficulty installing distribute 
and pip in a virtualenv. The [python.org installer for OSX](http://www.python.org/download/) 
may work better, if you're having trouble.

Running tests
-------------

Install `coverage` (`pip install coverage`), then::

    $ coverage run manage.py test
    $ coverage report

Generate an HTML report with `coverage html` if you like.

Compiling stylesheets
---------------------

To compile the stylesheets, you will need compass (`gem install compass`). Then:

    $ compass compile static
