# 1) SSH 
(image)
# 2) Downloading and unziping 
(image)
# Enter the following command to view the usage of hdfs dfs:
## --> hdfs dfs
image
# 3) Create a Directory in HDFS
## a. Enter the following -ls command to view the contents of the user’s root directory
## in HDFS, which is /user/root
## --> hdfs dfs -ls
## You do not have any files in /user/root yet, so no output is displayed.
## Run the -ls command again, but this time specify the root HDFS folder:
## --> hdfs dfs -ls /
(image)
# Important
## Notice how adding the / in the -ls command caused the contents of the root
## folder to display, but leaving off the / showed the contents of /user/root, which
## is the default prefix if you leave off the leading / on any of the hadoop commands
## (assuming the command is run by the “root” user).
# b. Enter the following command to create a directory named test in HDFS:
## --> hdfs dfs -mkdir test
# c. Verify that the folder was created successfully:
## --> hdfs dfs -ls
(image)
# d. Create a couple of subdirectories for test:
## hdfs dfs -mkdir test/test1
## hdfs dfs -mkdir -p test/test2/test3
# Notice how the -p command can be used to create multiple directories. The
## second command above will fail if you omit the -p.
# e. Use the -ls command to view the contents of /user/root:
## Notice you only see the test directory. To recursively view the contents of a folder,
## use -ls -R:
## --> hdfs dfs -ls -R
(image)
# 3) Delete a Directory
## a. Delete the test2 folder (and recursively, its subcontents) using the -rm -R command:
## --> hdfs dfs -rm -R test/test2
## b. Now run the -ls -R command:
## --> hdfs dfs -ls -R
(image)
# Note
## Notice Hadoop created a .Trash folder for the root user and moved the deleted
## content there. The .Trash folder empties automatically after a configured amount
## of time.
# 4) Upload a File to HDFS
(image)
## a. Now let’s put a file into the test folder. Change directories to
## You can also use the ‐tail command to view the end of a file:
## --> tail data.txt
# 5) Copy a File in HDFS
## a. Now copy the data.txt file in test to another folder in HDFS using the -cp command:
## --> hdfs dfs -cp test/data.txt test/test1/data2.txt
## c. Now delete the data2.txt file using the -rm command:
## --> hdfs dfs -rm test/test1/data2.txt
# 6) View the Contents of a File in HDFS
## a. You can use the -cat command to view text files in HDFS. Enter the following command to view the contents of data.txt:
## --> hdfs dfs -cat test/data.txt
(image)
## b. You can also use the ‐tail command to view the end of a file:
## --> hdfs dfs -tail test/data.txt
(image)
## Notice the output this time is only the last 20 rows of data.txt.
# 7) Getting a File from HDFS.
## a. See if you can figure out how to use the get command to copy test/data.txt from HDFS into your local /tmp folder.
## --> hdfs dfs -get test/data.txt /tmp/
## --> cd /tmp
## --> ls data*
(image)
# 8) The getmerge Command
## a. Put the file labs/demos/small_blocks.txt into the test folder in
## HDFS. You should now have two files in test: data.txt and small_blocks.txt.
(image)
## b. Run the following getmerge command:
## --> hdfs dfs -getmerge test /tmp/merged.txt
(image)
## c. What did the previous command do? Did you open the file merged.txt to see what happened?
## Answer: The two files that were in the test folder in HDFS were merged into a
## single file and stored on the local file system.
