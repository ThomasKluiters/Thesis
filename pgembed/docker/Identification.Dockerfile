FROM continuumio/miniconda3

COPY pgembed/environment.yml .
RUN conda env create -f environment.yml
RUN conda activate myenv

RUN prodigal -v
