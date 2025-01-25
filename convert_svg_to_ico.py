import os
import subprocess
from PIL import Image
import io
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import multiprocessing

def convert_svg_to_ico(svg_path):
    # Create ico directory if it doesn't exist
    ico_dir = os.path.join(os.path.dirname(svg_path), 'ico')
    os.makedirs(ico_dir, exist_ok=True)
    
    # Create output paths
    filename = os.path.basename(svg_path)
    temp_png_path = os.path.join(ico_dir, os.path.splitext(filename)[0] + '_temp.png')
    ico_path = os.path.join(ico_dir, os.path.splitext(filename)[0] + '.ico')
    
    try:
        # Convert SVG to PNG using Inkscape
        inkscape_path = r"C:\Program Files\Inkscape\bin\inkscape.exe"
        subprocess.run([
            inkscape_path,
            '--export-type=png',
            f'--export-filename={temp_png_path}',
            '-w', '128',
            '-h', '128',
            svg_path
        ], check=True, capture_output=True)
        
        # Convert PNG to ICO
        with Image.open(temp_png_path) as img:
            img = img.convert('RGBA')
            img.save(ico_path, format='ICO', sizes=[(128, 128)])
        
        # Remove temporary PNG file
        os.remove(temp_png_path)
        return True, svg_path
        
    except subprocess.CalledProcessError as e:
        return False, f'Error converting {svg_path}: {str(e)}'
    except Exception as e:
        return False, f'Error converting {svg_path}: {str(e)}'

def find_svg_files(directories):
    svg_files = []
    for directory in directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith('.svg'):
                        svg_files.append(os.path.join(root, file))
    return svg_files

def process_files_with_progress(svg_files):
    # Use number of CPU cores for maximum performance
    num_threads = multiprocessing.cpu_count()
    print(f"Processing {len(svg_files)} files using {num_threads} threads...")
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Create a progress bar
        results = list(tqdm(
            executor.map(convert_svg_to_ico, svg_files),
            total=len(svg_files),
            desc="Converting SVGs to ICOs"
        ))
    
    # Process results
    successful = 0
    for success, message in results:
        if success:
            successful += 1
        else:
            print(message)
    
    print(f"\nConversion complete! Successfully converted {successful} out of {len(svg_files)} files.")

if __name__ == '__main__':
    directories = ['apps', 'places', 'mimetypes', 'devices']
    svg_files = find_svg_files(directories)
    process_files_with_progress(svg_files) 