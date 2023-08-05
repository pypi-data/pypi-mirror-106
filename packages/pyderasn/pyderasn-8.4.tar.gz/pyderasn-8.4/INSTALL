Install
=======

Preferable way is to :ref:`download <download>` tarball with the
signature from `official website <http://www.pyderasn.cypherpunks.ru/>`__::

    $ [fetch|wget] http://www.pyderasn.cypherpunks.ru/download/pyderasn-8.4.tar.zst
    $ [fetch|wget] http://www.pyderasn.cypherpunks.ru/download/pyderasn-8.4.tar.zst.sig
    $ gpg --verify pyderasn-8.4.tar.zst.sig pyderasn-8.4.tar.zst
    $ zstd -d < pyderasn-8.4.tar.zst | tar xf -
    $ cd pyderasn-8.4
    $ python setup.py install
    # or copy pyderasn.py (+six.py, possibly termcolor.py) to your PYTHONPATH

PyDERASN depends on `six <https://pypi.org/project/six/>`__ package
for keeping compatibility with Py27/Py35. It is included in the tarball.
You can also find it mirrored on :ref:`download <download>` page.
``termcolor`` is an optional dependency used for output colourizing.
``urwid`` is an optional dependency used for :ref:`interactive browser <browser>`.

You could use pip (**no** OpenPGP authentication is performed!) with PyPI::

    $ cat > requirements.txt <<EOF
    pyderasn==8.4 --hash=sha256:TO-BE-FILLED
    six==1.16.0 --hash=sha256:1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926
    EOF
    $ pip install --requirement requirements.txt

You have to verify downloaded tarballs integrity and authenticity to be
sure that you retrieved trusted and untampered software. `GNU Privacy
Guard <https://www.gnupg.org/>`__ is used for that purpose.

For the very first time it is necessary to get signing public key and
import it. It is provided below, but you should check alternative
resources.

::

    pub   rsa2048/0x04A933D1BA20327A 2017-09-20
          2ED6 C846 3051 02DF 5B4E  0383 04A9 33D1 BA20 327A
    uid   PyDERASN releases <pyderasn@cypherpunks.ru>

    $ gpg --auto-key-locate dane --locate-keys pyderasn at cypherpunks dot ru
    $ gpg --auto-key-locate wkd --locate-keys pyderasn at cypherpunks dot ru

.. literalinclude:: ../PUBKEY.asc
