import argparse
from gui import show_gui
from downloader import download_and_extract_packages

def main():
    print()
    parser = argparse.ArgumentParser()
    parser.add_argument('ranges', type=str, help='Line ranges in the format 4,5,8 or 4-8')
    parser.add_argument('tsv_file', type=str, help='TSV file to read')
    parser.add_argument('-x', action='store_true', help='Delete files after unpackaging')
    parser.add_argument('-z', action='store_true', help='Automatically apply zRIF key')
    parser.add_argument('-q', action='store_true', help='Store all files in a single ZIP file')
    parser.add_argument('--nogui', action='store_false', help='Start the graphical user interface')
    args = parser.parse_args()

    if args.nogui:
        show_gui()
    else:
        ranges = args.ranges.replace(" ","")
        tsv_file = args.tsv_file
        delete_after_unpack = args.x
        auto_apply_zrif = args.z
        store_in_zip = args.q

        download_and_extract_packages(ranges, tsv_file, delete_after_unpack, auto_apply_zrif, store_in_zip)

if __name__ == '__main__':
    main()
