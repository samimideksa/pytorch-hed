# pytorch-hed
This is implementation of Holistically-Nested Edge Detection [1] using PyTorch. Should you be making use of this work, please cite the paper accordingly. Also, make sure to adhere to the licensing terms of the authors. Should you be making use of this particular implementation, please acknowledge it appropriately.

<a href="https://arxiv.org/abs/1504.06375" rel="Paper"><img src="http://www.arxiv-sanity.com/static/thumbs/1504.06375v2.pdf.jpg" alt="Paper" width="100%"></a>

For the original version of this work, please see: https://github.com/s9xie/hed
<br />
For another reimplementation based on Caffe, please see: https://github.com/zeakey/hed

## Requirement
	To install requirements for the project 
	$ pip install -r requirements.txt
	
	$ pip install grpcio
	$ pip install grpcio-tools
         

## Setup
To download the pre-trained models, run `bash download.bash`. These originate from the original authors, I just converted them to PyTorch.

- run the following command to generate gRPC classes for Python
    
      $python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. Service/edgedetect.proto

## Usage
To run it on your own image, use the following command. Please make sure to see their paper / the code for more details.


	#to test the service
	$ cd Service

	#this will start the server 
	$ python Service/server.py



	#on other terminal run 
	$ python Service/client.py [-h] [--image_input IMAGE_INPUT]
                       [--image_output IMAGE_OUTPUT] [--port PORT]

         optional arguments:
            -h, --help            show this help message and exit
            --image_input IMAGE_INPUT
                                  image path
            --image_output IMAGE_OUTPUT
                                  output image file name like "client_out"
            --port PORT           port you are using like : "localhost:50051" [The server must run on the port you specify ]






 It achieves an ODS=0.774  on the BSDS500 dataset, evaluated using [this code](https://github.com/zeakey/edgeval). Please feel free to contribute to this repository by submitting issues and pull requests.

## Comparison
<p align="center"><img src="comparison/comparison.gif?raw=true" alt="Comparison"></p>

## References
```
[1]  @inproceedings{Xie_ICCV_2015,
         author = {Saining Xie and Zhuowen Tu},
         title = {Holistically-Nested Edge Detection},
         booktitle = {IEEE International Conference on Computer Vision},
         year = {2015}
     }
```
