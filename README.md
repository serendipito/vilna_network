# vilna_network

This is a small repository hosting the files generating the [Vilna Network](https://vilna.network) visualisation.

Run each script with *python3 file_name*.

A short description of all of the files and their functions:
- family_network_generator.py generates a network based on the Vilna Troupe dataset (which has to be downloaded separately from the Vilna Troupe website and saved in the current directory as current_database.xls);
- biography_finder.py collects biographies of troop members from the Wikipedia (may take a long time);
- family_network_with_biographies_generator.py same as biography_finder.py but pre-supposes that biography_finder.py has been run and its outputs are saved in biographies.json.

If you run any of the network generators, make sure to save the resulting file in your computer with the desired file name.

More additions exploring different kinds of subsets of the network may follow in the future.
