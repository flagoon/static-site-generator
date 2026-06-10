
import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page
from gencontent_recursive import generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

paths= [
    "/blog/glorfindel",
    "/blog/tom",
    "/blog/majesty",
    "/contact"
]

basepath = sys.argv if sys.argv != None else "/"


def main() -> None:
    print("Deleting public directory...")
    print(basepath[1])
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        f"/`{basepath[1]}",
    )

main()
