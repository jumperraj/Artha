import pandas as pd
import requests
import json
url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/co/collections/undervalued_growth_stocks"

querystring = {"start":"0"}

headers = {
	"X-RapidAPI-Key": "d4f2c581e8msh426bae17d2f92d5p1d8341jsnea7fac36ad7d",
	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)
data=response.text
json_data=json.loads(data)
short=[]
fda=[]
fc=[]
ms=[]
rmp=[]

print(type(json_data))

def response():
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    string = ""
    for i in json_data["quotes"]:
        if (60  <i["fiftyDayAverage"] <170):
            print("s001")
            string=string + "stock name :  "+str(i["shortName"])+"  |  "+ "fiftyDayAverage :  "+ str(i["fiftyDayAverage"])+"  |  "+"financial currency :  "+ str(i["financialCurrency"]) +"  |  "+"marketState :  "+str(i["marketState"])+"  |  "+"regularMarketPrice :  "+ str(i["regularMarketPrice"])+"\n"+""+"\n"
            short.append(str(i["shortName"]))
            c1+=1
            fda.append(str(i["fiftyDayAverage"]))
            c2+=1
            fc.append(i["financialCurrency"])
            c3+=1
            ms.append(i["marketState"])
            c4+=1
            rmp.append(i["regularMarketPrice"])
            c5+=1
    print(c1,c2,c3,c4,c5)
    return string
response()
df3=pd.DataFrame()
df3["Name"]=short
df3["fiftyDayAverage"]=fda
df3["financialCurrency"]=fc
df3["marketState"]=ms
df3['regularMarketPrice']=rmp
pd.set_option('display.max_columns',None)
print(df3.head())
# print(type(json_data["quotes"]))
# # for i in json_data["quotes"] :
# #     print(i)




