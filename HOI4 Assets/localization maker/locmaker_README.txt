Chupachu's Localization Maker for HOI IV


USAGE


This section explains basic fundamentals of how to run the program.

1. Run the Run.bat file (You can run the python script, but the bat is more convenient, especially if there is an issue.)

2. Decide whether you want to run files in bulk, or if you want to enter them individually.

[Bulk]

2.5. If you want to run files in bulk, simply go into the countries.txt file and create new country files using the TAG|name|adjective format.  Once you've done this, enter y at the main menu.

2.6. This is now complete, and your output will be in out.yml.

[Non-Bulk]

3. Enter the country tag, then a | line, then the name of the country, then another | line, then the adjective of the country.

Example: GER|Germany|German

It's important to have no spaces or empty lines or other strange anomalies, as this is a simple program with little error trapping and they will interfere with the program.

4. Once this is done, your localization files will be placed in the out.yml file.


CUSTOMIZING IDEOLOGIES


This section is about how to add or change ideologies, which is pretty simple because it is much like creating a nation in the countries file.

1. Open the ideologies.txt file.

2. Enter the ideology name on a new line, followed by a |, followed by what you want the country names to be called.  You can use [NAME] and [ADJ] to be replaced by the country's name and adjective-name, respectively.

Example: socialism|People's Republic of [NAME]

3. Save your changes and run the program as normal.


UPDATING THE PROGRAM


Simply run the Updater.bat file and allow the file to be updated.  If this doesn't work, then try opening the GitHub link and downloading it from there.  The link to the GitHub is https://github.com/Chupachu/LocMaker/
