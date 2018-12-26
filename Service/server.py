import grpc
from concurrent import futures
import time

import edgedetect_pb2
import edgedetect_pb2_grpc

import edgedetect

class EdgedetectServicer(edgedetect_pb2_grpc.EdgedetectServicer):
	def DetectEdge(self,request,context):
		print("request recived")
		responce = edgedetect_pb2.ImageFile()
		responce.value = edgedetect.detectedge(request.value)
		return responce



server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
edgedetect_pb2_grpc.add_EdgedetectServicer_to_server(EdgedetectServicer(),server)



# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)