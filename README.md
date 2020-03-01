# MLRun Image Classification 
## Demo project using Distributed Tensorflow on Horovod with Nuclio

This example is using TensorFlow, Horovod, and Nuclio demonstrating end to end solution for image classification, 
it consists of 4 MLRun and Nuclio functions and Kubeflow Pipelines Orchastration:

1. **Download**: import an image archive from S3 to the cluster file system
2. **Label**: Tag the images based on their name structure 
3. **Traing**: Distrubuted training using TF, Keras and Horovod
4. **Inference**: Automated deployment of Nuclio model serving function (form [Notebook](./notebooks/nuclio-serving-tf-images.ipynb) and from [Dockerfile](./inference-docker/Dockerfile))

<br><p align="center"><img src="workflow.png" width="600"/></p><br>

## Running the demo

The demo is written as an MLRun Project, allowing you to use the [load project](./load_project.ipynb) to run the project through the [main workflow](./src/workflow.py) as specified in the [project.yaml](./project.yaml)

Running the demo

**Pre-requisites:**

* A Kubernetes cluster with pre-installed KubeFlow, Nuclio. 
* MLRun Service and UI installed, see MLRun readme.

**Deployment Steps**
- Clone this repo to your own Git. 
- in a client or notebook properly configured with MLRun and KubeFlow run:  

`mlrun project my-proj/ -u git://github.com/<your-fork>/demo-image-classification.git`  

3. Run the [local playground notebook](./notebooks/mlrun_mpijob_classify.ipynb) to build, test, and run functions.

4. Open the [project notebook](./notebooks/mlrun_mpijob_pipe) and follow the instructions to run an automated ML Pipeline and source control.

> Note: alternatively you can run the `main` pipeline from the CLI and specify artifacts path using:

`mlrun project my-proj/ -r main -p "v3io:///users/admin/kfp/{{workflow.uid}}/"`

## Notebooks & Code

* [All-in-one: Import, tag, launch training, deploy serving](mlrun_mpijob_classify.ipynb) 
* [Training function code](./py/horovod-training.py)
* [Serving function development and testing](./notebooks/nuclio-serving-tf-images.ipynb)
* [Auto generation of KubeFlow pipelines workflow](./notebooks/mlrun_mpijob_pipe.ipynb)
* [Building serving function using Dockerfile](./inference-docker)
  * [function code](./inference-docker/main.py)
  * [Dockerfile](./inference-docker/Dockerfile)

