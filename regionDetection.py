'''
Do not Change these imports!  
'''
import sys
import cv2
import grpc
import json
import logging
from concurrent import futures
sys.path.append("/usr/app/src/grpc_compiled") # Used when in docker
sys.path.append("./grpc_compiled")
from grpc_compiled import CameraSrv_pb2
from grpc_compiled import CameraSrv_pb2_grpc

# Space for Additional Imports



# End of import space 

# Declare variables 
MIN_EDGES = 5
PRECISION = 0.01
THRESHOLD = 120

PORT = 50099
ALIAS = "Paul McHard"

# End of Variables

class RegionDetectionService(CameraSrv_pb2_grpc.CameraSrvServicer):
   """
   Provides methods which implement the functionality of the Region detection server.
   """
   ### CORE ALGORITHM ###
   def find_regions(self, img : cv2.Mat, min_edges : int, precision : float, binaryThreshold : int) -> tuple[list, list]:

      """
      Finds closed contours in a black and white image.

      Args:
          image: A grayscale image.
          min_edges: Minimum number of edges to be found in a region to count it as not being noise
          precision: Fine tuning for how closely we trim the edges of a region

      Returns:
          A list of regions, where each region is a list of (x, y) coordinates corresponding to the vertices of that region.
      """
      # Convert the image to grayscale in case it's not already.
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      # Apply thresholding to convert the grayscale image to a binary image.
      thresh = cv2.threshold(gray, binaryThreshold, 255, cv2.THRESH_BINARY_INV)[1]
      # Find contours in the thresholded image.
      contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

      # Filter for closed contours
      vertex_set = []
      closed_polylines = []
      for contour in contours:
         contour_points = []
         # Approximate the contour with polygons
         perimeter = cv2.arcLength(contour, True)
         approx_polyline = cv2.approxPolyDP(contour, precision * perimeter, True)
         # If an obtained contour has fewer than the min edge count, we can discard as noise.
         if len(approx_polyline) < min_edges: 
            continue
       
         closed_polylines.append(approx_polyline)
         #approxPolyDP returns a different vector structure, to we need to reformat slightly for our function.
         for point in approx_polyline:
            contour_points.append(point[0])
         # Add the vertices of the contour to the list of closed regions
         vertex_set.append(contour_points)

      # Return the list of closed regions
      return closed_polylines, vertex_set

   ### ADD YOUR CUSTOM FUNCTION HERE 

   def format_json(self, regions):
      '''
         Format the generated region data into a JSON payload which can be handled correctly by the simulation.
         YOU DO NOT NEED TO CHANGE THIS FUNCTION
      '''
      formatted_string = []
      for region in regions:
         region_strings = []
         for point in region:
            # Convert each point to a comma-separated string "[x, y]"
            region_strings.append("[{:.6f}, {:.6f}]".format(point[0], point[1]))
         formatted_string.append("[{}]".format(",".join(region_strings)))
      return "[{}]".format(",".join(formatted_string))

   def TryTriggerCamera(self, request, context):
      '''
         Main function of Region Detection service gRPC server. 
         This is the function which is called remotely by the gRPC Client.
         YOU DO NOT NEED TO CHANGE THIS FUNCTION, EXCEPT WHERE EXPLICTLY TOLD
      '''
      get_module_logger().info("Received new request...")
      request_settings = json.loads(request.settings)
      request_image = request_settings["Image"]
      get_module_logger().info("Request received to address: {0}".format(request_image))
      img_file = 'data/'
      if request_image.endswith("test0"):
         img_file = img_file + "test0.png"
      elif request_image.endswith("test1"):
         img_file = img_file + "test1.png"
      elif request_image.endswith("test2"):
         img_file = img_file + "test2.png"
      elif request_image.endswith("test3"):
         img_file = img_file + "test3.png"
      else: #default is "dummy"
         img_file = img_file + "test0.png"
      
      image = cv2.imread(img_file)
      get_module_logger().info("finding regions in {0}".format(img_file))
      # Replace this line with your own function... if you dare!
      polylines, vertices = self.find_regions(image.copy(), min_edges=MIN_EDGES, precision=PRECISION, binaryThreshold=THRESHOLD) 
      
      get_module_logger().info("Formatting region data as JSON payload...")
      payload = self.format_json(vertices)
      return CameraSrv_pb2.CameraResponse(payload = payload, success = True, alias=ALIAS)
  
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  CameraSrv_pb2_grpc.add_CameraSrvServicer_to_server(RegionDetectionService(), server)
  server.add_insecure_port('[::]:{0}'.format(PORT))  # Replace with desired port
  server.start()
  server.wait_for_termination()

def get_module_logger():
  logger = logging.getLogger(__name__)
  handler = logging.StreamHandler()
  formatter = logging.Formatter(
      '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  logger.setLevel(logging.DEBUG)
  return logger
    
if __name__ == '__main__': #run test
   get_module_logger().info("Starting region detection server on port {0} for user {1}".format(PORT, ALIAS))
   serve()