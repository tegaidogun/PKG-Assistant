import os
import platform
import subprocess

def main():
    icon_path = os.path.join('assets', 'icons', 'icon.ico')
    main_script = os.path.join('src', 'main.py')
    output_dir = os.path.join(os.getcwd(), 'dist')
    command = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        '--name=pkgassistant',
        f'--icon={icon_path}',
        f'--distpath={output_dir}',
        main_script
    ]

    subprocess.run(command, check=True)

if __name__ == '__main__':
    main()
