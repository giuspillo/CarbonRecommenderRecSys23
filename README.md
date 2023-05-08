# CarbonRecommenderRecSys23
Source code and datasets for the paper "Towards Sustainability-aware Recommender Systems: Analyzing the Trade-off Between Algorithms Performance and Carbon Footprint"

### Requirements
* RecBole 1.1.1: https://recbole.io/
* CodeCarbon: https://codecarbon.io/
* Pytorch

If you should need more info about the requirements, 'req.txt' is the output of the 'pip freeze' command for the conda environment used for these experiments.

### Python scripts

* 'script.py' launches the training for each dataset and for each model
* 'full_model.py' executes the training of the selected model on the selected dataset if no results have been computed for that setting, while keeping track of emissions during the training; then, it saves the results on a 'results' folder (which must be created).

## Datasets

* 'dataset/' contains the three datasets used for this experiment:
    * movielens 1m: dataset about movies, already splitted into train, validation, and test set. knowledge data is available for this dataset.
    * mind: dataset about news. to repliacate our experiments, set 'repeatable' to 'True' in the recbole parameter dict. no knowledge data is available for this dataset.
    * amazon books: dataset about books. to repliacate our experiments, set 'repeatable' to 'True' in the recbole parameter dict. knowledge data is available for this dataset.

RecBole 1.1.1 has been used: https://recbole.io/

CodeCarbon has been used:https://codecarbon.io/

Dataset have been preprocessed by us, and original version can be found here: https://github.com/RUCAIBox/RecSysDatasets


## Results

Graphical results obtained and described in the original paper.
Full results available in the 'results.xlsx' file.

### Mind
![](/graphs/sum_mind_dataset.png | width=300)

