from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength

img_dir = Path(__file__).parent / "images"


def maki(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (0, -15, 256, 86),
            text,
            allow_wrap=True,
            lines_align="center",
            max_fontsize=40,
            min_fontsize=20,
            fill=(0, 0, 0),
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_png()


add_meme(
    "maki",
    maki,
    min_texts=1,
    max_texts=20,
    default_texts=["兄弟，你好香"],
    keywords=["真纪"],
)
