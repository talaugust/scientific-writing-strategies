# Writing Strategies for Science Communication: Data and Computational Analysis

## Purpose
This repo holds code and data for the publication:

  Tal August, Lauren Kim, Katharina Reinecke, and Noah Smith ''Writing Strategies for Science Communication: Data and Computational Analysis'', Conference on Empirical Methods in Natural Language Processing (EMNLP) 2020.


## Prerequisites
Begin by creating a new virtual environment and installing required packages 
(here using [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html))

`conda env create -f environment.yml`

And activate it 

`conda activate sci_articles`


## Data

The urls of all scraped articles are in `data/cleaned_article_urls.csv` and all annotations made on these articles are in `data/annotations.csv`

The code for the scraper (including the parameters used to run the [scrapy](https://scrapy.org/) spider) are in the `scraper/` directory


## Getting the data

If you want the full text for each article, you can run the scraper with the parameters of the original paper. In the `scraper/` directory, run `python runSpiders.py all <FILEPATH>.jsonl` for wherever you want to store the files.

Note that this might take a few days to scrape all the data.

## Models 

We use the RoBERTa models from the [Huggingface transformers library](https://github.com/huggingface/transformers), pretraining and finetuning details are in the paper. Many of the scripts we use are adapted from the Huggingface example scripts, please refer to these for more details, specifically the scripts in `examples/text-classification/`.

If you are interested in getting access to the final finetuned models for classifying the writing strategies, feel free to reach out!  

## Annotation Interface

For the annotation interface, see the repo: https://github.com/talaugust/scientific_article_annotation/.
