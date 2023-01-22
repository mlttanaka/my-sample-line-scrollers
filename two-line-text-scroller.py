# Display a two lines of text using the MatrixPortal library.
import board
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal

# --- Custom font ---
SPESHUL_FONT = "fonts/tb-8.bdf"

# --- Initialize MatrixPortal board ---
matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, bit_depth=6, debug=True)

# Create a line of text. (This will be index 0.)
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(3, 8),
    scrolling=False,
)

# Create a second line of text, with the color and text selected.
# (This will be index 1.)
matrixportal.add_text(
    text_font=SPESHUL_FONT,
    text_position=(0, 20),
    scrolling=True,
)
# The text strings for line 2.
contents = [
    {"text": "I'm so red.", "color": "#ff0000"},
    {"text": "I'm very blue.", "color": "#0000ff"},
]

# Set the speed of the scrolling text.
# - - - - - - - - - - - - - - - - - - -
# By the way, the built-in scroller only scrolls to the left.
# To scroll in a different direction, you'll need to write your
# own method(s) for shifting the pixels across your RGB LED Matrix.
SCROLL_DELAY = 0.07

while True:
    # Display the first line of text (index 0).
    # There's no need to specify the index when it's 0.
    # *shrugs*
    matrixportal.set_text("Lite Brite")

    for content in contents:
        # Display the 2nd line of text (index 1)
        matrixportal.set_text(content["text"], 1)

        # Set the text color of 2nd line of text (index 1)
        matrixportal.set_text_color(content["color"], 1)

        # Scroll the 2nd line of text.
        matrixportal.scroll_text(SCROLL_DELAY)
