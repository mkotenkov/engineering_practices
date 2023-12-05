from utils import load_csv, describe_df

if __name__ == '__main__':
    df = load_csv('data/train.csv')
    
    describe_df(df)
    