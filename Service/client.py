import os
import grpc
import edgedetect_pb2
import edgedetect_pb2_grpc
import base64

from PIL import Image
import  sys


from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

# from hed import Network ,estimate
import argparse

parser = argparse.ArgumentParser()



def open_drpc_channel(args):
	# open a gRPC channel
	channel = grpc.insecure_channel(args.port)

	stub = edgedetect_pb2_grpc.EdgedetectStub(channel)

	return stub
	



def send_request(args,stub):
	file_name = args.image_input
	out_file_name = args.image_output+'.png'

	img = Image.open(file_name).convert('L')
	img = img.resize((480,320))
	img_b = img.tobytes() 


	image_file = edgedetect_pb2.ImageFile(value = img_b)

	responce = stub.DetectEdge(image_file)

	image = Image.frombytes(data=responce.value,size=(480,320),mode='RGB')
	# image.convert('RGB').save(out_file_name, "PNG", optimize=True)

	return image



if __name__ == "__main__":
    parser.add_argument("--image_input",type=str,help='image path')
    parser.add_argument("--image_output",type=str,default='client_out',help='output image file name like "client_out"')
    parser.add_argument("--port",type=str,default='localhost:50051' ,help='port you are using like :   "localhost:50051" ')

    args = parser.parse_args()

    if len(sys.argv) == 1:
    	parser.print_help()
    	sys.exit()

    stub = open_drpc_channel(args)
    send_request(args,stub)
