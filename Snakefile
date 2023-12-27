rule prepare_data:
    input: 
        "data/raw/data.csv",    
    output: 
        "data/processed/data.csv"        
    shell:
        "python3 project/tasks/prepare_data.py"


rule split_data:
    input: 
        "data/processed/data.csv",        
    output: 
        "data/splitted/train.csv",
        "data/splitted/val.csv",
        "data/splitted/test.csv"
    shell:
        "python3 project/tasks/split_data.py"


rule grid_search:
    input:
        "data/processed/train.csv",
        "data/processed/val.csv"
    output:
        "data/best_params.json"
    shell:
        "python3 project/tasks/grid_search.py" 
    

# rule train:
#     input: 
#         "data/processed/train.csv",
#         "data/processed/test.csv"
#     output: 
#         "models/model.pkl"
#     script:
#         "project/tasks/train.py"