import torch
# import torch.utils.serialization

import getopt
import math
import numpy
import os
import PIL
import PIL.Image
import sys
import base64

from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from hed import Network ,estimate

Model = '../network-bsds500.pytorch'

train_on_gpu = torch.cuda.is_available()




def detectedge(image_in):
	image = PIL.Image.frombytes(data=image_in,size=(480,320),mode='RGB')
	if train_on_gpu:
		moduleNetwork = Network(Model).cuda().eval()
	else:
		moduleNetwork = Network(Model).cuda().eval()

	tensorInput = torch.FloatTensor(numpy.array(image)[:, :, ::-1].transpose(2, 0, 1).astype(numpy.float32) * (1.0 / 255.0))
	tensorOutput = estimate(tensorInput,moduleNetwork)
	img_out = PIL.Image.fromarray((tensorOutput.clamp(0.0, 1.0).detach().numpy().transpose(1, 2, 0)[:, :, 0] * 255.0))
	# img_out.convert('RGB').save('server_out.png', "PNG", optimize=True)
	# print("output",img_out.size)
	img = img_out.convert('RGB').tobytes() 
	return img


