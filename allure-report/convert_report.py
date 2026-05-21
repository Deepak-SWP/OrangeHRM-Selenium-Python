import json
from json2html import json2html

with open("allure-report/report.json") as f:
    data = json.load(f)

html = json2html.convert(json=data)

with open("allure-report/report.html", "w") as f:
    f.write(html)

print("HTML Report Generated Successfully")