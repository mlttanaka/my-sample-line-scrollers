# Display a single line of text in a custom font using just the
# MatrixPortal library and its dependencies.
import board
from adafruit_matrixportal.matrixportal import MatrixPortal

# --- Load font --
SPESHUL_FONT = "fonts/Helvetica-Bold-16.bdf"

# --- Display setup ---
matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, bit_depth=4, debug=True)

# Create a new label with the color and text selected
matrixportal.add_text(
    text_font=SPESHUL_FONT,
    text_position=(0, (matrixportal.graphics.display.height // 2) - 1),
    scrolling=True,
)

SCROLL_DELAY = 0.03

contents = [
    {"text": "THIS IS RED", "color": "#ff0000"},
    {"text": "THIS IS BLUE", "color": "#0000ff"},
]

while True:
    for content in contents:
        matrixportal.set_text(content["text"])

        # Set the text color
        matrixportal.set_text_color(content["color"])

        # Scroll it
        matrixportal.scroll_text(SCROLL_DELAY)
