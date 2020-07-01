## Objective: Export data from HDFS into a MySQL table using Sqoop.
## Successful outcome: The data in salarydata.txt in HDFS will appear in a table in MySQL named salary2.
- create RDS and connect to workbemch
- create database test;
- use test;
- copy table creation query from labs/Lab3.2 salaries2.sql
- paste to RDS and execute the query
- check salaries2 table created
- now we have to fill the data from HDFS file using sqoop command
- open MobaXterm do SSH
- -> wget wget  https://dbda-labs.s3.amazonaws.com/labs.zip
- -> unzip labs.zip
(image 2.1)
# 1 ) Put the Data into HDFS
- go to labs/Lab3.2
- View the contents of salarydata.txt:
### -> tail salarydata.txt
- Notice the records in this file contain four values separated by commas, and the values represent a gender, age, salary, and zip code, respectively.
- c. Create a new directory in HDFS named salarydata.
### -> hdfs dfs -mkdir salarydata
- d. Put salarydata.txt into the salarydata directory in HDFS.
### -> hdfs dfs –put salarydata.txt salarydata
(image 2.2)
# 3 ) Export the Data
- a. Run a Sqoop command that exports the salarydata folder in HDFS into the salaries2 table in MySQL. At the end of the MapReduce output, you should see a
log event stating that 10,000 records were exported.
## -> sqoop export --connect jdbc:mysql://hadoop.cwibdwqcgjze.us-east-1.rds.amazonaws.com/test --username bhavesh --password corydoras101# --table salaries2 --export-dir salarydata --input-fields-terminated-by ","
(image 2.3)
- b. Verify it worked by viewing the table’s contents from the mysql workbench.
- select * from salaries2;
## Result
You have now used Sqoop to export data from HDFS into a database table in MySQL.
