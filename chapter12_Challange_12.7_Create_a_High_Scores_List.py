import csv
from pathlib import Path
from Common import myPrint as sysout

score_csv = Path(Path.cwd()/"chapter12_Exercise"/"score.csv")

values = [ ["name", "score"],
           ["LLCoolDave",23],
           ["LLCoolDave",27],
           ["red",12],
           ["LLCoolDave",26],
           ["tom123",26] ]

with score_csv.open("w", newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(values)


high_scores_csv = Path(Path.cwd()/"chapter12_Exercise"/"high_scores.csv")

dict_high_scores= {}
with open(score_csv) as f:
    csv_dict_reader = csv.DictReader(f)
    for e in csv_dict_reader:
        # print(e)
        # each element in csv_dict_reader object is a dictionary
        # it is easier to work with each field if saving them separately 
        name = e['name']
        # convert the score to an integer, easy to compare.
        high_score = int(e['score'])
        # print(f"{name}:{high_score}")
        # then save the key value pair in a dictionary.
        if name not in dict_high_scores:
            dict_high_scores[name] = high_score
        else:
            if dict_high_scores[name] < high_score:
                dict_high_scores[name] = high_score

with high_scores_csv.open("w",encoding="utf-8",newline='') as f:
    csv_dict_writer = csv.DictWriter(f,fieldnames=["name","high_scores"])
    # write the header first
    csv_dict_writer.writeheader()
    # convert the dictionary we generated from last step
    # to a format csv.DictWriter recognizes
    # list of dictionaries.
    for item in dict_high_scores:
        row = {"name":item,"high_scores":dict_high_scores[item] }
        csv_dict_writer.writerow(row)
