from kfp import dsl
from mlrun import mount_v3io

artifcats_path = './'
funcs = {}


def init_functions(functions: dict, params=None, secrets=None):
    '''
    This function will run before running the project.
    It allows us to add our specific system configurations to the functions
    like mounts or secrets if needed.

    In this case we will add Iguazio's user mount to our functions using the
    `mount_v3io()` function to automatically set the mount with the needed
    variables taken from the environment.

    @param functions: <function_name: function_yaml> dict of functions in the
                        workflow
    @param params: parameters for the function configurations
    @param secrets: secrets required for the functions for s3 connections and
                    such
    '''
    for f in functions.values():
        f.apply(mount_v3io())


@dsl.pipeline(
    name='Image classification demo',
    description='Train an Image Classification TF Algorithm using MLRun'
)
def kfpipeline(
        image_archive='http://iguazio-sample-data.s3.amazonaws.com/catsndogs.zip',
        images_path='/User/mlrun/examples/images',
        source_dir='/User/mlrun/examples/images/cats_n_dogs',
        checkpoints_dir='/User/mlrun/examples/checkpoints',
        model_path='/User/mlrun/examples/models/cats_n_dogs.h5',
        model_name='cat_vs_dog_v1'):
    # First we need to build our function containers
    builder_utils = funcs['utils'].deploy_step(with_mlrun=True)

    open_archive = funcs['utils'].as_step(name='download',
                                          handler='open_archive',
                                          out_path=images_path,
                                          params={'target_dir': images_path},
                                          inputs={'archive_url': image_archive},
                                          outputs=['content']).apply(
        mount_v3io())

    label = funcs['utils'].as_step(name='label',
                                   handler='categories_map_builder',
                                   out_path=images_path,
                                   params={'source_dir': source_dir},
                                   outputs=['categories_map',
                                            'file_categories']).after(
        open_archive)

    train = funcs['trainer'].as_step(name='train',
                                     params={'epochs': 3,
                                             'checkpoints_dir': checkpoints_dir,
                                             'model_path': model_path,
                                             'data_path': source_dir},
                                     inputs={'categories_map': label.outputs[
                                         'categories_map'],
                                             'file_categories': label.outputs[
                                                 'file_categories']},
                                     outputs=['model'])

    # deploy the model using nuclio functions
    deploy = funcs['serving'].deploy_step(project='nuclio-serving',
                                          models={
                                              model_name: train.outputs[
                                                  'model']})
