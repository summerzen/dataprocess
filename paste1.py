import pandas as pd
data1=[]

with open('quotes111.txt',"r") as f:
   for line in f:
      
      line=line.strip().split("\t")
      line[0]=line[0].replace("\xe7\x94\xb5\xe5\xbd\xb1","")
      line[0]=line[0].strip()
      line[1]=line[1].strip()
      data1.append(line)

data2=[]

translation={}
i=0
with open('titles7.txt',"r") as u:
    for line in u:
        
       line=line.strip().split("\t")
       data2.append(line)

data3=[]
with open('titles7.txt',"r") as u:
    for line in u:
       line=line.strip().split("\t")[1]
       line=line.strip()
       data3.append(line)

for i in range(len(data3)/2):
    translation[data3[2*i+1].strip()]=data3[2*i].strip()



for i in range(len(data1)):
   if data1[i][0] in translation.keys():
         data1[i][0]=translation[data1[i][0]]
   data1[i][2]=int(data1[i][2])

k=0
WPR={}
with open('titles7.txt',"r") as r:
      for line in r:
         line=line.strip().split("\t")
         line[0]=line[0].strip()
         line[1]=line[1].strip()
         k=k+1
         if k%2!=0:
           WPR[line[1]]=line[0]


for i in range(len(data1)):
     if data1[i][0] in WPR.keys():
         data1[i].insert(0,WPR[data1[i][0]])

df1=pd.DataFrame(data1)

df1.columns=['wpr','title','date','mention']         
df2=df1.groupby(['wpr','title','date'],as_index=False).agg("sum")        


#col_list=list(df)

#df2=df2[["a","b","c"]]

#print list2[1][0]
#print list2[1][1]
#print list2[1][2]

print df2

df2.to_csv(r'wechat_output.txt', header=None, index=None, sep='\t', mode='w')
 

       

    
