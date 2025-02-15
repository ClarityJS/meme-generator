from pathlib import Path
from typing import List

from meme_generator import add_meme
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def ming_ku(images: List[BuildImage], texts: List[str], args):

    user_loc = (63, 50)

    user_head = (
        images[0].convert("RGBA").resize((60, 60), keep_ratio=True).circle()
    )

    frame = BuildImage.open(img_dir / "0.png")

    frame.paste(user_head, user_loc, alpha=True)

    text_positions = [
        (30, 180, 150, 210),
        (240, 180, 360, 210),
        (30, 240, 150, 270),
        (240, 240, 360, 270),
    ]

    for i, position in enumerate(text_positions):
        if i < len(texts) and texts[i]:
            frame.draw_text(
                position,
                texts[i],
                allow_wrap=True,
                lines_align="center",
                fontsize=30,
                fill=(0, 0, 0),
            )

    return frame.save_png()


add_meme(
    "ming_ku",
    ming_ku,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["命苦"],
)
