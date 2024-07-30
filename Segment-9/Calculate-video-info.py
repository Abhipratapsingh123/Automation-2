import cv2

video = cv2.VideoCapture('Segment-9/video.mp4')

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
nr_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))

print('width:', width, '\nheight:', height, '\nnumber of frames:', nr_frames,
      '\nfps:', fps)
