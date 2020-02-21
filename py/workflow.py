from mlrun import mount_v3io


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
