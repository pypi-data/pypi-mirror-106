## EfficientDet

Start with following command:

```python
export PYTHONPATH="$PWD/src"
```

All commands should be executed in **efficientdet/**.

#### To test trained model on validation dataset you can use the jupyter notebook or python script in examples/.
```python
For your own implementation set the dataset path and path to the trained model. Default paths are set to efficient/dataset.
```

#### To run all tests:
```python
python3 -m unittest
```

#### To train neural network
```python
python3 src/efficient_det/train.py --dataset_path /path/to/dataset/
```


When using Ray Tune verbose is default set to False. Use W&B for visualization.


