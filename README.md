# pytorch-hed
This is implementation of Holistically-Nested Edge Detection [1] using PyTorch. Should you be making use of this work, please cite the paper accordingly. Also, make sure to adhere to the licensing terms of the authors. Should you be making use of this particular implementation, please acknowledge it appropriately.

<a href="https://arxiv.org/abs/1504.06375" rel="Paper"><img src="http://www.arxiv-sanity.com/static/thumbs/1504.06375v2.pdf.jpg" alt="Paper" width="100%"></a>

For the original version of this work, please see: https://github.com/s9xie/hed
<br />
For another reimplementation based on Caffe, please see: https://github.com/zeakey/hed

## Setup
To download the pre-trained models, run `bash download.bash`. These originate from the original authors, I just converted them to PyTorch.

## Usage
To run it on your own image, use the following command. Please make sure to see their paper / the code for more details.

```
		#to test the service
		cd Service

		#this will start the server 
		python server.py



		#on other terminal run 
		python client.py --image_input "a.jpg"

```

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
