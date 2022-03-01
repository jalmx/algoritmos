import os
from pathlib import Path

"""
    Script to add template html with link to download pdf to generate in future for the plugin 
"""


def get_name_file(path):
    """Get the name file clean, without extention

    Args:
        path (Path): Full path from file

    Returns:
        string: name from file
    """
    return os.path.split(path)[-1].replace(".md", "")


def clear_link(path_file):
    """Replace old file with the content without link to download pdf

    Args:
        path_file (Path): File path to clean text generated automate
    """
    content = ""

    with open(path_file, "r+") as md:
        print("Clear file: ", path_file)
        for line in md.readlines():
            if not line.find("<!-- text autogenerated"):
                break
            content += line

    with open(path_file, "w+") as md:
        md.writelines(content)


def get_temp_html(file_name: str):
    """Generate template html for inject into markdown

    Args:
        file_name (Path): Name from file md to insert into template

    Returns:
        string: Template html with name file
    """
    return f'\n\n<!-- text autogenerated-->\n<blockquote style="" ><p><a href="./{file_name}.pdf" target="_blank">Descargar esta página en PDF</a></p> </blockquote>'


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


def inject_code(file_path, file_name):
    """Inject template html to final documento markdown

    Args:
        file_path (Path): Full path document
        file_name (str): name file markdown to append template html with link to download pdf
    """
    with open(file_path, "+a") as md:
        md.write(get_temp_html(file_name))
        print("Template add to: ", file_path)


if __name__ == "__main__":

    path_to_search = "../docs/"

    for markdown in get_files_md(path_to_search):
        print(markdown)
        clear_link(markdown)
        inject_code(markdown, get_name_file(markdown))
        
        