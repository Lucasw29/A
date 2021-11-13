# Tagup
After viewing the data. I found that there are 4 tables in the database as mentioned in the test. There are 20 machines in each table (from machine 0 to machine 19). Based on the static data, machine 0 to machine 13 are model A, the rest are model B. Based on my understanding of this dataset, I slice each table into two parts modelA and modelB. The reason I do so is the data coming from a single machine won’t provide enough information for our analyst. The machine may be under a bad condition, or it works overtime. There are tons of reasons that will influence the performance of machines. To get the best result, I think slicing the table based on the model of the machine is optimal. Of course, it only needs one change if we need to slice data based on the machine. 

The next step is data cleaning. I searched all the non-values at first and remove them from our dataset. I also print out how many data were removed. Then, I use a statistical method called IQR to remove the outliers. To consider the reuse of my code, I cannot guarantee all the datasets I received is normalized. This makes me give up on using Z-value. 

After the data is clean, I transfer all the data into an array and convert them together. I also write a function to upload them into S3.

Here I attach the box plot below. Although, it seems like there still are outliers. I’ll still leave them there. They can provide more information for our analysts.

Box plot for all data (before data clean)
Feat0 Model A
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Feat0%20ModelA.png)
Feat0 Model B
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Feat0%20ModelB.png)
Feat1 Model A	
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Feat1%20ModelA.png)
Feat1 Model B   
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Feat1%20ModelB.png)
Feat2 Model A
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Feat2%20ModelA.png)
Feat2 Model B
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Feat2%20ModelB.png)
Feat3 Model A
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Feat3%20ModelA.png)
Feat3 Model B   
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Feat3%20ModelB.png)

Box plot for all data (after data clean)
Feat0 Model A
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Cleaned%20Feat0%20ModelA.png)
Feat0 Model B
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Cleaned%20Feat0%20ModelB.png)
Feat1 Model A	
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Cleaned%20Feat1%20ModelA.png)
Feat1 Model B   
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Cleaned%20Feat1%20ModelB.png)
Feat2 Model A
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Cleaned%20Feat2%20ModelA.png)
Feat2 Model B
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Cleaned%20Feat2%20ModelB.png)
Feat3 Model A
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Cleaned%20Feat3%20ModelA.png)
Feat3 Model B   
![image](https://github.com/Lucasw29/Tagup/blob/main/Img/Cleaned%20Feat3%20ModelB.png)

