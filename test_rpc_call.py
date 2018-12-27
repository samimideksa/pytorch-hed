import sys
sys.path.insert(0, 'Service/')

from client import ClientTest
from PIL import Image
import unittest
import numpy as np 


class TestSuiteGrpc(unittest.TestCase):
    def setUp(self):
    	self.image = Image.open('images/sample.png')
    	self.server = ClientTest()

    def test_grpc_call(self):
    	stub = self.server.open_grpc_channel()
    	result_image = self.server.send_request(stub,self.image)
    	result_image =  result_image.resize((480,320))
    	result_image.save("images/client_out2.png")

    	img_res = np.asarray(Image.open("images/client_out2.png").convert('L'))
    	img_expected = np.asarray(Image.open("images/client_out.png").convert('L'))
    	# print(img_res.shape,img_out.shape)
    	assert (img_res==img_expected).all()
    	

    def tearDown(self):
        # self.server.channel.close()
        pass



if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestSuiteGrpc("test_grpc_call"))
    unittest.main()