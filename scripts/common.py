import os

import matplotlib.pyplot as plt

import pandas as pd

DATA_DIR = os.path.join("..", "data")
FIGURES_DIR = os.path.join("..", "figures")


def store_figure_as_jpg(figure: plt.Figure, name: str) -> None:
    plt.savefig(os.path.join(FIGURES_DIR, name))


def read_data_file_as_csv(file: str) -> pd.DataFrame:
    return pd.read_csv(os.path.join(DATA_DIR, file))
