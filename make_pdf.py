#!/usr/bin/env python3
"""
Combine slide screenshots into a PDF with dark grey background.
"""
import fitz  # PyMuPDF
from pathlib import Path
import glob

# Configuration
SCREENSHOT_DIR = "/var/folders/1h/69n4v3r5373_jzyzsp8s3y780000gn/T/cursor/screenshots"
OUTPUT_PDF = "docs/JaxTech - The AI Innovators Dilemma - 20260128.pdf"
BACKGROUND_COLOR = (10/255, 10/255, 15/255)  # #0A0A0F - matches slide background
PAGE_WIDTH = 1920
PAGE_HEIGHT = 1080

def main():
    # Get all slide images sorted by name
    pattern = f"{SCREENSHOT_DIR}/slide-*.png"
    images = sorted(glob.glob(pattern))
    
    if not images:
        print(f"No images found matching {pattern}")
        return
    
    print(f"Found {len(images)} slides")
    
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
        
        # Insert the image centered on the page
        img_rect = fitz.Rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT)
        page.insert_image(img_rect, filename=img_path)
    
    # Save PDF
    doc.save(OUTPUT_PDF)
    doc.close()
    
    print(f"\nCreated: {OUTPUT_PDF} ({len(images)} pages)")

if __name__ == "__main__":
    main()



