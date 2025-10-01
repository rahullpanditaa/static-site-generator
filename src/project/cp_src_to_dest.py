from pathlib import Path
from shutil import copytree

def src_to_dest(src="static", dest="public"):
    src_dir = Path(src).resolve()
    dest_dir = Path(dest).resolve()

    if not (src_dir.exists() or dest_dir.exists()):
        return "Error: Invalid directories given"
    
    if not (src_dir.is_dir() and dest_dir.is_dir()):
        return "Error: Given args not directories"
    
    # delete contents of dest dir
    delete_dir_contents(dest_dir)
    copytree(src=src_dir, dst=dest_dir, dirs_exist_ok=True)
    

# will delete all files in dir and subdir
# at the end of it the dir will only contain empty subdirs
def delete_dir_contents(dir: Path):
    # root -> pth to dir currently being walked
    # dirs -> list of str for names of subdirs in root
    # files -> list of str for files in root
    for root, dirs, files in dir.walk(top_down=False):
        for name in files:
            (root / name).unlink()
        for name in dirs:
            (root / name).rmdir()
        