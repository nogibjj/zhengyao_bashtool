# zhengyao_bashtool

## Project Workflow
![image](https://github.com/nogibjj/Zhengyao_proj1/blob/main/image.png)

## Test CLI
```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```

## Query Command
```
chmod +x db_process.py
./db_process.py cli-query
./db_process.py cli-query --query "YOUR QUERY CODE"
// "YOUR QUERY CODE" can be like "SELECT * FROM default.netflix1_csv LIMIT 2"
```

## Dataset
[dataset source](https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization)

## Show your query at web
```
python ./fastapi-app.py
```

## Customized Bash Command Line Tool
```
Data Cleaning: Query all works directed by one director
./db_process.py select-by-director
```
```
Data Sorting: Sort the query data based on released year in ascending order
./db_process.py sort-by-year
```

## Implement the Bash Tool
``` sh bashtool.sh
```