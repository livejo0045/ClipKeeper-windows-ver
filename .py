# ClipKeeper for Windows  A clipboard manager built with PyQt6

import sys
import random
from datetime import datetime 
from PyQt6.QtWidgets import (
     Application, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, QFrame, SizePolicy, QGraphicsOpacityEffect, QMenu )
from PyQt6.QtCore import(
    Qt, QTimer, QPropertyAnimation, QEasingCurve, QSize, QMineData, pyqtSignal, QThread, QObject)
from PyQt6.QtGui import(
    QColor, QPalette, QPixmap, QImage, QFont, QFontDatabase, QIcon, QPainter, QBrush, QPen, QLinearGradient, QCursor, QAction )
import uuid

# - Colour palette

BG_DARK = "#0F1117"
BG_CARD = "#161B27"
BG_HEADER = "#0D1020"
BORDER_COLOR = "#252D45"
ACCENT_GREEN = "#4DFFB0"
ACCENT_BLUE = "#4D9FFF"
TEXT_PRIMARY = "#E8EAF2"
TEXT_MUTED = "#5A6380" 
TEXT_DIMMED = "#3A4260"

clip_colors = [
    '#4DFFB0',  # Mint green
    "#4D9FFF",  # sky blue
    "#FF6B9D",  # pink
    "#FFB84D",  # orange
    "#C084FC",  # Purple
    "#4DFFE0",  # cyan
    "#FF8C4D"   # light orange
]

# - Clip data model
class ClipItem:
    deg _init_(self, content_type: str, text: = "", image: QImage = none):
    self.id = str(uuid.uuid4())
    self.content_type = content_type
    self.text = text
    sself.color = random.choice(clip_colors)
    self.timestamp = datetime.now ()

    @property
    def preview(self):
        if self.content_type =="image"
        return "image"
    return self.text{ :120}.replace("\n"," ") if self.text else ""

@property
def time_str(self):
    return self.timestamp.strftime("%H:%M:%S")

