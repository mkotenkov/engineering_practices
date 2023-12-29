

rule prepare_data:
    input: 
        "data/raw/data.csv",    
    output: 
        "data/processed/data.csv"        
    shell:
        "python3 project/prepare_data.py"


rule split_data:
    input: 
        "data/processed/data.csv",        
    output: 
        "data/splitted/train.csv",        
        "data/splitted/test.csv"
    shell:
        "python3 project/split_data.py"


rule grid_search:
    input:
        "data/splitted/train.csv",        
    output:
        "data/best_params.json"
    shell:
        "python3 project/grid_search.py" 
    

rule train:
    input: 
        "data/splitted/train.csv",        
    output: 
        "models/model.pkl"
    shell:
        "python3 project/train.py"


rule test:
    input:
        "models/model.pkl"
    output:
        "test_results.txt"
    shell:
        "python3 project/test.py"