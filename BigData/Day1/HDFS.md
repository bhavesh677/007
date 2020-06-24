# 1) SSH 

<img src ="/images/1.png" width="500">

# 2) Downloading and unziping 

<img src ="/images/2.png" width="500">

# Enter the following command to view the usage of hdfs dfs:
## --> hdfs dfs

<img src ="/images/3.png" width="500">

# 3) Create a Directory in HDFS
## a. Enter the following -ls command to view the contents of the user’s root directory
## in HDFS, which is /user/root
## --> hdfs dfs -ls
## You do not have any files in /user/root yet, so no output is displayed.
## Run the -ls command again, but this time specify the root HDFS folder:
## --> hdfs dfs -ls /

<img src ="/images/4.png" width="500">

# Important
## Notice how adding the / in the -ls command caused the contents of the root
## folder to display, but leaving off the / showed the contents of /user/root, which
## is the default prefix if you leave off the leading / on any of the hadoop commands
## (assuming the command is run by the “root” user).
# b. Enter the following command to create a directory named test in HDFS:
## --> hdfs dfs -mkdir test
# c. Verify that the folder was created successfully:
## --> hdfs dfs -ls

<img src ="/images/5.png" width="500">

# d. Create a couple of subdirectories for test:
## hdfs dfs -mkdir test/test1
## hdfs dfs -mkdir -p test/test2/test3
# Notice how the -p command can be used to create multiple directories. The
## second command above will fail if you omit the -p.
# e. Use the -ls command to view the contents of /user/root:
## Notice you only see the test directory. To recursively view the contents of a folder,
## use -ls -R:
## --> hdfs dfs -ls -R

<img src ="/images/6.png" width="500">

# 3) Delete a Directory
## a. Delete the test2 folder (and recursively, its subcontents) using the -rm -R command:
## --> hdfs dfs -rm -R test/test2
## b. Now run the -ls -R command:
## --> hdfs dfs -ls -R

<img src ="/images/7.png" width="500">

# Note
## Notice Hadoop created a .Trash folder for the root user and moved the deleted
## content there. The .Trash folder empties automatically after a configured amount
## of time.
# 4) Upload a File to HDFS

<img src ="/images/8.png" width="500">

## a. Now let’s put a file into the test folder. Change directories to
## You can also use the ‐tail command to view the end of a file:
## --> tail data.txt
# 5) Copy a File in HDFS
## a. Now copy the data.txt file in test to another folder in HDFS using the -cp command:
## --> hdfs dfs -cp test/data.txt test/test1/data2.txt
<img src ="/images/9.png" width="500">
## c. Now delete the data2.txt file using the -rm command:
## --> hdfs dfs -rm test/test1/data2.txt
# 6) View the Contents of a File in HDFS
## a. You can use the -cat command to view text files in HDFS. Enter the following command to view the contents of data.txt:
## --> hdfs dfs -cat test/data.txt

<img src ="/images/10.png" width="500">

## b. You can also use the ‐tail command to view the end of a file:
## --> hdfs dfs -tail test/data.txt

<img src ="/images/11.png" width="500">

## Notice the output this time is only the last 20 rows of data.txt.
# 7) Getting a File from HDFS.
## a. See if you can figure out how to use the get command to copy test/data.txt from HDFS into your local /tmp folder.
## --> hdfs dfs -get test/data.txt /tmp/
## --> cd /tmp
## --> ls data*

<img src ="/images/12.png" width="500">

# 8) The getmerge Command
## a. Put the file labs/demos/small_blocks.txt into the test folder in
## HDFS. You should now have two files in test: data.txt and small_blocks.txt.

<img src ="/images/13.png" width="500">

## b. Run the following getmerge command:
## --> hdfs dfs -getmerge test /tmp/merged.txt

<img src ="/images/14.png" width="500">

## c. What did the previous command do? Did you open the file merged.txt to see what happened?
## Answer: The two files that were in the test folder in HDFS were merged into a
## single file and stored on the local file system.
