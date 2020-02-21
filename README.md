# Image Classification Using Distributed Training

This example is using TensorFlow, Horovod, and Nuclio demonstrating end to end solution for image classification, 
it consists of 4 MLRun and Nuclio functions:

1. import an image archive from S3 to the cluster file system
2. Tag the images based on their name structure 
3. Distrubuted training using TF, Keras and Horovod
4. Automated deployment of Nuclio model serving function (form [Notebook](./notebooks/nuclio-serving-tf-images.ipynb) and from [Dockerfile](./inference-docker/Dockerfile))

<br><p align="center"><img src="workflow.png" width="600"/></p><br>

The Example also demonstrate an [automated pipeline](./notebooks/mlrun_mpijob_pipe.ipynb) using MLRun and KubeFlow pipelines 

## Notebooks & Code

* [All-in-one: Import, tag, launch training, deploy serving](mlrun_mpijob_classify.ipynb) 
* [Training function code](./py/horovod-training.py)
* [Serving function development and testing](./notebooks/nuclio-serving-tf-images.ipynb)
* [Auto generation of KubeFlow pipelines workflow](./notebooks/mlrun_mpijob_pipe.ipynb)
* [Building serving function using Dockerfile](./inference-docker)
  * [function code](./inference-docker/main.py)
  * [Dockerfile](./inference-docker/Dockerfile)

