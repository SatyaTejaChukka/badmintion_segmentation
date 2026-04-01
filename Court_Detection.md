# Model Benchmark

| Model | Little Explanation | Pixel Accuracy | Parameters | Weight Size (MB) | Avg Inference Time (ms/frame) |
| --- | --- | --- | --- | --- | --- |
| [`court_model.pth`](https://github.com/SatyaTejaChukka/badmintion_segmentation/blob/main/court_model.pth) | U-Net with a ResNet-18 encoder used to segment the badminton court area from each frame. | `99.48%` | `14.33M` | `54.76` | `76.64` |

## How Each Value Is Calculated

### Pixel Accuracy

Pixel accuracy is computed by comparing the predicted binary mask with the ground-truth binary mask for every pixel in the evaluation set.

Formula:

`Pixel Accuracy = Correctly Predicted Pixels / Total Pixels`

Numbers used:

- Correctly predicted pixels = `12,191,205`
- Total pixels = `12,255,232`
- Calculation = `12,191,205 / 12,255,232 = 0.994775537501`
- Final value reported = `99.48%`

The total pixel count comes from `187` evaluation images, each resized to `256 x 256`.

`187 x 256 x 256 = 12,255,232`

### Parameters

Parameters are calculated as the total number of learnable values in the model.

Numbers used:

- Total parameters = `14,328,209`
- Final value reported = `14.33M`

### Weight Size

Weight size is the size of the saved checkpoint file on disk.

Formula:

`Weight Size (MB) = File Size in Bytes / (1024 x 1024)`

Numbers used:

- Checkpoint file size = `57,422,531 bytes`
- Calculation = `57,422,531 / 1,048,576 = 54.762393 MB`
- Final value reported = `54.76 MB`

### Average Inference Time

Average inference time is measured by timing only the model forward pass for each evaluation image after resizing it to `256 x 256`, and then averaging that time over the full evaluation set.

Formula:

`Average Inference Time = Total Forward-Pass Time / Number of Evaluated Frames`

Numbers used:

- Total evaluated frames = `187`
- Total forward-pass time = `14,332.11 ms`
- Calculation = `14,332.11 / 187 = 76.64 ms/frame`
- Final value reported = `76.64 ms/frame`
- Device used for this measurement = `CPU`

This timing refers to the segmentation model prediction step only. It does not include file loading, display time, or GitHub screenshot rendering.

## What the Inference Output Shows

The inference output shown by the test pipeline is the final visual result after prediction and post-processing.

Step by step:

1. A video frame is resized to `256 x 256` and passed into the model.
2. The model predicts a single-channel mask for the court region.
3. A sigmoid is applied to convert raw output logits into probabilities.
4. A threshold of `0.5` is applied to convert the probability map into a binary mask.
5. The binary mask is resized back to the original frame size.
6. Morphological cleanup is applied to remove noise and fill small gaps.
7. The largest valid court contour is selected from the cleaned mask.
8. Four court corners are estimated from the contour and refined using fitted edge lines.
9. The final frame is rendered with:

- A green overlay showing the predicted court segmentation area
- A red polygon showing the detected court boundary
- Four labeled corner points: `TL`, `TR`, `BR`, `BL`

## Important Note About Runtime Display

The displayed test output in [`test_seg_model.py`](https://github.com/SatyaTejaChukka/badmintion_segmentation/blob/main/test_seg_model.py) is optimized for smoother viewing:

- `SOURCE_FRAME_STRIDE = 2` means every second source frame is processed from the video.
- `INFERENCE_FRAME_STRIDE = 4` means model inference is not run on every processed frame.
- On skipped frames, the previous mask and corner estimate are reused.

Because of that, the live demo behavior and the benchmark value `76.64 ms/frame` should not be treated as exactly the same measurement. The benchmark value is the average model forward-pass time measured separately across the evaluation images.

## Test Output Screenshots

The two screenshots below are sample frames captured from the same output while running `test_seg_model.py`.

![Inference Output Frame 1](https://raw.githubusercontent.com/SatyaTejaChukka/badmintion_segmentation/main/Screenshot_1.png)

![Inference Output Frame 2](https://raw.githubusercontent.com/SatyaTejaChukka/badmintion_segmentation/main/Screenshot_2.png)

### Test Video Result

Click the thumbnail below to open the test video result.

[![Test Video Thumbnail](https://raw.githubusercontent.com/SatyaTejaChukka/badmintion_segmentation/main/Screenshot_1.png)](https://github.com/SatyaTejaChukka/badmintion_segmentation/blob/main/Court_detection.mp4)
