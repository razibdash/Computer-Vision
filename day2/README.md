# Day 2 — OpenCV Basics

Scripts covering core OpenCV operations: reading images/video/webcam, basic image
processing (grayscale, blur, edge detection), cropping, drawing shapes/text,
perspective warping, and stacking images.

## Files

### `reading_images.py`
Demonstrates three input sources with OpenCV (image, video file, webcam), with
image/video reading commented out and webcam capture active. Opens the default
webcam at 640x480 and shows the live feed until `q` is pressed.

### `basic_function.py`
Walks through grayscale conversion, Gaussian blur, and Canny edge detection on
`resources/lena.png`. Earlier steps are commented out; only the Canny edge
detection section runs, printing the shape of each intermediate image and
displaying all four versions (original, grayscale, blurred, canny).

### `resize_image.py`
Loads `Resources/lambo.png` and crops a region (`[0:200, 200:500]`) using NumPy
array slicing, then displays the original and cropped images side by side.

### `shapes_test.py`
Creates a blank 512x512 image with NumPy, fills it with a solid color, then
draws a line, a rectangle, a filled circle, and text on top using
`cv2.line`, `cv2.rectangle`, `cv2.circle`, and `cv2.putText`.

### `wrap_prespective.py`
Reads `resources/cards.jpg` and applies a perspective transform
(`cv2.getPerspectiveTransform` + `cv2.warpPerspective`) to extract and
straighten a card region into a 250x350 output image.

### `joining_img.py`
Loads `resources/lena.png` and stacks it with itself horizontally
(`np.hstack`) and vertically (`np.vstack`) to demonstrate image concatenation.

## Notes

- Image paths are inconsistent across scripts (`Resources/` vs `resources/`,
  and filenames like `lena.png`, `lambo.png`, `cards.jpg`) — make sure the
  referenced file exists at the path used before running a script.
- All scripts use `cv2.waitKey(0)` (or `cv2.waitKey(1)` for webcam) to keep
  the display window open; press any key (or `q` for webcam/video) to close.
- `.gitignore` excludes the local `.venv` virtual environment from version control.
