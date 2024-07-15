# A Python application to decode barcodes from images within a specified folder using different settings and templates.

## Overview
This application attempts to decode barcodes from images using a two-step approach:
1. **Default Settings**: Initially, it decodes the images using the default runtime settings.
2. **Fallback Template**: If no barcodes are detected using the default settings, it then tries to decode the images using an external JSON template with customized settings.

## Features
* Decodes barcodes from multiple images in a specified folder.
* Utilizes default runtime settings for initial decoding.
* Applies a customizable JSON template for enhanced barcode decoding if the default settings fail.
* Supports various barcode formats and configurations.

## Getting Started
### Prerequisites
* Python 3.x
* Dynamsoft Barcode Reader SDK
### Installation
1. Clone the repository:

```
git clone https://github.com/christopher-kwok/batch-decode-multiple-templates.git
cd batch-decode-multiple-templates
```
2. Install the required dependencies:

```
Copy code
pip install dbr
```
3. Obtain a trial license from Dynamsoft and replace the license string in the script.

### Usage
1. Replace the image path in the script with the path to your folder containing images.
2. Customize the JSON template as needed for your specific barcode decoding requirements.
3. Run the script:
```
python batch-decode-multiple-templates.py
```
