import matplotlib.pyplot as plt

from scripts import read_data_file_as_csv, store_figure_as_jpg


def produce_literature_popularity_plot():
    df = read_data_file_as_csv('pubmed-timeline.csv')
    df = df[::-1]
    fig = plt.figure()
    df.plot.bar(x='Year', y='Count')
    plt.legend(['Papers mentioning pangenome'])
    store_figure_as_jpg(fig, 'literature-timeline.jpg')


if __name__ == '__main__':
    produce_literature_popularity_plot()
