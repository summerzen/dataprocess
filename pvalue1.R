attach(chickwts)
x<-sort(as.vector(weight[feed=="soybean"]))
y<-sort(as.vector(weight[feed=="linseed"]))
t0<-t.test(x,y)$p.value
R<-888
z<-c(x,y)
K<-1:(length(x)+length(y))
reps<-numeric(R)
for (i in 1:R)
{k<-sample(K,size=length(x),replace=FALSE)
	x1<-z[k]
	y1<-z[-k]
	reps[i]<-t.test(x1,y1)}
p<-mean(c(t0,reps)>=t0)
hist(unlist(reps),freq=FALSE)
points(t0,0,cex=1,pch=16)