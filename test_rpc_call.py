import sys
sys.path.insert(0, 'Service/')

from client import ClientTest
from PIL import Image
import unittest

class TestSuiteGrpc(unittest.TestCase):
    def setUp(self):
    	self.image = Image.open('images/sample.png')
    	self.server = ClientTest()
    	self.result = Image.open("images/client_out.png")

    def test_grpc_call(self):
    	stub = self.server.open_grpc_channel()
    	result_image = self.server.send_request(stub,self.image)
    	assert Image.isImageType(result_image) == True

    def tearDown(self):
        # self.server.channel.close()
        pass



if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestSuiteGrpc("test_grpc_call"))
    unittest.main()