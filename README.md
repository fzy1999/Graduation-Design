

## Background

复现了
paper ["Arrow R-CNN for handwritten diagram recognition" by Bernhard Schäfer](https://link.springer.com/article/10.1007/s10032-020-00361-1).


## Training data


dataset [bernhardschaefer/handwritten-diagram-datasets](https://github.com/bernhardschaefer/handwritten-diagram-datasets).

### Structure

仓库结构

```
.
├── data                                            # Data folder
├── models                                          # Model folder
├── notebooks                                       # Jupyter notebooks
│   ├── predictions.ipynb                           # Notebook for recognizing a single image
│   ├── analyse_dataset.ipynb                       # Notebook for analysing training data
│   ├── model_trainer.ipynb                         # Notebook for training models
│   ├── evaluation.ipynb                            # Notebook for evaluating models
│   └── simple_compare.ipynb                        # Notebook for comparing models directly
├── references                                      # Reference material
├── reports                                         # Evaluation reports
├── requirements.txt                                # Python requirements
└── src                                             # Source code
    ├── dataset                                     # Code for loading the dataset
    ├── sketch_detection_rcnn                       # Custom detectron2 model
    ├── utils                                       # Utility functions
    └── visualization                               # Visualization functions
```

## Implementing Network Architecture

本项目基于detectron2 进行复现

### Arrow R-CNN

Bernhard Schäfer 提出的 Arrow R-CNN 模型在 src/sketch_detection_rcnn 文件夹中实现。该模型基于 Faster R-CNN 模型，并在 ROI 头部添加了一个关键点回归层


