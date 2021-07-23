#!python3
'''
Converts a word doc to md using pandoc
'''

#from bs4 import BeautifulSoup as bs
#from bs4 import Comment, Doctype
#import json
import os
import shutil
import subprocess


# get info
print('Files need to be in the current directory.  What is the name of the word doc you want to convert to html?: ')
word_doc = input()

print('A folder for media will be created in the ../content folder.  The name of this folder is ../content/:')
folder = input()
md = word_doc[:-5] + ".md"
md_markdownify = word_doc[:-5] + "-markdownify.md"
html = word_doc[:-5] + ".html"

destination = '../content'

shutil.copy2('./'+word_doc, destination)
os.chdir(destination)

'''
# convert to html first to preserve tables in a readable format and also to allow for some parsing
subprocess.run(["pandoc", "--extract-media", "./" + folder, "-s", word_doc, "-o", html])

# take the .html version of document, read into memory:
with open(html, "r") as f:
    soup = bs(f, 'html.parser')

# removing or changing document attributes

def remove_instance_type(soup, instance):
    elements = soup.find_all(text=lambda text:isinstance(text, instance))
    for element in elements:
        element.extract()


remove_style = soup.find('style')
remove_style.extract()
remove_instance_type(soup, Doctype)

# getting rid of extraneous text:
for txt in soup.find_all(text='intentionally blank'):
    txt.parent.extract()

# write html to file
with open(html, "w+") as f:
    f.write(soup.prettify())
'''

#subprocess.run(["pandoc", html, "-o", md])
subprocess.run(["pandoc", "--extract-media", "./" + folder, "-s", word_doc, "-t", "gfm", "-o", md])

os.remove(word_doc)
#os.remove(html)


os.chdir('..')
os.chdir('utils')


"""


- might be best to convert to HTML, scrub, then Markdown...
{width="6.425613517060367in"
height="3.7361964129483813in"}
Page intentionally left blank.
[]{#_Toc33174698 .anchor}
.ul
Tables are trash in the default converter




# using soup, create a .js react component stub
os.chdir("../utils")
with open(html[:-5] + '.js', "w+") as f:
    f.write('import React, { Component } from "react";')
    f.write('import "./html-inline.css";')
    f.write('\n')
    f.write('\n')
    f.write('class HTMLInline extends Component {')
    f.write('  componentDidMount() {    const id = this.props.placeholder;    const yOffset = -10;    const element = document.getElementById(id);    const y =      element.getBoundingClientRect().top + window.pageYOffset + yOffset;    window.scrollTo({ top: y, behavior: "smooth" });  }')
    f.write('\n')
    f.write('  render() {var visibility = "show";if (this.props.menuVisibility) {visibility = "hide";}    return (')
    f.write('<div id="html-inline" className={visibility}>')
    f.write(soup.prettify())
    f.write("</div>")
    f.write("    );  }}export default HTMLInline;")
print('Take the file ' + html[:-5] + '.js in ./utils and copy it to the render component of a new React component .js file.')


# create a JSON obj that conforms to spec for frontend search (react-minisearch)
json_obj = html[:-5] + '-data.js'
new_search_doc = []
for i, item in enumerate(search_items):
    new_search_doc.append({
        'id': i+1,
        'name': item[0].split(':')[0] + ':' + item[1][:50] + "...",
        'link_name': item[0],
        'description': item[1]
    })


with open(json_obj, "w+") as f:
    f.write('export var ' + html[:-5] + 'Data = ')
    f.write(json.dumps(new_search_doc))

shutil.copy2('./'+json_obj, '../src')
os.remove(json_obj)
print('File ' + json_obj + ' is in ./src, ready to add to mini-search as a document.')
"""