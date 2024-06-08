import json, csv, logging

from model.cls_custom import CustomJSONEncoder
from model.cls_process import Process

logging.basicConfig(level=logging.INFO)

def read_filter_csv():
    colums = [
        "Name",
        "Color",
        "Type"
    ]    
    with open('tbl-filter.csv', "r") as fi:
        reader = csv.DictReader(
            fi, fieldnames=colums, delimiter=",", quotechar='"'
        )

        # This skips the first row which is the header of the CSV file.
        next(reader)

        build_const = []
        platform_const = []
        language_const = []
        tech_const = []
        for row in reader:
            val = {'name': row['Name'], 'color': row['Color']}
            if int(row['Type']) == 1:
                build_const.append(val)
            elif int(row['Type']) == 2:
                language_const.append(val)
            elif int(row['Type']) == 3:
                platform_const.append(val)
            else:
                tech_const.append(val)

        return build_const, platform_const, language_const, tech_const

def read_catagory_csv():
    colums = [
        "Key", "Catagory", "Subcatagory"
    ]    
    with open('tbl-catagory.csv', "r") as fi:
        reader = csv.DictReader(
            fi, fieldnames=colums, delimiter=",", quotechar='"'
        )

        # This skips the first row which is the header of the CSV file.
        next(reader)

        actions = []
        for row in reader:
            value = {row['Key']: {'catagory': row['Catagory'], 'subcatagory': row['Subcatagory']}}
            actions.append(value)

        return actions

def read_repo_csv():
    catagory_const = read_catagory_csv()
    build_const, platform_const, language_const, tech_const = read_filter_csv()
    colums = [
        "Name"
    ]    
    with open('Repo.csv', "r") as fi:
        reader = csv.DictReader(
            fi, fieldnames=colums, delimiter=",", quotechar='"'
        )

        # This skips the first row which is the header of the CSV file.
        next(reader)

        actions = []
        for row in reader:
            p = Process(row['Name'], catagory_const, build_const, platform_const, language_const, tech_const)
            s = json.dumps(p, cls=CustomJSONEncoder)
            actions.append(s)

        return actions
    
json_data = read_repo_csv()
with open('data.txt', 'w') as out_file:
     json.dump(json_data, out_file, sort_keys = True, indent = 4,
               ensure_ascii = False)