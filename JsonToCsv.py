import csv
import json

with open("app2869_edit.json") as file:
    data = json.load(file)

f = csv.writer(open("app2869.csv", "wb+"))

f.writerow(["category", "level", "source_time", "source_ip", "client", "user", "area", "type_of_change", "object", "id",
            "log_time", "environment"])

for x in data:
    f.writerow([x["category"],
                x["level"],
                x["source_time"],
                x["source_ip"],
                x["client"],
                x["user"],
                x["fields"]["area"],
                x["fields"]["type_of_change"],
                x["fields"]["object"],
                x["id"],
                x["log_time"],
                x["environment"]])
