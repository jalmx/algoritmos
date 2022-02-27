import os
from pathlib import Path

"""
    Script to add create a markmap taking all files markdown and its subtitles
"""

flag_to_insert = "<!-- Map site insert-->"
flag_start = "<!-- Map site start-->"
flag_end = "<!-- Map site end-->"

## No usados por el momento
def clear_link(path_file):
    """Replace old file with the content without link to download pdf

    Args:
        path_file (Path): File path to clean text generated automate
    """
    content = ""

    with open(path_file, "r+") as md:
        print("Clear file: ", path_file)
        for line in md.readlines():
            if not line.find(flag_start):
                break
            content += line

    with open(path_file, "w+") as md:
        md.writelines(content)


def inject_code(file_path, file_name):
    """Inject template html to final documento markdown

    Args:
        file_path (Path): Full path document
        file_name (str): name file markdown to append template html with link to download pdf
    """
    with open(file_path, "+a") as md:
        md.write("")
        print("Template add to: ", file_path)


def generate_link(**kwargs):
    """Generate a tag with the content, a <p> and inside a <a>

    Returns:
        kwargs: content for <p>, href and text to <a>
    """
    return f'<p>{kwargs["content"]} <a href="{kwargs["href"]}" target="_blank">{kwargs["link_text"]}</a></p>'.strip()

####################################

def get_files_md(path):
    """get alls files markdown from folder and subfolders

    Args:
        path (Path): path for to search files md

    Returns:
        list: markdown files's list
    """
    list_md = []

    for file in Path(path).iterdir():
        if file.is_dir():
            list_md += get_files_md(file)
        if file.is_file() and str(file).endswith(".md"):
            list_md.append(os.path.abspath(file))

    return list_md



if __name__ == "__main__":

    path_to_search = "../test/"

    for markdown in get_files_md(path_to_search):
        print(markdown)
