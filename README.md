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

> The demo applications are tested on the [Iguazio's Data Science PaaS](https://www.iguazio.com/), 
and use Iguazio's shared data fabric (v3io), and can be modified to work with any shared file storage by replacing the 
```apply(v3io_mount())``` calls with other KubeFlow volume modifiers (e.g. `apply(mlrun.platforms.mount_pvc())`) . 
You can request a [free trial of Iguazio PaaS](https://www.iguazio.com/lp/14-day-free-trial-in-the-cloud/).

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

* [All-in-one: Import, tag, launch training, deploy serving](./notebooks/mlrun_mpijob_classify.ipynb) 
* [Training function code](./py/horovod-training.py)
* [Serving function development and testing](./notebooks/nuclio-serving-tf-images.ipynb)
* [Auto generation of KubeFlow pipelines workflow](./notebooks/mlrun_mpijob_pipe.ipynb)
* [Building serving function using Dockerfile](./inference-docker)
  * [function code](./inference-docker/main.py)
  * [Dockerfile](./inference-docker/Dockerfile)

