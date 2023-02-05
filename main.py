from matrix.bindings.python.rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 2
options.parallel = 1
# If you have an Adafruit HAT: 'adafruit-hat'
options.hardware_mapping = 'regular'

# tdb
