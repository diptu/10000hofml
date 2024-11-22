# 100 Days of ML
- daily ML Practice

# Certification:

## Convolutional Neural Networks:

### Day 001: Edge Detection
**NxN matrices are convolved by FxF filter/kernel; the output would be (N-F+1) by (N-F+1) matrices.**
- e.g., a 6x6 matrix is convolved by a 3x3 filter; the output would be a 4x4 matrix.
- F should always be odd, e.g., 3, 5, 7...
- This process shrinks the image.
- Information from corner/edge points is discarded.

## Limitation:
- Images shirinks
- Pixels in the edges are considered less than in the middle of the image.

1. **valid convolution**: No Padding
2. **same convolution**: Output image and input image size are equal.
## Padding
- By convention, padding is done with zeros.
**NxN matrices are convolved by FxF filter/kernel with padding of p; the output would be (N+2p-F+1) by (N+2p-F+1) matrices.**
- e.g., a 6x6 matrix is convolved by a 3x3 filter with padding of 1; the output would be a 6x6 matrix.
  - *Valid:* No padding (Image shrinks).
  - *Same:* p = (F-1)/2 (Retain original shape).

### Stride
**NxN matrices are convolved by FxF filter/kernel with padding of p and stride of S; the output would be `floor((N+2p-F)/S) + 1` by `floor((N+2p-F)/S) + 1` matrices.**
- e.g., a 6x6 matrix is convolved by a 3x3 filter with padding of 1 and strided with 2; the output would be a 3x3 matrix.
- e.g., a 7x7 matrix is convolved by a 3x3 filter with padding of 1 and strided with 2; the output would be a 4x4 matrix.