import urllib.request
import xml.dom.minidom

data_course = xml.dom.minidom.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp"))
valNodes = data_course.getElementsByTagName("Valute")
for i in valNodes:
   num_code = i.getElementsByTagName("NumCode")[0]
   if num_code.firstChild.data == "348":
      value = i.getElementsByTagName("Value")[0].firstChild.data
      HUF_value = float(value.replace(',','.')) / float(i.getElementsByTagName("Nominal")[0].firstChild.data)
   if num_code.firstChild.data == "578":
      value = i.getElementsByTagName("Value")[0].firstChild.data
      NOK_value = float(value.replace(',','.')) / float(i.getElementsByTagName("Nominal")[0].firstChild.data)
#print("один венгерский форинт равен " + str(HUF_value) + " рублей")
#print("одна норвежская крона равна " + str(NOK_value) + " рублей")
print("одна норвежская крона равна " + str(NOK_value / HUF_value) + " венгерских форинтов")
