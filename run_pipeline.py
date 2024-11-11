from zenml.client import Client

from pipelines.training_pipeline import train_pipeline


if __name__ == "__main__":
    # Run the pipeline
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    train_pipeline(data_path="C:/Users/balde/OneDrive/Bureau/DA_DS/customer-satisfaction-mlops-main/Project_MLops_Customer_Satisfaction/data/olist_customers_dataset.csv")
    # Read the data with pandas, specifying index_col and parse_dates
    
    
    # import pandas as pd

    # data_path = "C:/Users/balde/OneDrive/Bureau/DA_DS/customer-satisfaction-mlops-main/Project_MLops_Customer_Satisfaction/data/olist_customers_dataset.csv"
    
    # df = pd.read_csv(data_path, sep=",", header=0, encoding='utf-8')
    # print(df.columns)