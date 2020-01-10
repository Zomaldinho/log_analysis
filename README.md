Log Analysis Project

This project is created based on Database of a news website to get :
1- The most popular three articles of all time.
2- The most popular article authors of all time.
3- Days when more than 1% of requests led to errors.

The code is written in Python in three different functions for each requirement so that any one can call only one function or the three functions at one time by adding or removing the function call from the Python file

Function "pop_art()" for requirement #1
Function "pop_aut()" for requirement #2
Function "errors()" for requirement #3

Use a terminal
Access this project using a Unix-style terminal on your computer. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from git-scm.com.

Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.
Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

Download the VM configuration
https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip

Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!
Then use the command psql -d news -f newsdata.sql to load and access the database that you can download from here
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip


The views used in the database are:

1) hits ==> 'create view hits as select articles.slug, count(*) as views from articles,log where log.path = CONCAT('/article/', articles.slug) group by articles.slug;'
2) auth_name ==> 'create view auth_name as select authors.name,articles.slug from authors,articles where articles.author = authors.id;'
3) error_t ==> 'create view error_t as select time::date as day,count(*) as errors from log where status='404 NOT FOUND' group by day order by day desc;'
4) requests_t ==> 'create view requests_t asselect time::date as day,count(*) as requests from log group by day order by day;'
5) error_pcnt ==> 'create view error_pcnt as select error_t.day,round(((error_t.errors::decimal*100)/requests_t.requests::decimal), 2) as percentage from error_t,requests_t where error_t.day = requests_t.day;'