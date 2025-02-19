import random
from pathlib import Path

from pil_utils import BuildImage
from pydantic import Field

from meme_generator import (
    MemeArgsModel,
    MemeArgsType,
    ParserArg,
    ParserOption,
    add_meme,
)
from meme_generator.exception import MemeFeedback, TextOverLength

img_dir = Path(__file__).parent / "images"

help_text = "图片编号，范围为 1~4"


class Model(MemeArgsModel):
    number: int = Field(0, description=help_text)


args_type = MemeArgsType(
    args_model=Model,
    parser_options=[
        ParserOption(
            names=["-n", "--number"],
            args=[ParserArg(name="number", value="int")],
            help_text=help_text,
        ),
    ],
)


def sick_delicate(images: list[BuildImage], texts, args: Model):
    total_num = 4

    if args.number == 0:
        num = random.randint(1, total_num)
    elif 1 <= args.number <= total_num:
        num = args.number
    else:
        raise MemeFeedback(f"图片编号错误，请选择 1~{total_num}")

    img_name = f"{num:02d}.png"
    frame = BuildImage.open(img_dir / img_name)
    text = texts[0]

    font_color = "red" if img_name == "03.png" else "white"

    try:
        frame.draw_text(
            (20, 0, frame.width - 20, 180),
            text,
            max_fontsize=70,
            min_fontsize=30,
            fill=font_color,
            lines_align="center",
        )
    except TextOverLength:
        raise TextOverLength(text)

    return frame.save_png()


add_meme(
    "sick_delicate",
    sick_delicate,
    min_texts=1,
    max_texts=1,
    default_texts=["好羡慕啊"],
    args_type=args_type,
    keywords=["病娇"],
)
