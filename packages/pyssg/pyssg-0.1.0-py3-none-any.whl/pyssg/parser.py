import os
import shutil
from .discovery import get_all_files
from .converter import create_all_html_from_md


def create_dir_structure(dirs: list[str]):
    cwd = os.getcwd()

    for d in dirs:
        # for the dir structure,
        # doesn't matter if the dir already exists
        try:
            os.makedirs(os.path.join(cwd, d))
        except FileExistsError:
            pass


def copy_existing_html_files(src: str, dst: str, files: list[str]):
    src_file = None
    dst_file = None

    for f in files:
        src_file = os.path.join(src, f)
        dst_file = os.path.join(dst, f)

        shutil.copy2(src_file, dst_file)


def generate_static_site(src: str, dst: str):
    # store the initial workin directory,
    # to be able to come back
    iwd = os.getcwd()

    os.chdir(src)
    dirs, md_files, html_files = get_all_files()
    os.chdir(iwd)

    os.chdir(dst)
    create_dir_structure(dirs)
    os.chdir(iwd)

    copy_existing_html_files(src, dst, html_files)

    create_all_html_from_md(src, dst, md_files)
