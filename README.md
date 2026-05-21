# Overview

Software Description: I wrote a Python-based clothing inventory system that uses Pandas to import apparel data from an Excel spreadsheet and load it directly into a local SQLite relational database. To use the program, you simply save your data as InvData.xlsx in the same directory and run the script to automatically build the tables, execute SQL mutations (Insert, Update, Delete), and calculate total stock summaries.

Software Purpose: I wrote this software to demonstrate how to programmatically connect Python with a relational SQL database, automating the process of loading spreadsheet data, executing standard database mutations, and calculating inventory summaries.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

Relational Database: I am using SQLite (via Python's built-in sqlite3 library) as my relational database management system (RDBMS). 

Table Description: The database consists of a single relational table named products. This table is structured to efficiently store, update, and manage inventory metrics for an apparel stock tracking system.

# Development Environment

Tools Used: Visual Studio Code, Pandas, & SQLite3

Language(s) Used: Python & SQLite3

# Useful Websites

- [datacamp](https://www.datacamp.com/tutorial/pandas?utm_cid=23487274749&utm_aid=192541861336&utm_campaign=230119_1-ps-dscia~dsa-tofu~python_2-b2c_3-nam_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9029499-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-dscia~nam-en~dsa~tofu~tutorial~python&gad_source=1&gad_campaignid=23487274749&gbraid=0AAAAADQ9WsFPj1G01_te1pfOLt_MCYckr&gclid=CjwKCAjw5ZXQBhBdEiwAI5XVWeYFr0X5NxTG3-wXtz1X8XQew4GzMQgNJXERQImvJbkiI_rGV2LyRRoCUXgQAvD_BwE) : Used to understand Pandas
- [Gemini](https://gemini.google.com/share/e80fb1b5267e) : Used to fix a problem with Pandas
- [Python](https://docs.python.org/3.8/library/sqlite3.html) : Used to understand sqlite3

# Future Work

- Fix: 
    - Handle Missing Excel File Gracefully: If the InvData.xlsx file is missing or renamed, the program falls back to hardcoded mock data. I need to fix this to either prompt the user to provide the correct file path or automatically generate a fresh template Excel file.
- Improve: 
    - Visual Data Presentation: Instead of printing raw text dataframes to the terminal, improve the user interface by incorporating the tabulate library to print beautiful, clean grid borders for the inventory reports.
- Add: 
    - Transaction History Table: Add a second database table called sales_transactions that records whenever a shirt is bought or restocked. This will allow me to utilize SQL JOIN clauses to link products to their sales history, fulfilling another advanced relational database concept.