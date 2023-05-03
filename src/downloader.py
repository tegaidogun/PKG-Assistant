from colorama import Fore
import os
import zipfile
from utils import download_file, combine_zip_files, delete_all_zip_files_except
from parser import parse_ranges, parse_tsv_file

def download_and_extract_packages(ranges_rum, tsv_file, delete_after_unpack, auto_apply_zrif, store_in_zip):
    ranges = parse_ranges(ranges_rum)
    pkg_data = parse_tsv_file(tsv_file, ranges)

    downloads_dir = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)

    if auto_apply_zrif:
        pkg2zip_path = os.path.join(downloads_dir, 'pkg2zip.zip')
        if not os.path.exists(pkg2zip_path):
            print(f"\n{Fore.LIGHTGREEN_EX}Downloading {Fore.LIGHTMAGENTA_EX}pkg2zip{Fore.GREEN} from github...")
            download_file('https://github.com/mmozeiko/pkg2zip/releases/download/v1.8/pkg2zip_64bit.zip',
                          pkg2zip_path)
            with zipfile.ZipFile(pkg2zip_path, 'r') as pkg_zip:
                pkg_zip.extractall(downloads_dir)
        print()

    for pkg_url, zrif, pkg_name in pkg_data:
        output_path = os.path.join(downloads_dir, os.path.basename(pkg_url))

        print(f"{Fore.BLUE}Downloading {Fore.LIGHTWHITE_EX}{pkg_name}{Fore.BLUE}...{Fore.BLUE}")
        download_file(pkg_url, output_path)

        if auto_apply_zrif:
            print(f"{Fore.RESET}Applying zRIF license key using pkg2zip...")
            os.chdir(downloads_dir)
            os.system(f'pkg2zip {output_path} {zrif}')
            os.chdir(os.path.dirname(downloads_dir))
            output_folder = os.path.splitext(output_path)[0]

            if delete_after_unpack:
                print(f"{Fore.RESET}Deleting {Fore.LIGHTRED_EX}{output_folder}.zip file{Fore.RESET}...\n")

            if delete_after_unpack:
                print(f"{Fore.RESET}Deleting {Fore.LIGHTRED_EX}{pkg_name} .pkg file{Fore.RESET}...\n")
                os.remove(output_path)

    if auto_apply_zrif:
        print(f"\n{Fore.RESET}Deleting {Fore.LIGHTMAGENTA_EX}pkg2zip{Fore.RESET}...")
        try:
            os.remove(os.path.join(downloads_dir, "pkg2zip.zip"))
            os.remove(os.path.join(downloads_dir, "pkg2zip.exe"))
            print("File deleted successfully.\n")
        except OSError as error:
            return None

    if store_in_zip:
        output_zip_path = os.path.join(downloads_dir, 'addcont.zip')
        combine_zip_files(downloads_dir, output_zip_path)
        if delete_after_unpack:
            print("Deleting all other excess zip files...")
            delete_all_zip_files_except(downloads_dir, 'addcont.zip', ".zip")
