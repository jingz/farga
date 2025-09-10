import os
from jinja2 import Environment, FileSystemLoader

env = Environment(
        loader=FileSystemLoader("site_templates"),
        autoescape=False)

index_html = env.get_template("pages/index.html")

# print(index_html.render())

# render all the files in the pages
# and write output corresonding the the file name

directory = os.fsencode("site_templates/pages")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if not filename.endswith("html"):
        continue

    print(filename)

    page = env.get_template("pages/" + filename)
    print(page.render())

    with open("site/" + filename, "w") as f:
        f.write(page.render())
