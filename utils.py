from matplotlib.font_manager import FontManager
from matplotlib import rcParams


def add_font(font_file_name: str) -> None:
    """Add a font to the list of available fonts."""
    fm = FontManager()
    fm.addfont(font_file_name)
    rcParams['font.family'] = font_file_name.split('.')[0]
