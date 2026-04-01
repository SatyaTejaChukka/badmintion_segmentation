# Model Benchmarks

| Model | Little Explanation | Pixel Accuracy | Parameters | Weight Size (MB) | Avg Inference Time (ms/frame) |
| --- | --- | --- | --- | --- | --- |
| `court_model.pth` | U-Net with ResNet-18 encoder for badminton court segmentation. | `99.48%` | `14.33M` | `54.76` | `76.64` |


## Calculation

- Pixel Accuracy = correct predicted pixels / total pixels = `12,191,205 / 12,255,232 = 99.48%`
- Parameters = total number of model parameters = `14,328,209 = 14.33M`
- Weight Size = model checkpoint size = `57,422,531 bytes / (1024 x 1024) = 54.76 MB`
- Avg Inference Time = total forward-pass time across all evaluated frames / number of frames = `14,332.11 ms / 187 = 76.64 ms/frame`
- Inference timing was measured on `CPU` with input resolution `256 x 256`
