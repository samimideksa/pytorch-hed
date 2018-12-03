## gRPC service for reimplementation of [Holistically-Nested Edge Detection](https://arxiv.org/pdf/1504.06375) [1] using PyTorch


## setup

  - make sure you read the readme in the parent folder and installed all requirements 
  
## Installation 

      $ pip install grpcio
      $ pip install grpcio-tools
      
      
## Runnig Demo

  - you can find example code that sends image to the server and get the edge detection results back 


        python client.py [-h] [--image_input IMAGE_INPUT]
                       [--image_output IMAGE_OUTPUT] [--port PORT]

         optional arguments:
            -h, --help            show this help message and exit
            --image_input IMAGE_INPUT
                                  image path
            --image_output IMAGE_OUTPUT
                                  output image file name like "client_out"
            --port PORT           port you are using like : "localhost:50051" [The server must run on the port you specify ]
