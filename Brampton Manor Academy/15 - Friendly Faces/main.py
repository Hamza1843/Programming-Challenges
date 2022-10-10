import csv 
from pathlib import Path 

csv_file = Path("south.csv")
html_file = Path("south.html")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(path):
    csv_contents = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            csv_contents.append(row)
        return csv_contents

def read_html(path):
    f = open(path)
    html_contents = f.read()
    f.close()
    return html_contents

def process(html, csv):
    for i in range(len(csv)):
        lookingfor_link = "link"+str(i+1)
        lookingfor_initials = "initials"+str(i+1)
        lookingfor_name = "name"+str(i+1)
        newvalue_link = csv[i][0]
        newvalue_initials = csv[i][1]
        newvalue_name = csv[i][2]
        html = html.replace(lookingfor_link, newvalue_link)
        html = html.replace(lookingfor_initials, newvalue_initials)
        html =  html.replace(lookingfor_name, newvalue_name)
    return html

def write_html(path, html):
    f = open(path, "w")
    f.write(html)
    f.close()

if __name__ == "__main__":
    csv = read_csv(csv_file)
    html = read_html(html_file)
    html = process(html, csv)
    write_html("south_final.html", html)