import os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import multiprocessing

def convert_png_to_ico(png_path):
    # Create ico directory if it doesn't exist
    ico_dir = os.path.join(os.path.dirname(png_path), 'ico')
    os.makedirs(ico_dir, exist_ok=True)
    
    # Create output path
    filename = os.path.basename(png_path)
    ico_path = os.path.join(ico_dir, os.path.splitext(filename)[0] + '.ico')
    
    try:
        # Convert PNG to ICO
        with Image.open(png_path) as img:
            # Convert to RGBA if necessary
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Resize to 128x128 if not already that size
            if img.size != (128, 128):
                img = img.resize((128, 128), Image.Resampling.LANCZOS)
            
            img.save(ico_path, format='ICO', sizes=[(128, 128)])
        
        return True, png_path
        
    except Exception as e:
        return False, f'Error converting {png_path}: {str(e)}'

def find_png_files(directories):
    png_files = []
    for directory in directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith('.png'):
                        png_files.append(os.path.join(root, file))
    return png_files

def process_files_with_progress(png_files):
    # Use number of CPU cores for maximum performance
    num_threads = multiprocessing.cpu_count()
    print(f"Processing {len(png_files)} files using {num_threads} threads...")
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Create a progress bar
        results = list(tqdm(
            executor.map(convert_png_to_ico, png_files),
            total=len(png_files),
            desc="Converting PNGs to ICOs"
        ))
    
    # Process results
    successful = 0
    for success, message in results:
        if success:
            successful += 1
        else:
            print(message)
    
    print(f"\nConversion complete! Successfully converted {successful} out of {len(png_files)} files.")

if __name__ == '__main__':
    directories = ['apps', 'places', 'mimetypes', 'devices', 'icons']
    png_files = find_png_files(directories)
    process_files_with_progress(png_files) 