import os
import shutil


def zip_directory(folder_path: str, output_path: str):
    print(f"Zipping {folder_path} to {output_path}")
    base_name = output_path.replace('.zip', '')
    root_dir, base_dir = os.path.split(folder_path)
    shutil.make_archive(base_name, 'zip', root_dir=root_dir, base_dir=base_dir)

def main():
    examples_dir = 'examples'
    dist_dir = 'dist'

    if os.path.exists(dist_dir):
        print(f"Removing existing {dist_dir}")
        shutil.rmtree(dist_dir)
    os.makedirs(dist_dir)

    for subdir in os.listdir(examples_dir):
        subdir_path = os.path.join(examples_dir, subdir)
        if os.path.isdir(subdir_path):
            zip_filename = f"{subdir}.zip"
            zip_filepath = os.path.join(dist_dir, zip_filename)
            zip_directory(subdir_path, zip_filepath)


if __name__ == "__main__":
    main()
