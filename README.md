# Remote Database Update with Unity
A small system for updating a remote SQLite database with Unity Web Request through PHP scripts.

## General Information
This program works on 2 different sides:
1. ***Apache Server Side***: The files and folders that will be placed in **htdocs** folder:
   * ***getrow.php** File (Compulsory)*: This is the main PHP file which gets data from Unity Web Request in JSON type and executes an SQL query to update the database with this data on the same server.
   * ***register.db** File (Compulsory)*: This is the database file which will be altered by the data submitter Unity part. The given file here in the **htdocs** folder already has 4 entries which can help easily testing the optional files below. For a clean database file, you can use the **register.db** file given in the **create_db** folder or create a new database file by using the **create_db.py** Python file in it.
   * ***create_db** Folder (Optional)*: **create_db.py** file is used to create an empty **register.db** database with suitable tables for the data submitter Unity part.
   * ***flask** Folder (Optional)*: **crud.py** file is used to monitor the current status of the **register.db** database and update/delete its entries manually via Flask web server: ```python crud.py``` --> *http://localhost:5000/*
   * ***insert.php** File (Optional)*: This file has GET method in PHP form and is used by placing in Apache web server to manually add new entries to the **register.db** database in order to test it optionally.
   * ***insert_get.php** File (Optional)*: This file gets data from the **insert.php** file and writes the new manual entry to the **register.db** database by using the Apache web server: *http://localhost/*
   * ***show_register.php** File (Optional)*: This file is used to monitor the current status of the **register.db** database by listing all the entries in it on the Apache web server: *http://localhost/*  
2. ***Unity Application Side***: The C# script in the Unity application will get some user information input, convert it to JSON type and send it to a remote SQLite database stored in a web server and remotely update it by using the **getrow.php** file.
   * ***WebRequest** Folder*: This is the project folder of the remote database updater Unity program. Open it with Unity editor and build it for the platform that you will use or directly run it with Play Mode. The current remote web server link is set to **localhost** in the project. In order to change the remote web server which stores the **register.db** and **getrow.php** files, open the **HandleButtons.cs** file from **Assets** folder and change the **"http://localhost/getrow.php"** link to **"yourwebserver/getrow.php"**

## Technologies
This project is created with:
* [Unity](https://unity.com/download)
* [XAMPP](https://www.apachefriends.org/download.html)'s Apache Server
* [SQLite Browser](https://sqlitebrowser.org/dl/)
* [SQLite](https://www.sqlite.org/download.html)
* PHP
* Python
  * Flask Framework
* HTML

## Setup & Run
To run this program:
1. Install XAMPP and place the **getrow.php** and **register.db** files in **htdocs** folder of XAMPP. You may copy the **register.db** file from **create_db** folder for a clean database with no entry.
2. Activate Apache web server from the control panel of XAMPP.
3. Run the executable file generated with Unity by building the **WebRequest** project or directly run it with Play Mode.
4. Check the final status of the **register.db** database file by either using the **show_register.php** file from Apache server (*http://localhost/show_register.php*) or running the **crud.py** file with Python (place **flask** folder near the updated **register.db** file in the **htdocs** folder, enter the **flask** folder in terminal/cmd and run: ```python crud.py```) to list database entries on the web browser by using Flask web server (*http://localhost:5000*)
