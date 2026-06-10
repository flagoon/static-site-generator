import os
from gencontent import generate_page

def generate_page_recursive(content_path, template_path, dest_path, basepath):
    print(f"gen_recursive for: {content_path} to {dest_path}")
    folder_contents = os.listdir(content_path)
    for content in folder_contents:
        if os.path.isfile(content_path + "/" + content):
            new_content_path = content_path + "/" + content.split(".")[0] + ".md"
            new_dest_path = dest_path + "/" + content.split(".")[0] + ".html"
            generate_page(new_content_path, template_path, new_dest_path, basepath)
        else:
            new_content_path = content_path + "/" + content
            new_dest_path = dest_path + "/" + content
            generate_page_recursive(new_content_path, template_path, new_dest_path, basepath)


