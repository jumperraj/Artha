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
print(json_data)
def response():
    string = ""
    for i in json_data["quotes"]:
        if (60 < i["fiftyDayAverage"] < 150):
            string+="stock name :  "+str(i["shortName"])+"  |  "+ "fiftyDayAverage :  "+ str(i["fiftyDayAverage"])+"  |  "+"financial currency :  "+ str(i["financialCurrency"]) +"  |  "+"marketState :  "+str(i["marketState"])+"  |  "+"regularMarketPrice :  "+ str(i["regularMarketPrice"])+"\n"+""+"\n"
    return string
print(response())
