from PIL import Image, ImageDraw, ImageFont
import os

def create_app_icon(size, output_path):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw rounded rectangle background with nice gradient-like color
    # Deep blue / purple background
    bg_color = (44, 62, 80, 255) # #2c3e50
    corner_radius = int(size * 0.22)
    draw.rounded_rectangle([0, 0, size, size], radius=corner_radius, fill=bg_color)
    
    # Draw an inner accent border
    border_color = (52, 152, 219, 255) # #3498db
    draw.rounded_rectangle([int(size*0.04), int(size*0.04), int(size*0.96), int(size*0.96)], 
                           radius=int(corner_radius*0.85), outline=border_color, width=max(2, int(size*0.02)))
    
    # Draw mathematical symbols and book design
    # Let's draw text if default font, or draw geometric math symbols
    # Draw "8" in gold/yellow, "ICSE" in white, and "MATHS" in cyan
    try:
        font_large = ImageFont.truetype("arial.ttf", int(size * 0.38))
        font_med = ImageFont.truetype("arial.ttf", int(size * 0.13))
        font_small = ImageFont.truetype("arial.ttf", int(size * 0.11))
    except Exception:
        font_large = font_med = font_small = ImageFont.load_default()
        
    # Draw "8" in center
    draw.text((size/2, size*0.42), "8", fill=(241, 196, 15, 255), anchor="mm", font=font_large)
    
    # Draw "ICSE" on top
    draw.text((size/2, size*0.17), "ICSE", fill=(236, 240, 241, 255), anchor="mm", font=font_med)
    
    # Draw "MATHS" on bottom
    draw.text((size/2, size*0.74), "MATHS", fill=(52, 152, 219, 255), anchor="mm", font=font_med)
    
    # Draw "CLASS" badge
    draw.text((size/2, size*0.87), "SOLUTIONS", fill=(189, 195, 199, 255), anchor="mm", font=font_small)
    
    # Decorative math symbols on sides
    try:
        font_sym = ImageFont.truetype("arial.ttf", int(size * 0.12))
        draw.text((size*0.18, size*0.38), "√", fill=(46, 204, 113, 200), anchor="mm", font=font_sym)
        draw.text((size*0.82, size*0.38), "π", fill=(231, 76, 60, 200), anchor="mm", font=font_sym)
        draw.text((size*0.18, size*0.62), "∑", fill=(155, 89, 182, 200), anchor="mm", font=font_sym)
        draw.text((size*0.82, size*0.62), "x²", fill=(230, 126, 34, 200), anchor="mm", font=font_sym)
    except Exception:
        pass

    img.save(output_path, "PNG")
    print(f"Created {output_path} ({size}x{size})")

os.chdir(r"d:\Guna Shekhar\My Classes\Class 8th icsc")
create_app_icon(192, "icon-192.png")
create_app_icon(512, "icon-512.png")
