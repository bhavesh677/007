# About this Lab
## Objective: Import data from a database into HDFS.
## Successful outcome: You will have imported data from MySQL into folders in HDFS.
# 1 ) Create a Table in MySQL
- first craete RDS in AWS.
- connect RDS to workbench.
- from labs/Lab3.1/ open salaries.sql copy the table creation query.
- go to your RDS database and create test database -> create database test;
- then use database test -> use test;
- then paste table creation query and execute.
- check in the schema our table named salaries has been created.
- now run this query to check our table -> select * from salaries;
- you will get empty table.
- now we have to fill the table.
- right click on your table - select import data - and browse labs/Lab3.1/salaries.txt (makesure before doing this step you convert salaries.txt to salaries.csv).
- now again run this query -> select * from salaries;
- this time you will notice our salaries table is filled with new entries.
# 2 ) Import the Table into HDFS
- open MobaXterm and do SSH.
- download labs.zip -> wget  https://dbda-labs.s3.amazonaws.com/labs.zip
- unzip labs.zip -> unzip labs.zip
## a. Enter the following Sqoop command (all on a single line), which imports the salaries table in the test database into HDFS:
## - sqoop import --connect jdbc:mysql://(end point)/(database name) --username (user name) --password (password) --table (table name)
## -> sqoop import --connect jdbc:mysql://hadoop.cwibdwqcgjze.us-east-1.rds.amazonaws.com/test --username bhavesh --password corydoras101# --table salaries

<img src ="/images/3.2.png" width="1000">

- b. A MapReduce job should start executing, and it may take a couple of minutes for the job to complete.
# 4 ) Verify the Import
- a. View the contents of your HDFS folder:
- -> hdfs dfs -ls
- b. You should see a new folder named salaries. View its contents:
- -> hdfs dfs -ls salaries
- c. Notice there are four new files in the salaries folder named part‐m‐0000x. Why are there four of these files?
- Answer: The MapReduce job that executed the Sqoop command used four mappers, so there are four output files (one from each mapper).
- d. Use the cat command to view the contents of the files. For example:
- -> hdfs dfs -cat salaries/part-m-00000
- Notice the contents of these files are the rows from the salaries table in MySQL. You have now successfully imported data from a MySQL database into HDFS.
Notice that you imported the entire table with all of its columns. Next, you will import only specific columns of a table.
<img src ="/images/3.3.png" width="1000">

# 5 ) Specify Columns to Import
- a. Using the ‐‐columns argument, write a Sqoop command that imports the salary
and age columns (in that order) of the salaries table into a directory in HDFS
named salaries2. In addition, set the ‐m argument to 1 so that the result is a single
file.
Solution: The command you enter in the command line will look like this in the terminal window:
## -> ## -> sqoop import --connect jdbc:mysql://hadoop.cwibdwqcgjze.us-east-1.rds.amazonaws.com/test --username bhavesh --password corydoras101# --table salaries --columns salary,age -m 1 --target-dir salaries2
(image 3.4)
- b. After the import, verify you only have one part‐m file in salaries2:
- -> hdfs dfs -ls salaries2
- c. Verify that the contents of part‐m‐00000 are only the two columns you specified:
- -> hdfs dfs -ls salaries2/part-m-00000
(image 3.5)
# 6 ) Importing from a Query
- Write a Sqoop import command that imports the rows from salaries in MySQL whose salary column is greater than 90,000.00.
- a. Use gender as the --split-by value, specify only two mappers, and import the data into the salaries3 folder in HDFS.
- Tip
The Sqoop command will look similar to the ones you have been using throughout
this lab, except you will use --query instead of --table. Recall that when you use
a --query command you must also define a --split-by column, or define -m to
be 1.
- Also, do not forget to add $CONDITIONS to the WHERE clause of your query, as
demonstrated earlier in this unit.
## -> sqoop import "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" --connect jdbc:mysql://hadoop.cwibdwqcgjze.us-east-1.rds.amazonaws.com/test --username bhavesh --password corydoras101# --query "select * from salaries where salary>90000.00 AND \$CONDITIONS" --split-by salaries.gender -m 2 --target-dir salaries3
- after running this command you will get following error
(image 3.6)
(image 3.6.1)
(image 3.6.2)
(image 3.6.3)
- to remove this error change the collation settings of gender column becouse we are splitting on the basis of gender
(image collation)
- now if you run the same command you will not get any error
(image 3.7)
- b. To verify the result, view the contents of the files in salaries3. You should have only two output files.
- -> hdfs dfs -ls salaries3
- c. View the contents of part‐m‐00000 and part‐m‐00001.
- this part-m-00000 will show only females with salary > 90000
- -> hdfs dfs -cat salaries3/part-m-00000
- this part-m-00001 will show only men with salary > 90000
- -> hdfs dfs -cat salaries3/part-m-00001
(image3.8)
- Notice that one file contains females, and the other file contains males. Why?
- Answer: You used gender as the split‐by column, so all records with the same gender are sent to the same mapper.
- d. Verify that the output files contain only records whose salary is greater than 90,000.00.
## Result
- You have imported the data from MySQL to HDFS using the entire table, specific columns, and also using the result of a query.
