from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
api.dataset_download_files("jacksoncrow/stock-market-dataset", path="files", unzip=True)