=======
syncfat
=======

A dodgy ripoff of ``rsync`` for my music files.
MTP mounts have been very flakey for me in the past.
FAT32 and exFAT filesystems have restrictions on what filenames are allowed.
This combination makes transferring music to my phone difficult.

This script helps. It takes care of munging filenames appropriately,
checking if a file needs updating in case of a partial or failed transfer,
and copying only subsets of your library.
If a file already exists at the destination with the same file size, it will not copy.

To copy the contents of 'Zechs Marquise/Getting Paid/' and 'Grails/' from your
music library to your mounted phone:

.. code-block:: sh

    $ syncfat --source $HOME/Music \
            --destination /mnt/phone/Music \
           'Zechs Marquise/Getting Paid/' \
           'Grails/'

The source defaults to ``pwd``. This script works best when you are in the
source directory, as you can leave off the source and tab-complete files to
copy:

.. code-block:: sh

    $ cd $HOME/Music
    $ syncfat --destination /mnt/phone/Music \
           'Zechs Marquise/Getting Paid/' \
           'Grails/'

This never deletes files, and should not be used for transferring back to
your music library. It is designed specifically for transferring to
intermittent FAT devices. File names are munged on the destination to fit FAT
naming restrictions, as well as other conversions that might happen.

Usage
=====

See ``syncfat --help`` for detailed help.
Two useful options:

``-v``
    Print more information about what is happening.
    Use this twice to print even more information
``--dry-run``
    Don't actually transfer anything, only print what would happen.
