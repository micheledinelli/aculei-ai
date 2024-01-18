This is a simple guide in order to execute the notebooks correctly

It is possible to run them in any environmnet supporting `.ipynb` files with a python kernel.

It is mandatory to have the images downloaded placed in this repository root folder under `./images` folder. Images are not provided in this repository because the file size is not supported on gitlab (> 30GB). We'll provide the data upon request with different zip files.

Execution order

1. **[metadata.ipynb](metadata.ipynb)**

> This notebook sets up the dataframe reading the images folder and extraxcts the metadata from them. It creates [metadata.csv](../datasets/metadata.csv) at the end of the execution.

2. **[ocr_1.ipynb](ocr_1.ipynb)**

> This notebook uses ocr `pytesseract` to read missing data. It creates [ocr.csv](../datasets/ocr.csv) at the end of the execution. `ocr.csv` fills the gap of `metadata.csv`.

3. **[ocr_2.ipynb](ocr_2.ipynb)**

> This notebook processes [ocr.csv](../datasets/ocr.csv) to add antoher pipeline step. It refines the results obtained from ocr_1.ipynb using `easyocr` python library.

4. **[meld.ipynb](meld.ipynb)**

> This notebook merges results from metadata.ipynb and ocr.ipynb to obtain the final dataset. It checks for duplicate images, and checks the data produced with ocr. It creates [aculei.csv](../datasets/aculei.csv)

5. **[insights.ipynb](insights.ipynb)**

> This notebook uses matplotlib and seaborn to visualize data and some insights

6. **[zero-shot-image-classification.ipynb](zero-shot-image-classification.ipynb)**

> This notebook uses huggingface model to produce labels for animals

7. **[clustering-one-hot-encoded.ipynb](clustering/clustering-one-hot-encoded.ipynb)**

> This notebook uses unsupervised learning algorithms such as [KMeans](https://it.wikipedia.org/wiki/K-means) to cluster similar images using the dataset we built. This clustering version analyzes data using [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis) and the dataset used only categorical data translated using one-hot-encoding. We evaluated KMeans performances using both [euclidian distance implentation and manhattan distance implementation](https://towardsdatascience.com/log-book-guide-to-distance-measuring-approaches-for-k-means-clustering-f137807e8e21).
