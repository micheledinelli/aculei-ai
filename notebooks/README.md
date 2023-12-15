This is a simple guide in order to execute the notebooks correctly

It is possible to run them in any environmnet supporting `.ipynb` files with a python kernel.

It is mandatory to have the images downloaded placed in this repository root folder under `./images` folder. Images are not provided in this repository because the file size is not supported on gitlab (> 30GB). We'll provide the data upon request with different zip files.

Execution order

1. **[metadata.ipynb](metadata.ipynb)**

> This notebook sets up the dataframe reading the images folder and extraxcts the metadata from them. It creates [metadata.csv](../datasets/metadata.csv) at the end of the execution.

2. **[ocr.ipynb](ocr.ipynb)**

> This notebook uses ocr to read missing data. It creates [ocr.csv](../datasets/ocr.csv) at the end of the execution. `ocr.csv` fills the gap of `metadata.csv`.

3. **[meld.ipynb](meld.ipynb)**

> This notebook merges results from metadata.ipynb and ocr.ipynb to obtain the final dataset. It checks for duplicate images, and checks the data produced with ocr. It creates [aculei.csv](../datasets/aculeiß.csv)

4. **[insights.ipynb](insights.ipynb)**

> This notebook uses matplotlib and seaborn to visualize data and give some insights
