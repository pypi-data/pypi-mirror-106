folder_clean
============

This package allows you to easily specify a folder path and a list of items to exclude from a folder clean.

Usage
_____________

.. code-block:: shell

   from folder_clean import clean
   folder_path = "/content/folder_clean"
   items_to_exclude = ["movies", "notes.txt", "family_pictures"]
   clean(folder_path, items_to_exclude)


