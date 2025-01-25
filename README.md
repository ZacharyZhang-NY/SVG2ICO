# 🎨 SVG2ICO

> A lightning-fast ⚡ batch SVG to ICO converter using Python and Inkscape CLI

## 🌟 Features

- 🚀 Multi-threaded processing for maximum performance
- 📁 Batch processing of multiple directories
- 🎯 Converts SVG files to 128x128 ICO format
- 📊 Progress bar visualization
- ⚙️ Utilizes all available CPU cores
- 🔄 Automatic cleanup of temporary files

## 🔧 Prerequisites

- Python 3.6+
- Inkscape (installed in the default location: `C:\Program Files\Inkscape\bin\inkscape.exe`)
- Required Python packages:
  ```txt
  Pillow==10.1.0
  tqdm==4.66.1
  ```

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/svg2ico.git
   cd svg2ico
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. Place your SVG files in any of these directories:
   - `apps/`
   - `places/`
   - `mimetypes/`
   - `devices/`

2. Run the script:
   ```bash
   python convert_svg_to_ico.py
   ```

3. The converted ICO files will be saved in an `ico` subdirectory within each source directory.

## 🔍 How It Works

The script performs the following operations:
1. Recursively searches for SVG files in specified directories
2. Creates an `ico` subdirectory in each source location
3. Converts each SVG to a temporary PNG using Inkscape CLI
4. Converts the PNG to ICO format using Pillow
5. Automatically removes temporary files
6. Utilizes multi-threading for optimal performance

## 📊 Performance

The converter automatically detects your CPU core count and creates an optimal number of threads for parallel processing. Progress is displayed using a progress bar, showing real-time conversion status.

## ⚠️ Error Handling

- Failed conversions are logged with detailed error messages
- The script continues processing remaining files even if some conversions fail
- A summary of successful and failed conversions is provided at the end

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest enhancements
- 🔧 Submit pull requests

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inkscape for providing CLI support
- Pillow library for image processing
- tqdm for progress bar functionality

---

Made with ❤️ by Yang Zhang
