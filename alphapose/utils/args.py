import torch

sp = False
detector = "yolo"
save_img = False
vis = False
showbox = False
profile = False
min_box_area = 0
detbatch = 5
posebatch = 64
eval = False
gpus = "0"
qsize = 1024
flip = False
debug = False
webcam = -1
save_video = False
vis_fast = False
pose_flow = False
pose_track = False

gpus = [int(i) for i in gpus.split(',')] if torch.cuda.device_count() >= 1 else [-1]
device = torch.device("cuda:" + str(gpus[0]) if gpus[0] >= 0 else "cpu")
detbatch = detbatch * len(gpus)
posebatch = posebatch * len(gpus)
tracking = pose_track or pose_flow or detector=='tracker'

