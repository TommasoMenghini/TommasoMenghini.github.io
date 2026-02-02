from PIL import Image, ImageFile
import os

ImageFile.LOAD_TRUNCATED_IMAGES = True

SRC = os.path.join('assets', 'img', 'milan-skyline-original.jpg')
OUT_JPEG = os.path.join('assets', 'img', 'milan-skyline.jpg')
OUT_WEBP = os.path.join('assets', 'img', 'milan-skyline.webp')
OUT_SMALL = os.path.join('assets', 'img', 'milan-skyline-400.jpg')

if not os.path.exists(SRC):
    raise FileNotFoundError(f"Source image not found: {SRC}")

with Image.open(SRC) as im:
    # Ensure RGB for JPEG output
    if im.mode not in ('RGB', 'RGBA'):
        im = im.convert('RGB')

    # Resize to width 1600px
    w, h = im.size
    if w > 1600:
        new_h = int(h * (1600 / w))
        large = im.resize((1600, new_h), Image.LANCZOS)
    else:
        large = im.copy()

    # Save JPEG progressive quality 75, strip exif
    large.save(OUT_JPEG, format='JPEG', quality=75, optimize=True, progressive=True)

    # Save WebP
    large.save(OUT_WEBP, format='WEBP', quality=80, method=6)

    # Small thumbnail width 400px
    new_h = int(h * (400 / w))
    small = im.resize((400, new_h), Image.LANCZOS)
    small.save(OUT_SMALL, format='JPEG', quality=70, optimize=True)

print('Generated:', OUT_JPEG, OUT_WEBP, OUT_SMALL)