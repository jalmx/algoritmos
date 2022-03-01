import os
from pathlib import Path

"""
    Script to add create a markmap taking all files markdown and its subtitles
"""

FLAG_TO_INSERT = "<!-- Map site insert-->"
FLAG_START = "<!-- Map site start-->"
FLAG_END = "<!-- Map site end-->"

## FIXME: ajustar estas funciones


def clear_map(path_file):
    """Replace old file with the content without link to download pdf

    Args:
        path_file (Path): File path to clean text generated automate
    """
    content = ""


    with open(path_file, "r+") as md:
        print("Clear file: ", path_file)
        for line in md.readlines():
            if not line.find(FLAG_START):
                break
            content += line

    with open(path_file, "w+") as md:
        md.writelines(content)


def inject_map(file_path, file_name):
    """Inject template html to final documento markdown

    Args:
        file_path (Path): Full path document
        file_name (str): name file markdown to append template html with link to download pdf
    """
    with open(file_path, "+a") as md:
        md.write("")
        print("Template add to: ", file_path)


####################################


def build_markmap(list_headers):
    map_init = "```markmap"
    map_end = "```"

    content = f"{map_init}\n"
    for line in list_headers:
        content += f"{line}\n"

    content += map_end

    return content


def get_structure_without_hash(path_file):
    """Generate a dict with the structure of document, list of title and subtitles

    Args:
        path_file (Path): Path of file markdown

    Returns:
        dict: Structure with all title and subtitles, the key is h#
    """
    structure = {}

    with open(path_file, "r") as file:
        for line in file.readlines():
            if line.strip().startswith("#"):

                number_hash = len(line.split(" ")[0])

                new_line = line.replace("#" * number_hash, "").strip()

                if not structure.get(f"h{number_hash}"):
                    structure[f"h{number_hash}"] = [new_line]
                else:
                    structure[f"h{number_hash}"].append(new_line)

    return structure


def get_structure_with_hash(path_file):
    """Generate a dict with the structure of document, list of title and subtitles

    Args:
        path_file (Path): Path of file markdown

    Returns:
        dict: Structure with all title and subtitles, the key is h#
    """
    structure = {}

    with open(path_file, "r") as file:
        for line in file.readlines():
            if line.strip().startswith("#"):

                number_hash = len(line.split(" ")[0])

                new_line = line.strip()

                if not structure.get(f"h{number_hash}"):
                    structure[f"h{number_hash}"] = [new_line]
                else:
                    structure[f"h{number_hash}"].append(new_line)

    return structure


def get_all_md(path):
    """get alls files markdown from folder and subfolders

    Args:
        path (Path): path for to search files md

    Returns:
        list: markdown files's list
    """
    list_md = []

    for file in Path(path).iterdir():
        if file.is_dir():
            list_md += get_all_md(file)
        if file.is_file() and str(file).endswith(".md"):
            list_md.append(os.path.abspath(file))

    return sorted(list_md)


def get_all_md_from_folder(path):
    """get alls files markdown from folder

    Args:
        path (Path): path for to search files md

    Returns:
        list: markdown files's list
    """
    list_md = []

    for file in Path(path).iterdir():

        if file.is_file() and str(file).endswith(".md"):
            list_md.append(os.path.abspath(file))

    return sorted(list_md)


def get_paths_abs(base_dir, *args):
    """Generate a list of paths absolutes from base dir and all name of folders

    Args:
        base_dir (Path): Path base to generate path absolute, join base dir and folders

    Returns:
        List: List with all paths from folders
    """
    paths = []

    for path in args:
        paths.append(os.path.abspath(f"{base_dir}{os.path.sep}{path}"))

    return sorted(list(set(paths)))


def get_all_folders(path):
    """Get all folders and subfolders from path

    Args:
        path (Path): Receive a path to search folders

    Returns:
        List: List of folders and sobfolders
    """
    list_dir = []
    for file in Path(os.path.abspath(path)).iterdir():
        if file.is_dir():
            list_dir.append(os.path.abspath(file))
            if len(get_all_folders(os.path.abspath(file))):
                list_dir += get_all_folders(os.path.abspath(file))

    if not (os.path.abspath(path) is list_dir):
        list_dir.append(os.path.abspath(path))

    return sorted(list(set(list_dir)))


def remove_path_home(list_path:list):
    list_complete_new = []
    
    for folder in list_path:
        list_complete_new.append(folder.replace(str(Path.home()),""))
    return list_complete_new
    

def clean_list_folder(list_complete: list, list_exclude: list):
    list_clean = []
    
    list_complete_new = remove_path_home(list_complete)
    list_exclude_new = remove_path_home(list_exclude)
        
    for folder in list_complete_new:
        print(folder.split("/")[1:])
    
    for folder in list_exclude_new:
        print(folder.split("/")[1:])    
    
    return sorted(set(list_clean))


def _clean_list_folder(list_complete: list, list_exclude: list):
    list_clean = []  # foldback

    for exclude in list_exclude:
        for folder in list_complete:
            if not exclude.startswith(folder):
                break
            print("folder:", folder, "exclude", exclude)
            list_clean.append(folder)

    return sorted(set(list_clean))


if __name__ == "__main__":

    PATH_TO_SEARCH = "../docs/"
    # path_file_get_title_map = os.path.abspath(PATH_TO_SEARCH + os.path.sep + "index.md")
    paths_excludes = get_paths_abs(
        PATH_TO_SEARCH, "icons", "img", "javascripts", "stylesheets", "extras"
    )

    # print("=======================EXCLUDES")
    # for e in paths_excludes:
    #     print(e)

    # print("=======================ALL")
    # for e in get_all_folders(PATH_TO_SEARCH):
    #     print(e)

    print("=======================DIFF")

    print(clean_list_folder(get_all_folders(PATH_TO_SEARCH), paths_excludes))
    # for a in clean_list_folder(get_all_folders(PATH_TO_SEARCH), paths_excludes):
    #     print(a)

        # for markdown in get_all_md_from_folder(folder):
        #     print(markdown)
        # print(get_structure_with_hash(markdown))
