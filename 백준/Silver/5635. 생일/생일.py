n = int(input())

maxlis={"name" : " ","day" :00,"month" :00,"year":2022}
minlis={"name" : " ","day" :00,"month" :00,"year":00}

def maxadd(a,b,c,d) :
	maxlis["name"]=a
	maxlis["day"]=b
	maxlis["month"]=c
	maxlis["year"]=d
def minadd(a,b,c,d) :
	minlis["name"]=a
	minlis["day"]=b
	minlis["month"]=c
	minlis["year"]=d

for i in range(0,n) :
	name,day,month,year=input().split()
	day = int(day)
	month = int(month)
	year = int(year)

	if year<maxlis["year"] :
		maxadd(name,day,month,year)
	elif year==maxlis["year"] :
		if month<maxlis["month"] :
			maxadd(name,day,month,year)
		elif month == maxlis["month"] :
			if day<maxlis["day"] :
				maxadd(name,day,month,year)

	if year>minlis["year"] :
		minadd(name,day,month,year)
	elif year==minlis["year"] :
		if month>minlis["month"] :
			minadd(name,day,month,year)
		elif month == minlis["month"] :
			if day>minlis["day"] :
				minadd(name,day,month,year)


print(minlis["name"])
print(maxlis["name"])





