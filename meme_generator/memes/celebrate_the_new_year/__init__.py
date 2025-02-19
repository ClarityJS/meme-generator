from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme

img_dir = Path(__file__).parent / "images"


def celebrate_the_new_year(images, texts, args):
    img = images[0].convert("RGBA").resize((1242, 922), keep_ratio=True)
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(img, (0, 0))
    return frame.save_png()


add_meme(
    "celebrate_the_new_year",
    celebrate_the_new_year,
    min_images=1,
    max_images=1,
    keywords=["贺新春"],
)
