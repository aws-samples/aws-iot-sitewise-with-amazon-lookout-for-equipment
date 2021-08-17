# Update the name of the bucket you want to use
# to store the intermediate results of this getting
# started:

BUCKET                   = '<<YOUR_BUCKET>>'
ASSET_ID                 = '<<ASSET_ID_FROM_SITEWISE_SIMULATOR_CF_STACK>>'

# You can leave these other parameters to these
# default values:

PREFIX_TRAINING          = f'{ASSET_ID}/training-data/'
PREFIX_LABEL             = f'{ASSET_ID}/label-data/'
PREFIX_INFERENCE         = f'{ASSET_ID}/inference-data'
DATASET_NAME             = f'{ASSET_ID}'
MODEL_NAME               = f'{DATASET_NAME}-model'
INFERENCE_SCHEDULER_NAME = f'{DATASET_NAME}-scheduler'