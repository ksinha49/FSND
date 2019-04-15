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

  - Linux Based System. 
  Run it in a Virtual machine environment using:
     1. Vagrant version 2.2.4 [Click [here](https://www.vagrantup.com/) to install]. 
     2. Vagrant Configuration file to setup the VM. This can be downloaded from [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).
     3. Oracle VM Virtual Box version 5.1.38 [Click [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install].
  - Use Python 3 version for testing this routine. Click [here](https://www.python.org/downloads/) for installation link on your local machine.   
  - Database file used in this tool can be found in this location [[link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)].
  
### Virtual Machine setup
Once the Virtual Machine and the Vagrant installation complete. Unzip the Vagrant Config File to a folder and using your terminal go the folder location. Once in the folder.Run the following command:
```sh
$ vagrant up
```
For first time users it will take some time to boot up the VM and installation of the OS. Once the VM has booted up and the terminal displays the VM is ready for use, type the following command to access the VM in vagrant
```sh
$ vagrant ssh
```
For installation of Python 3 on Vagrant OS use the following command in the VM
  ```sh
  sudo apt-get install python3 python3-pip
  ```
NOTE: For Windows users you will need to enable Virtualization in BIOS or UEFI firmware of your local machine prior to running this step or the VM will not boot up.
Click on [this](https://blogs.technet.microsoft.com/canitpro/2015/09/08/step-by-step-enabling-hyper-v-for-use-on-windows-10/) to learn more on how to enable virtualization on your local machine.
  
  
### Database Setup

The tool is setup to access the news database and generate the report.
Change the directory to repository location and use the newsdata.sql in the folder to generate the Database in Vagrant environment using the following command:
```sh
$ psql -d news -f newsdata.sql
```

### Command List 

Use this commands to enter the Database and check the DB structure respectively:
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



