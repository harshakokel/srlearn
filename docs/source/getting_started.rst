###############
Getting Started
###############

1. Prerequisites
----------------

- Java (1.8)
- Python (3.6, 3.7)

Windows
'''''''

Exact steps may depend on your setup. The steps here assume `Windows Terminal <https://www.microsoft.com/en-us/p/windows-terminal-preview/9n0dx20hk701>`_ and
`Chocolatey <https://chocolatey.org/>`_ are installed.

Open the Windows Terminal in Administrator mode. Use Chocolatey to install a Java Development Kit.

.. code-block:: console

    choco install openjdk

MacOS / Linux
'''''''''''''

Ubuntu:

.. code-block:: bash

    sudo apt-get install openjdk-8-jdk

`Jenv <https://www.jenv.be/>`_ might be a helpful way to manage Java versions as well.
If you're on MacOS it's also fairly easy to set up with Homebrew.

2. Installation
---------------

The package can be installed from the Python Package Index (PyPi) with ``pip``.

.. code-block:: python

    pip install srlearn

3. Test Installation
--------------------

Do a sanity check by importing ``srlearn``:

.. code-block:: console

    $ python
    >>> import srlearn

If you've reached this point, you should be ready for the `User Guide <user_guide.html>`_.
