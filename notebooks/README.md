This is a simple guide in order to execute the notebooks correctly

It is possible to run them in any environmnet supporting `.ipynb` files with a python kernel.

Execution order

1. metadata_extraction.ipynb

`This notebooks sets up the dataframe reading the images folder and extracting the metadata from them. It creates aculei.csv file at the end of the execution.`

2. ocr.ipynb

`This notebook uses ocr to read missing data and filling the aculei.csv dataset.`

3. data_visualization.ipynb

`This notebook uses matplotlib and seaborn to visualize data and gives some insights`
