## EfficientDet

export PYTHONPATH="$PWD/src"

Execute all commands in **efficientdet/**


#### To run all tests:

* And run **python3 -m unittest**

#### To traing neural network

* **python3 train.py**

* Training will be logged with Tensorboard. To take a look at the training progress do: **tensorboard --logdir logs**

#### To test loaded model
* Notebook in example_prediction/example_prediction.py
* You need to set dataset path
* You need to set path to trained model

* path for notebook and python script are different
* execute python script from efficientdet/ with python3 example/efficient_det_d0.py

