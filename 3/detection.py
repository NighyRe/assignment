#from jetson_inference import detectNet
#from jetson_utils import videoSource, videoOutput
import jetson_inference
import jetson_utils

net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
#camera = jetson_utils.videoSource("/dev/video0")
camera = jetson_utils.videoSource("/home/nvidia/jetson-inference/python/training/detection/ssd/data/fruit/train/0bc9985844755dc3.jpg")
display = jetson_utils.videoOutput("display://0")

while display.IsStreaming():
  img = camera.Capture()

  if img is None:
    continue

  detections = net.Detect(img)
  print(detections)

  display.Render(img)
  import pdb;pdb.set_trace()
  display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
  
