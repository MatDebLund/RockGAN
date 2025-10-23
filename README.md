# Rock-GAN

This project implements a Generative Adversarial Network (GAN) for generating synthetic rock images, using **Keras** and **TensorFlow**. A kaggle dataset (https://www.kaggle.com/datasets/stealthtechnologies/rock-classification) is used for the training images with labels.

![Generated rock samples](figs/diatomite_training.gif)

![Real and fake samples](figs/real_fake.png)
## Contents
- `Rock_GAN_main.ipynb`: Jupyter notebook containing model architecture, training, and visualisation code.
- `requirements.txt`: List of dependencies for reproducibility.

## Installation
```bash
git clone https://github.com/MatDebLund/Rock-GAN.git
cd Rock-GAN
pip install -r requirements.txt
```
## Usage

Run the jupyter notebook, further explanations can be found inside it.
```bash
jupyter notebook Rock_GAN_main.ipynb
```
