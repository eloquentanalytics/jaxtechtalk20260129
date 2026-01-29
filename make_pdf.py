#!/usr/bin/env python3
"""
Combine slide screenshots into a PDF with dark grey background.
Compresses images to keep file size under 100MB for GitHub.
"""
import fitz  # PyMuPDF
from PIL import Image
from pathlib import Path
import glob
import io

# Configuration
SCREENSHOT_DIR = "/var/folders/1h/69n4v3r5373_jzyzsp8s3y780000gn/T/cursor/screenshots"
OUTPUT_PDF = "docs/JaxTech - The AI Innovators Dilemma - 20260128.pdf"
BACKGROUND_COLOR = (10/255, 10/255, 15/255)  # #0A0A0F - matches slide background
PAGE_WIDTH = 1920
PAGE_HEIGHT = 1080
JPEG_QUALITY = 75  # Lower = smaller file, 75 is good balance

def compress_image(img_path):
    """Convert PNG to compressed JPEG bytes."""
    with Image.open(img_path) as img:
        # Convert to RGB (JPEG doesn't support alpha)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Compress to JPEG
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=JPEG_QUALITY, optimize=True)
        return buffer.getvalue()

def main():
    # Get all slide images sorted by name
    pattern = f"{SCREENSHOT_DIR}/slide-*.png"
    images = sorted(glob.glob(pattern))
    
    if not images:
        print(f"No images found matching {pattern}")
        return
    
    print(f"Found {len(images)} slides (compressing to JPEG quality {JPEG_QUALITY})")
    
    # Create PDF
    doc = fitz.open()
    
    for img_path in images:
        print(f"  Adding: {Path(img_path).name}")
        
        # Create page with dark background
        page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)
        
        # Fill with background color
        rect = page.rect
        shape = page.new_shape()
        shape.draw_rect(rect)
        shape.finish(color=BACKGROUND_COLOR, fill=BACKGROUND_COLOR)
        shape.commit()
        
        # Compress and insert the image
        img_bytes = compress_image(img_path)
        img_rect = fitz.Rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT)
        page.insert_image(img_rect, stream=img_bytes)
    
    # Save PDF with compression
    doc.save(OUTPUT_PDF, garbage=4, deflate=True)
    doc.close()
    
    # Report file size
    size_mb = Path(OUTPUT_PDF).stat().st_size / (1024 * 1024)
    print(f"\nCreated: {OUTPUT_PDF}")
    print(f"Size: {size_mb:.1f} MB ({len(images)} pages)")

if __name__ == "__main__":
    main()
