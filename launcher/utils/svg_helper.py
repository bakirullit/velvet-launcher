from pathlib import Path
import cairosvg

ROOT = Path(__file__).resolve().parent.parent

CACHE = ROOT / "assets" / "icons" / ".cache"

CACHE.mkdir(parents=True, exist_ok=True)


def svg_to_png(svg_path: Path, size: int = 28) -> Path:
    png_path = CACHE / f"{svg_path.stem}_{size}.png"

    # regenerate only if needed
    if not png_path.exists() or svg_path.stat().st_mtime > png_path.stat().st_mtime:
        cairosvg.svg2png(
            url=str(svg_path),
            write_to=str(png_path),
            output_width=size,
            output_height=size,
        )

    return png_path


