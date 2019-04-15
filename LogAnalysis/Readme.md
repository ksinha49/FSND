# LOG REPORTER

A reporting tool that prints out reports (in plain text) based on the data in a sample database(news). This reporting tool is a Python program using the psycopg2 module to connect to the database.
The database news has 3 tables:
  - articles - Contains Author_id, Title, slug(path), lead, body, time and id fields
  - authors - Contains Name, Bio and Id fields 
  - log - Contains path, id, method , status, time , id

The routine has following functionalities:
  - Get the top 3 articles based on number of views
  - Get the sorted list of authors based on the total views on articles
  - Get the dates when the the site sent error responses more than 1%
  

# Requirements

  - Linux Based System. Tested in Vagrant(2.2.4) with VM Virtual Box(v.5.1.38) 
  - Python 3 version for the routine execution
  
### Database Setup

The tool is setup to access the news database and generate the report.
Change the directory to repository location and use the newsdata.sql in the folder to generate the Database in Vagrant environment using the following command:
```sh
$ psql -d news -f newsdata.sql
```

### Command List 

Use this commands to enter the Database and check the DB structure:
```sh
$ psql -d news
$ \d+
```
To run the routine for report log
```sh
$ python3 reporter.py
```

### Plugins

If running in Python3 please install the following plugins:
```sh
$ sudo pip3 install psycopg2
```



