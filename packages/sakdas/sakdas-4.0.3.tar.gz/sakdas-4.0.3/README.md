# Acknowledgment
This package is a part of the Master of Science Program in Applied Statistics (Business Analytics and Intelligence: BA&I), National Institute of Development Administration(NIDA), Thailand

## Version 2.8.12
Sakdas is a data profiling and auditing package based on statistical methods.

Its primary goals are to provide self-service data profiling to understand the data via statistical and visualization and data auditing to audit the data via a predefined condition.
## Features
1. Analyze the data profile based on statistical methods and visualization
2. Audit the data by using a predefined condition.
3. Provide audited dataset(CSV) with auditing result tag or without tag, duplicated dataset.
4. Generate data profiling and auditing reports.

## Installation
```
pip install pandas
pip install matplotlib
pip install sakdas
```
## Upgrade
```
pip install sakdas --upgrade
```
## Profiling Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')

get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>')

```
## Auditing Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')

auditing_config = {'audit':{
    'audit_missing_value': False,
    
    'audit_data_pattern':[
                {'column_name':'Gender', 'regex_pattern': '(Female|Male)'},
                {'column_name':'Invoice_ID', 'regex_pattern': '(^[0-9]{3}-[0-9]{2}-[0-9]{4})'}
            ],
    'audit_outlier': False,

    'audit_data_range' : [{'column_name':'Quantity', 'min': 0, 'max': 100}]
    }
}
sample_supermarket_sales = sd(
    df,'sample_supermarket_sales','<Path-to-Result>', 
    auditing_config = auditing_config)

```
## Sakda Methods
|Methods|Return|
|---|---|
|dataset = sd(Path to CSV file)|dataset object and profiling report|
|dataset.audit(audit_config)|data profiling and auditing report|
    
## Sakda Attributes
## Attrubutes: sakda.dataset_name
#### Return type: String
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>')

print(get_profile.dataset_name)
```
#### Output
```
sample_supermarket_sales
```
## Attrubute: sakda.df
#### Return type: pandas.core.frame.DataFrame
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>')

print(get_profile.df)
```
#### Output
```
Example data in DataFrame
```
## Attrubute: sakda.duplicated_record
#### Return type: pandas.core.frame.DataFrame
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>')

print(get_profile.duplicated_record)
```
#### Output
```
Example duplicated data in DataFrame
```

## Attrubute: sakda.schema
#### Return type: list
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>')

print(get_profile.schema)
```
#### Output
```
===Schema===
Invoice_ID: object
Branch: object
City: object
Customer_type: object
Gender: object
Product_line: object
Unit_price: float64
Quantity: int64
Tax: float64
Total: float64
Date: object
Time: object
Payment: object
cogs: float64
gross_margin_percentage: float64
gross_income: float64
Rating: float64
```

## Attrubute: sakda.schema_json
#### Return type: list
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>')

print(get_profile.schema_json)
```
#### Output
```
[{'columnName': 'Invoice_ID', 'dataType': 'object'}, {'columnName': 'Branch', 'dataType': 'object'}, {'columnName': 'City', 'dataType': 'object'}, {'columnName': 'Customer_type', 'dataType': 'object'}, {'columnName': 'Gender', 'dataType': 'object'}, {'columnName': 'Product_line', 'dataType': 'object'}, {'columnName': 'Unit_price', 'dataType': 'float64'}, {'columnName': 'Quantity', 'dataType': 'int64'}, {'columnName': 'Tax', 'dataType': 'float64'}, {'columnName': 'Total', 'dataType': 'float64'}, {'columnName': 'Date', 'dataType': 'object'}, {'columnName': 'Time', 'dataType': 'object'}, {'columnName': 'Payment', 'dataType': 'object'}, {'columnName': 'cogs', 'dataType': 'float64'}, {'columnName': 'gross_margin_percentage', 'dataType': 'float64'}, {'columnName': 'gross_income', 'dataType': 'float64'}, {'columnName': 'Rating', 'dataType': 'float64'}]
```



## Attrubute: sakda.profile
#### Return type: dict
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>')

print(get_profile.profile)
```
#### Output
```
{'profile_engine': 'sakdas beta version 0.2.15', 'profile_id': 'b6e810ab-701f-489d-ac58-98515b021159', 'file_name': 'sample_supermarket_sales', 'profile_datetime': '23/09/2020 10:52:47', 'total_record': 1000, 'total_record_after_deduplication': 1000, 'duplicated_data': '0', 'primary_key': 'Invoice_ID', 'total_column': 17, 'completed_record': '1000', 'completed_record_ratio': '1.0', 'blank_column': 0, 'missing_condition': 'null', 'missing_data': '0', 'missing_data_ratio': '0.0', 'schema': '===Schema===\nInvoice_ID: object\nBranch: object\nCity: object\nCustomer_type: object\nGender: object\nProduct_line: object\nUnit_price: float64\nQuantity: int64\nTax: float64\nTotal: float64\nDate: object\nTime: object\nPayment: object\ncogs: float64\ngross_margin_percentage: float64\ngross_income: float64\nRating: float64', 'column_profile': {'Invoice_ID': {'dataType': 'object', 'is_primary_key': 'True', 'distinct_value': '1000', 'ratio_distinct_value': '1.0', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '11', 'data_lenght_max': '11', 'top_5_data_value': [{'data_value': '101-17-6199', 'count_data_value': '1', 'value_ratio': '0.001'}, {'data_value': '641-62-7288', 'count_data_value': '1', 'value_ratio': '0.001'}, {'data_value': '633-91-1052', 'count_data_value': '1', 'value_ratio': '0.001'}, {'data_value': '634-97-8956', 'count_data_value': '1', 'value_ratio': '0.001'}, {'data_value': '635-28-5728', 'count_data_value': '1', 'value_ratio': '0.001'}], 'top_5_data_pattern': [{'pattern': 'XXX-XX-XXXX', 'count_pattern': '1000', 'pattern_ratio': '1.0'}]}, 'Branch': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '3', 'ratio_distinct_value': '0.003', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '1', 'data_lenght_max': '1', 'top_5_data_value': [{'data_value': 'A', 'count_data_value': '340', 'value_ratio': '0.34'}, {'data_value': 'B', 'count_data_value': '332', 'value_ratio': '0.332'}, {'data_value': 'C', 'count_data_value': '328', 'value_ratio': '0.328'}], 'top_5_data_pattern': [{'pattern': 'X', 'count_pattern': '1000', 'pattern_ratio': '1.0'}]}, 'City': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '3', 'ratio_distinct_value': '0.003', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '6', 'data_lenght_max': '9', 'top_5_data_value': [{'data_value': 'Yangon', 'count_data_value': '340', 'value_ratio': '0.34'}, {'data_value': 'Mandalay', 'count_data_value': '332', 'value_ratio': '0.332'}, {'data_value': 'Naypyitaw', 'count_data_value': '328', 'value_ratio': '0.328'}], 'top_5_data_pattern': [{'pattern': 'XXXXXX', 'count_pattern': '340', 'pattern_ratio': '0.34'}, {'pattern': 'XXXXXXXX', 'count_pattern': '332', 'pattern_ratio': '0.332'}, {'pattern': 'XXXXXXXXX', 'count_pattern': '328', 'pattern_ratio': '0.328'}]}, 'Customer_type': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '2', 'ratio_distinct_value': '0.002', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '6', 'data_lenght_max': '6', 'top_5_data_value': [{'data_value': 'Member', 'count_data_value': '501', 'value_ratio': '0.501'}, {'data_value': 'Normal', 'count_data_value': '499', 'value_ratio': '0.499'}], 'top_5_data_pattern': [{'pattern': 'XXXXXX', 'count_pattern': '1000', 'pattern_ratio': '1.0'}]}, 'Gender': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '2', 'ratio_distinct_value': '0.002', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '4', 'data_lenght_max': '6', 'top_5_data_value': [{'data_value': 'Female', 'count_data_value': '501', 'value_ratio': '0.501'}, {'data_value': 'Male', 'count_data_value': '499', 'value_ratio': '0.499'}], 'top_5_data_pattern': [{'pattern': 'XXXXXX', 'count_pattern': '501', 'pattern_ratio': '0.501'}, {'pattern': 'XXXX', 'count_pattern': '499', 'pattern_ratio': '0.499'}]}, 'Product_line': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '6', 'ratio_distinct_value': '0.006', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '17', 'data_lenght_max': '22', 'top_5_data_value': [{'data_value': 'Fashion accessories', 'count_data_value': '178', 'value_ratio': '0.178'}, {'data_value': 'Food and beverages', 'count_data_value': '174', 'value_ratio': '0.174'}, {'data_value': 'Electronic accessories', 'count_data_value': '170', 'value_ratio': '0.17'}, {'data_value': 'Sports and travel', 'count_data_value': '166', 'value_ratio': '0.166'}, {'data_value': 'Home and lifestyle', 'count_data_value': '160', 'value_ratio': '0.16'}], 'top_5_data_pattern': [{'pattern': 'XXXX XXX XXXXXXXXX', 'count_pattern': '334', 'pattern_ratio': '0.334'}, {'pattern': 'XXXXXX XXX XXXXXX', 'count_pattern': '318', 'pattern_ratio': '0.318'}, {'pattern': 'XXXXXXX XXXXXXXXXXX', 'count_pattern': '178', 'pattern_ratio': '0.178'}, {'pattern': 'XXXXXXXXXX XXXXXXXXXXX', 'count_pattern': '170', 'pattern_ratio': '0.17'}]}, 'Unit_price': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '943', 'ratio_distinct_value': '0.943', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '4', 'data_lenght_max': '5', 'min_value': '10.08', 'max_value': '99.96', 'mean': '55.67', 'median': '55', 'mode': '83.77', 'variance': '701.97', 'std': '26.49', 'first_quartile': '33', 'third_quartile': '78', 'iqr': '45', 'minimum': '10.5', 'maximum': '100.5', 'negative_outliner_datapoint': '0', 'positive_outliner_datapoint': '5', 'top_5_data_value': [{'data_value': '83.77', 'count_data_value': '3.0', 'value_ratio': '0.003'}, {'data_value': '99.96', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '24.74', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '45.38', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '45.58', 'count_data_value': '2.0', 'value_ratio': '0.002'}], 'top_5_data_pattern': [{'pattern': 'XX.XX', 'count_pattern': '903', 'pattern_ratio': '0.903'}, {'pattern': 'XX.X', 'count_pattern': '97', 'pattern_ratio': '0.097'}]}, 'Quantity': {'dataType': 'int64', 'is_primary_key': 'False', 'distinct_value': '10', 'ratio_distinct_value': '0.01', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '1', 'data_lenght_max': '2', 'min_value': '1', 'max_value': '10', 'mean': '5.51', 'median': '5', 'mode': '10', 'variance': '8.55', 'std': '2.92', 'first_quartile': '3', 'third_quartile': '8', 'iqr': '5', 'minimum': '0.5', 'maximum': '10.5', 'negative_outliner_datapoint': '0', 'positive_outliner_datapoint': '0', 'top_5_data_value': [{'data_value': '10', 'count_data_value': '119', 'value_ratio': '0.119'}, {'data_value': '1', 'count_data_value': '112', 'value_ratio': '0.112'}, {'data_value': '4', 'count_data_value': '109', 'value_ratio': '0.109'}, {'data_value': '5', 'count_data_value': '102', 'value_ratio': '0.102'}, {'data_value': '7', 'count_data_value': '102', 'value_ratio': '0.102'}], 'top_5_data_pattern': [{'pattern': 'X', 'count_pattern': '881', 'pattern_ratio': '0.881'}, {'pattern': 'XX', 'count_pattern': '119', 'pattern_ratio': '0.119'}]}, 'Tax': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '990', 'ratio_distinct_value': '0.99', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '3', 'data_lenght_max': '18', 'min_value': '0.51', 'max_value': '49.65', 'mean': '15.38', 'median': '12', 'mode': '4.15', 'variance': '137.1', 'std': '11.71', 'first_quartile': '6', 'third_quartile': '22', 'iqr': '16', 'minimum': '-2.0', 'maximum': '30.0', 'negative_outliner_datapoint': '137', 'positive_outliner_datapoint': '0', 'top_5_data_value': [{'data_value': '39.48', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '13.187999999999999', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '22.428', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '4.4639999999999995', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '4.154', 'count_data_value': '2.0', 'value_ratio': '0.002'}], 'top_5_data_pattern': [{'pattern': 'XX.XXX', 'count_pattern': '259', 'pattern_ratio': '0.259'}, {'pattern': 'X.XXX', 'count_pattern': '195', 'pattern_ratio': '0.195'}, {'pattern': 'XX.XXXX', 'count_pattern': '127', 'pattern_ratio': '0.127'}, {'pattern': 'X.XXXX', 'count_pattern': '107', 'pattern_ratio': '0.107'}, {'pattern': 'XX.XX', 'count_pattern': '97', 'pattern_ratio': '0.097'}]}, 'Total': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '990', 'ratio_distinct_value': '0.99', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '4', 'data_lenght_max': '18', 'min_value': '10.68', 'max_value': '1042.65', 'mean': '322.97', 'median': '254', 'mode': '87.23', 'variance': '60459.6', 'std': '245.89', 'first_quartile': '124', 'third_quartile': '471', 'iqr': '347', 'minimum': '-49.5', 'maximum': '644.5', 'negative_outliner_datapoint': '131', 'positive_outliner_datapoint': '0', 'top_5_data_value': [{'data_value': '829.08', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '276.948', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '470.98800000000006', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '93.744', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '87.234', 'count_data_value': '2.0', 'value_ratio': '0.002'}], 'top_5_data_pattern': [{'pattern': 'XXX.XXX', 'count_pattern': '358', 'pattern_ratio': '0.358'}, {'pattern': 'XXX.XXXX', 'count_pattern': '166', 'pattern_ratio': '0.166'}, {'pattern': 'XXX.XX', 'count_pattern': '120', 'pattern_ratio': '0.12'}, {'pattern': 'XXX.XXXXXXXXXXXXXX', 'count_pattern': '106', 'pattern_ratio': '0.106'}, {'pattern': 'XX.XXX', 'count_pattern': '91', 'pattern_ratio': '0.091'}]}, 'Date': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '89', 'ratio_distinct_value': '0.089', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '8', 'data_lenght_max': '9', 'top_5_data_value': [{'data_value': '2/7/2019', 'count_data_value': '20', 'value_ratio': '0.02'}, {'data_value': '2/15/2019', 'count_data_value': '19', 'value_ratio': '0.019'}, {'data_value': '1/8/2019', 'count_data_value': '18', 'value_ratio': '0.018'}, {'data_value': '3/2/2019', 'count_data_value': '18', 'value_ratio': '0.018'}, {'data_value': '3/14/2019', 'count_data_value': '18', 'value_ratio': '0.018'}], 'top_5_data_pattern': [{'pattern': 'X/XX/XXXX', 'count_pattern': '677', 'pattern_ratio': '0.677'}, {'pattern': 'X/X/XXXX', 'count_pattern': '323', 'pattern_ratio': '0.323'}]}, 'Time': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '506', 'ratio_distinct_value': '0.506', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '5', 'data_lenght_max': '5', 'top_5_data_value': [{'data_value': '19:48', 'count_data_value': '7', 'value_ratio': '0.007'}, {'data_value': '14:42', 'count_data_value': '7', 'value_ratio': '0.007'}, {'data_value': '17:38', 'count_data_value': '6', 'value_ratio': '0.006'}, {'data_value': '17:36', 'count_data_value': '5', 'value_ratio': '0.005'}, {'data_value': '19:44', 'count_data_value': '5', 'value_ratio': '0.005'}], 'top_5_data_pattern': [{'pattern': 'XX:XX', 'count_pattern': '1000', 'pattern_ratio': '1.0'}]}, 'Payment': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '3', 'ratio_distinct_value': '0.003', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '4', 'data_lenght_max': '11', 'top_5_data_value': [{'data_value': 'Ewallet', 'count_data_value': '345', 'value_ratio': '0.345'}, {'data_value': 'Cash', 'count_data_value': '344', 'value_ratio': '0.344'}, {'data_value': 'Credit card', 'count_data_value': '311', 'value_ratio': '0.311'}], 'top_5_data_pattern': [{'pattern': 'XXXXXXX', 'count_pattern': '345', 'pattern_ratio': '0.345'}, {'pattern': 'XXXX', 'count_pattern': '344', 'pattern_ratio': '0.344'}, {'pattern': 'XXXXXX XXXX', 'count_pattern': '311', 'pattern_ratio': '0.311'}]}, 'cogs': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '990', 'ratio_distinct_value': '0.99', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '4', 'data_lenght_max': '6', 'min_value': '10.17', 'max_value': '993.0', 'mean': '307.59', 'median': '242', 'mode': '83.08', 'variance': '54838.64', 'std': '234.18', 'first_quartile': '118', 'third_quartile': '449', 'iqr': '331', 'minimum': '-47.5', 'maximum': '614.5', 'negative_outliner_datapoint': '131', 'positive_outliner_datapoint': '0', 'top_5_data_value': [{'data_value': '789.6', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '263.76', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '448.56', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '89.28', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '83.08', 'count_data_value': '2.0', 'value_ratio': '0.002'}], 'top_5_data_pattern': [{'pattern': 'XXX.XX', 'count_pattern': '534', 'pattern_ratio': '0.534'}, {'pattern': 'XXX.X', 'count_pattern': '242', 'pattern_ratio': '0.242'}, {'pattern': 'XX.XX', 'count_pattern': '185', 'pattern_ratio': '0.185'}, {'pattern': 'XX.X', 'count_pattern': '39', 'pattern_ratio': '0.039'}]}, 'gross_margin_percentage': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '1', 'ratio_distinct_value': '0.001', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '18', 'data_lenght_max': '18', 'min_value': '4.76', 'max_value': '4.76', 'mean': '4.76', 'median': '5', 'mode': '4.76', 'variance': '0.0', 'std': '0.0', 'first_quartile': '5', 'third_quartile': '5', 'iqr': '0', 'minimum': '5.0', 'maximum': '5.0', 'negative_outliner_datapoint': '0', 'positive_outliner_datapoint': '1000', 'top_5_data_value': [{'data_value': '4.7619047619999995', 'count_data_value': '1000.0', 'value_ratio': '1.0'}], 'top_5_data_pattern': [{'pattern': 'X.XXXXXXXXXXXXXXXX', 'count_pattern': '1000', 'pattern_ratio': '1.0'}]}, 'gross_income': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '990', 'ratio_distinct_value': '0.99', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '3', 'data_lenght_max': '18', 'min_value': '0.51', 'max_value': '49.65', 'mean': '15.38', 'median': '12', 'mode': '4.15', 'variance': '137.1', 'std': '11.71', 'first_quartile': '6', 'third_quartile': '22', 'iqr': '16', 'minimum': '-2.0', 'maximum': '30.0', 'negative_outliner_datapoint': '137', 'positive_outliner_datapoint': '0', 'top_5_data_value': [{'data_value': '39.48', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '13.187999999999999', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '22.428', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '4.4639999999999995', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '4.154', 'count_data_value': '2.0', 'value_ratio': '0.002'}], 'top_5_data_pattern': [{'pattern': 'XX.XXX', 'count_pattern': '259', 'pattern_ratio': '0.259'}, {'pattern': 'X.XXX', 'count_pattern': '195', 'pattern_ratio': '0.195'}, {'pattern': 'XX.XXXX', 'count_pattern': '127', 'pattern_ratio': '0.127'}, {'pattern': 'X.XXXX', 'count_pattern': '107', 'pattern_ratio': '0.107'}, {'pattern': 'XX.XX', 'count_pattern': '97', 'pattern_ratio': '0.097'}]}, 'Rating': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '61', 'ratio_distinct_value': '0.061', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '3', 'data_lenght_max': '4', 'min_value': '4.0', 'max_value': '10.0', 'mean': '6.97', 'median': '7', 'mode': '6.0', 'variance': '2.95', 'std': '1.72', 'first_quartile': '6', 'third_quartile': '8', 'iqr': '2', 'minimum': '5.0', 'maximum': '9.0', 'negative_outliner_datapoint': '151', 'positive_outliner_datapoint': '153', 'top_5_data_value': [{'data_value': '6.0', 'count_data_value': '26.0', 'value_ratio': '0.026'}, {'data_value': '6.6', 'count_data_value': '24.0', 'value_ratio': '0.024'}, {'data_value': '9.5', 'count_data_value': '22.0', 'value_ratio': '0.022'}, {'data_value': '4.2', 'count_data_value': '22.0', 'value_ratio': '0.022'}, {'data_value': '5.1', 'count_data_value': '21.0', 'value_ratio': '0.021'}], 'top_5_data_pattern': [{'pattern': 'X.X', 'count_pattern': '995', 'pattern_ratio': '0.995'}, {'pattern': 'XX.X', 'count_pattern': '5', 'pattern_ratio': '0.005'}]}}}
```
## Attrubute: sakda.profile_json
#### Return type: string
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>')

print(get_profile.profile_json)
```
#### Output
```
{
    "profile_engine": "sakdas beta version 0.2.15",
    "profile_id": "f904dc2f-e84d-4c83-b97c-8dd8d2054389",
    "file_name": "sample_supermarket_sales",
    "profile_datetime": "23/09/2020 10:54:34",
    "total_record": 1000,
    "total_record_after_deduplication": 1000,
    "duplicated_data": "0",
    "primary_key": "Invoice_ID",
    "total_column": 17,
    "completed_record": "1000",
    "completed_record_ratio": "1.0",
    "blank_column": 0,
    "missing_condition": "null",
    "missing_data": "0",
    "missing_data_ratio": "0.0",
    "schema": "===Schema===\nInvoice_ID: object\nBranch: object\nCity: object\nCustomer_type: object\nGender: object\nProduct_line: object\nUnit_price: float64\nQuantity: int64\nTax: float64\nTotal: float64\nDate: object\nTime: object\nPayment: object\ncogs: float64\ngross_margin_percentage: float64\ngross_income: float64\nRating: float64",
    "column_profile": {
        "Invoice_ID": {
            "dataType": "object",
            "is_primary_key": "True",
            "distinct_value": "1000",
            "ratio_distinct_value": "1.0",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "11",
            "data_lenght_max": "11",
            "top_5_data_value": [
                {
                    "data_value": "101-17-6199",
                    "count_data_value": "1",
                    "value_ratio": "0.001"
                },
                {
                    "data_value": "641-62-7288",
                    "count_data_value": "1",
                    "value_ratio": "0.001"
                },
                {
                    "data_value": "633-91-1052",
                    "count_data_value": "1",
                    "value_ratio": "0.001"
                },
                {
                    "data_value": "634-97-8956",
                    "count_data_value": "1",
                    "value_ratio": "0.001"
                },
                {
                    "data_value": "635-28-5728",
                    "count_data_value": "1",
                    "value_ratio": "0.001"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XXX-XX-XXXX",
                    "count_pattern": "1000",
                    "pattern_ratio": "1.0"
                }
            ]
        },
        "Branch": {
            "dataType": "object",
            "is_primary_key": "False",
            "distinct_value": "3",
            "ratio_distinct_value": "0.003",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "1",
            "data_lenght_max": "1",
            "top_5_data_value": [
                {
                    "data_value": "A",
                    "count_data_value": "340",
                    "value_ratio": "0.34"
                },
                {
                    "data_value": "B",
                    "count_data_value": "332",
                    "value_ratio": "0.332"
                },
                {
                    "data_value": "C",
                    "count_data_value": "328",
                    "value_ratio": "0.328"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "X",
                    "count_pattern": "1000",
                    "pattern_ratio": "1.0"
                }
            ]
        },
        "City": {
            "dataType": "object",
            "is_primary_key": "False",
            "distinct_value": "3",
            "ratio_distinct_value": "0.003",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "6",
            "data_lenght_max": "9",
            "top_5_data_value": [
                {
                    "data_value": "Yangon",
                    "count_data_value": "340",
                    "value_ratio": "0.34"
                },
                {
                    "data_value": "Mandalay",
                    "count_data_value": "332",
                    "value_ratio": "0.332"
                },
                {
                    "data_value": "Naypyitaw",
                    "count_data_value": "328",
                    "value_ratio": "0.328"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XXXXXX",
                    "count_pattern": "340",
                    "pattern_ratio": "0.34"
                },
                {
                    "pattern": "XXXXXXXX",
                    "count_pattern": "332",
                    "pattern_ratio": "0.332"
                },
                {
                    "pattern": "XXXXXXXXX",
                    "count_pattern": "328",
                    "pattern_ratio": "0.328"
                }
            ]
        },
        "Customer_type": {
            "dataType": "object",
            "is_primary_key": "False",
            "distinct_value": "2",
            "ratio_distinct_value": "0.002",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "6",
            "data_lenght_max": "6",
            "top_5_data_value": [
                {
                    "data_value": "Member",
                    "count_data_value": "501",
                    "value_ratio": "0.501"
                },
                {
                    "data_value": "Normal",
                    "count_data_value": "499",
                    "value_ratio": "0.499"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XXXXXX",
                    "count_pattern": "1000",
                    "pattern_ratio": "1.0"
                }
            ]
        },
        "Gender": {
            "dataType": "object",
            "is_primary_key": "False",
            "distinct_value": "2",
            "ratio_distinct_value": "0.002",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "4",
            "data_lenght_max": "6",
            "top_5_data_value": [
                {
                    "data_value": "Female",
                    "count_data_value": "501",
                    "value_ratio": "0.501"
                },
                {
                    "data_value": "Male",
                    "count_data_value": "499",
                    "value_ratio": "0.499"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XXXXXX",
                    "count_pattern": "501",
                    "pattern_ratio": "0.501"
                },
                {
                    "pattern": "XXXX",
                    "count_pattern": "499",
                    "pattern_ratio": "0.499"
                }
            ]
        },
        "Product_line": {
            "dataType": "object",
            "is_primary_key": "False",
            "distinct_value": "6",
            "ratio_distinct_value": "0.006",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "17",
            "data_lenght_max": "22",
            "top_5_data_value": [
                {
                    "data_value": "Fashion accessories",
                    "count_data_value": "178",
                    "value_ratio": "0.178"
                },
                {
                    "data_value": "Food and beverages",
                    "count_data_value": "174",
                    "value_ratio": "0.174"
                },
                {
                    "data_value": "Electronic accessories",
                    "count_data_value": "170",
                    "value_ratio": "0.17"
                },
                {
                    "data_value": "Sports and travel",
                    "count_data_value": "166",
                    "value_ratio": "0.166"
                },
                {
                    "data_value": "Home and lifestyle",
                    "count_data_value": "160",
                    "value_ratio": "0.16"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XXXX XXX XXXXXXXXX",
                    "count_pattern": "334",
                    "pattern_ratio": "0.334"
                },
                {
                    "pattern": "XXXXXX XXX XXXXXX",
                    "count_pattern": "318",
                    "pattern_ratio": "0.318"
                },
                {
                    "pattern": "XXXXXXX XXXXXXXXXXX",
                    "count_pattern": "178",
                    "pattern_ratio": "0.178"
                },
                {
                    "pattern": "XXXXXXXXXX XXXXXXXXXXX",
                    "count_pattern": "170",
                    "pattern_ratio": "0.17"
                }
            ]
        },
        "Unit_price": {
            "dataType": "float64",
            "is_primary_key": "False",
            "distinct_value": "943",
            "ratio_distinct_value": "0.943",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "4",
            "data_lenght_max": "5",
            "min_value": "10.08",
            "max_value": "99.96",
            "mean": "55.67",
            "median": "55",
            "mode": "83.77",
            "variance": "701.97",
            "std": "26.49",
            "first_quartile": "33",
            "third_quartile": "78",
            "iqr": "45",
            "minimum": "10.5",
            "maximum": "100.5",
            "negative_outliner_datapoint": "0",
            "positive_outliner_datapoint": "5",
            "top_5_data_value": [
                {
                    "data_value": "83.77",
                    "count_data_value": "3.0",
                    "value_ratio": "0.003"
                },
                {
                    "data_value": "99.96",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "24.74",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "45.38",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "45.58",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XX.XX",
                    "count_pattern": "903",
                    "pattern_ratio": "0.903"
                },
                {
                    "pattern": "XX.X",
                    "count_pattern": "97",
                    "pattern_ratio": "0.097"
                }
            ]
        },
        "Quantity": {
            "dataType": "int64",
            "is_primary_key": "False",
            "distinct_value": "10",
            "ratio_distinct_value": "0.01",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "1",
            "data_lenght_max": "2",
            "min_value": "1",
            "max_value": "10",
            "mean": "5.51",
            "median": "5",
            "mode": "10",
            "variance": "8.55",
            "std": "2.92",
            "first_quartile": "3",
            "third_quartile": "8",
            "iqr": "5",
            "minimum": "0.5",
            "maximum": "10.5",
            "negative_outliner_datapoint": "0",
            "positive_outliner_datapoint": "0",
            "top_5_data_value": [
                {
                    "data_value": "10",
                    "count_data_value": "119",
                    "value_ratio": "0.119"
                },
                {
                    "data_value": "1",
                    "count_data_value": "112",
                    "value_ratio": "0.112"
                },
                {
                    "data_value": "4",
                    "count_data_value": "109",
                    "value_ratio": "0.109"
                },
                {
                    "data_value": "5",
                    "count_data_value": "102",
                    "value_ratio": "0.102"
                },
                {
                    "data_value": "7",
                    "count_data_value": "102",
                    "value_ratio": "0.102"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "X",
                    "count_pattern": "881",
                    "pattern_ratio": "0.881"
                },
                {
                    "pattern": "XX",
                    "count_pattern": "119",
                    "pattern_ratio": "0.119"
                }
            ]
        },
        "Tax": {
            "dataType": "float64",
            "is_primary_key": "False",
            "distinct_value": "990",
            "ratio_distinct_value": "0.99",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "3",
            "data_lenght_max": "18",
            "min_value": "0.51",
            "max_value": "49.65",
            "mean": "15.38",
            "median": "12",
            "mode": "4.15",
            "variance": "137.1",
            "std": "11.71",
            "first_quartile": "6",
            "third_quartile": "22",
            "iqr": "16",
            "minimum": "-2.0",
            "maximum": "30.0",
            "negative_outliner_datapoint": "137",
            "positive_outliner_datapoint": "0",
            "top_5_data_value": [
                {
                    "data_value": "39.48",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "13.187999999999999",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "22.428",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "4.4639999999999995",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "4.154",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XX.XXX",
                    "count_pattern": "259",
                    "pattern_ratio": "0.259"
                },
                {
                    "pattern": "X.XXX",
                    "count_pattern": "195",
                    "pattern_ratio": "0.195"
                },
                {
                    "pattern": "XX.XXXX",
                    "count_pattern": "127",
                    "pattern_ratio": "0.127"
                },
                {
                    "pattern": "X.XXXX",
                    "count_pattern": "107",
                    "pattern_ratio": "0.107"
                },
                {
                    "pattern": "XX.XX",
                    "count_pattern": "97",
                    "pattern_ratio": "0.097"
                }
            ]
        },
        "Total": {
            "dataType": "float64",
            "is_primary_key": "False",
            "distinct_value": "990",
            "ratio_distinct_value": "0.99",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "4",
            "data_lenght_max": "18",
            "min_value": "10.68",
            "max_value": "1042.65",
            "mean": "322.97",
            "median": "254",
            "mode": "87.23",
            "variance": "60459.6",
            "std": "245.89",
            "first_quartile": "124",
            "third_quartile": "471",
            "iqr": "347",
            "minimum": "-49.5",
            "maximum": "644.5",
            "negative_outliner_datapoint": "131",
            "positive_outliner_datapoint": "0",
            "top_5_data_value": [
                {
                    "data_value": "829.08",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "276.948",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "470.98800000000006",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "93.744",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "87.234",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XXX.XXX",
                    "count_pattern": "358",
                    "pattern_ratio": "0.358"
                },
                {
                    "pattern": "XXX.XXXX",
                    "count_pattern": "166",
                    "pattern_ratio": "0.166"
                },
                {
                    "pattern": "XXX.XX",
                    "count_pattern": "120",
                    "pattern_ratio": "0.12"
                },
                {
                    "pattern": "XXX.XXXXXXXXXXXXXX",
                    "count_pattern": "106",
                    "pattern_ratio": "0.106"
                },
                {
                    "pattern": "XX.XXX",
                    "count_pattern": "91",
                    "pattern_ratio": "0.091"
                }
            ]
        },
        "Date": {
            "dataType": "object",
            "is_primary_key": "False",
            "distinct_value": "89",
            "ratio_distinct_value": "0.089",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "8",
            "data_lenght_max": "9",
            "top_5_data_value": [
                {
                    "data_value": "2/7/2019",
                    "count_data_value": "20",
                    "value_ratio": "0.02"
                },
                {
                    "data_value": "2/15/2019",
                    "count_data_value": "19",
                    "value_ratio": "0.019"
                },
                {
                    "data_value": "1/8/2019",
                    "count_data_value": "18",
                    "value_ratio": "0.018"
                },
                {
                    "data_value": "3/2/2019",
                    "count_data_value": "18",
                    "value_ratio": "0.018"
                },
                {
                    "data_value": "3/14/2019",
                    "count_data_value": "18",
                    "value_ratio": "0.018"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "X/XX/XXXX",
                    "count_pattern": "677",
                    "pattern_ratio": "0.677"
                },
                {
                    "pattern": "X/X/XXXX",
                    "count_pattern": "323",
                    "pattern_ratio": "0.323"
                }
            ]
        },
        "Time": {
            "dataType": "object",
            "is_primary_key": "False",
            "distinct_value": "506",
            "ratio_distinct_value": "0.506",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "5",
            "data_lenght_max": "5",
            "top_5_data_value": [
                {
                    "data_value": "19:48",
                    "count_data_value": "7",
                    "value_ratio": "0.007"
                },
                {
                    "data_value": "14:42",
                    "count_data_value": "7",
                    "value_ratio": "0.007"
                },
                {
                    "data_value": "17:38",
                    "count_data_value": "6",
                    "value_ratio": "0.006"
                },
                {
                    "data_value": "17:36",
                    "count_data_value": "5",
                    "value_ratio": "0.005"
                },
                {
                    "data_value": "19:44",
                    "count_data_value": "5",
                    "value_ratio": "0.005"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XX:XX",
                    "count_pattern": "1000",
                    "pattern_ratio": "1.0"
                }
            ]
        },
        "Payment": {
            "dataType": "object",
            "is_primary_key": "False",
            "distinct_value": "3",
            "ratio_distinct_value": "0.003",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "4",
            "data_lenght_max": "11",
            "top_5_data_value": [
                {
                    "data_value": "Ewallet",
                    "count_data_value": "345",
                    "value_ratio": "0.345"
                },
                {
                    "data_value": "Cash",
                    "count_data_value": "344",
                    "value_ratio": "0.344"
                },
                {
                    "data_value": "Credit card",
                    "count_data_value": "311",
                    "value_ratio": "0.311"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XXXXXXX",
                    "count_pattern": "345",
                    "pattern_ratio": "0.345"
                },
                {
                    "pattern": "XXXX",
                    "count_pattern": "344",
                    "pattern_ratio": "0.344"
                },
                {
                    "pattern": "XXXXXX XXXX",
                    "count_pattern": "311",
                    "pattern_ratio": "0.311"
                }
            ]
        },
        "cogs": {
            "dataType": "float64",
            "is_primary_key": "False",
            "distinct_value": "990",
            "ratio_distinct_value": "0.99",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "4",
            "data_lenght_max": "6",
            "min_value": "10.17",
            "max_value": "993.0",
            "mean": "307.59",
            "median": "242",
            "mode": "83.08",
            "variance": "54838.64",
            "std": "234.18",
            "first_quartile": "118",
            "third_quartile": "449",
            "iqr": "331",
            "minimum": "-47.5",
            "maximum": "614.5",
            "negative_outliner_datapoint": "131",
            "positive_outliner_datapoint": "0",
            "top_5_data_value": [
                {
                    "data_value": "789.6",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "263.76",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "448.56",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "89.28",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "83.08",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XXX.XX",
                    "count_pattern": "534",
                    "pattern_ratio": "0.534"
                },
                {
                    "pattern": "XXX.X",
                    "count_pattern": "242",
                    "pattern_ratio": "0.242"
                },
                {
                    "pattern": "XX.XX",
                    "count_pattern": "185",
                    "pattern_ratio": "0.185"
                },
                {
                    "pattern": "XX.X",
                    "count_pattern": "39",
                    "pattern_ratio": "0.039"
                }
            ]
        },
        "gross_margin_percentage": {
            "dataType": "float64",
            "is_primary_key": "False",
            "distinct_value": "1",
            "ratio_distinct_value": "0.001",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "18",
            "data_lenght_max": "18",
            "min_value": "4.76",
            "max_value": "4.76",
            "mean": "4.76",
            "median": "5",
            "mode": "4.76",
            "variance": "0.0",
            "std": "0.0",
            "first_quartile": "5",
            "third_quartile": "5",
            "iqr": "0",
            "minimum": "5.0",
            "maximum": "5.0",
            "negative_outliner_datapoint": "0",
            "positive_outliner_datapoint": "1000",
            "top_5_data_value": [
                {
                    "data_value": "4.7619047619999995",
                    "count_data_value": "1000.0",
                    "value_ratio": "1.0"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "X.XXXXXXXXXXXXXXXX",
                    "count_pattern": "1000",
                    "pattern_ratio": "1.0"
                }
            ]
        },
        "gross_income": {
            "dataType": "float64",
            "is_primary_key": "False",
            "distinct_value": "990",
            "ratio_distinct_value": "0.99",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "3",
            "data_lenght_max": "18",
            "min_value": "0.51",
            "max_value": "49.65",
            "mean": "15.38",
            "median": "12",
            "mode": "4.15",
            "variance": "137.1",
            "std": "11.71",
            "first_quartile": "6",
            "third_quartile": "22",
            "iqr": "16",
            "minimum": "-2.0",
            "maximum": "30.0",
            "negative_outliner_datapoint": "137",
            "positive_outliner_datapoint": "0",
            "top_5_data_value": [
                {
                    "data_value": "39.48",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "13.187999999999999",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "22.428",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "4.4639999999999995",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                },
                {
                    "data_value": "4.154",
                    "count_data_value": "2.0",
                    "value_ratio": "0.002"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "XX.XXX",
                    "count_pattern": "259",
                    "pattern_ratio": "0.259"
                },
                {
                    "pattern": "X.XXX",
                    "count_pattern": "195",
                    "pattern_ratio": "0.195"
                },
                {
                    "pattern": "XX.XXXX",
                    "count_pattern": "127",
                    "pattern_ratio": "0.127"
                },
                {
                    "pattern": "X.XXXX",
                    "count_pattern": "107",
                    "pattern_ratio": "0.107"
                },
                {
                    "pattern": "XX.XX",
                    "count_pattern": "97",
                    "pattern_ratio": "0.097"
                }
            ]
        },
        "Rating": {
            "dataType": "float64",
            "is_primary_key": "False",
            "distinct_value": "61",
            "ratio_distinct_value": "0.061",
            "missing_value": "0",
            "ratio_missing_value": "0.0",
            "data_lenght_min": "3",
            "data_lenght_max": "4",
            "min_value": "4.0",
            "max_value": "10.0",
            "mean": "6.97",
            "median": "7",
            "mode": "6.0",
            "variance": "2.95",
            "std": "1.72",
            "first_quartile": "6",
            "third_quartile": "8",
            "iqr": "2",
            "minimum": "5.0",
            "maximum": "9.0",
            "negative_outliner_datapoint": "151",
            "positive_outliner_datapoint": "153",
            "top_5_data_value": [
                {
                    "data_value": "6.0",
                    "count_data_value": "26.0",
                    "value_ratio": "0.026"
                },
                {
                    "data_value": "6.6",
                    "count_data_value": "24.0",
                    "value_ratio": "0.024"
                },
                {
                    "data_value": "9.5",
                    "count_data_value": "22.0",
                    "value_ratio": "0.022"
                },
                {
                    "data_value": "4.2",
                    "count_data_value": "22.0",
                    "value_ratio": "0.022"
                },
                {
                    "data_value": "5.1",
                    "count_data_value": "21.0",
                    "value_ratio": "0.021"
                }
            ],
            "top_5_data_pattern": [
                {
                    "pattern": "X.X",
                    "count_pattern": "995",
                    "pattern_ratio": "0.995"
                },
                {
                    "pattern": "XX.X",
                    "count_pattern": "5",
                    "pattern_ratio": "0.005"
                }
            ]
        }
    }
}
```

## Attrubute: sakda.column_profile
#### Return type: dict
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>')

print(get_profile.column_profile)
```
#### Output
```
{'Invoice_ID': {'dataType': 'object', 'is_primary_key': 'True', 'distinct_value': '1000', 'ratio_distinct_value': '1.0', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '11', 'data_lenght_max': '11', 'top_5_data_value': [{'data_value': '101-17-6199', 'count_data_value': '1', 'value_ratio': '0.001'}, {'data_value': '641-62-7288', 'count_data_value': '1', 'value_ratio': '0.001'}, {'data_value': '633-91-1052', 'count_data_value': '1', 'value_ratio': '0.001'}, {'data_value': '634-97-8956', 'count_data_value': '1', 'value_ratio': '0.001'}, {'data_value': '635-28-5728', 'count_data_value': '1', 'value_ratio': '0.001'}], 'top_5_data_pattern': [{'pattern': 'XXX-XX-XXXX', 'count_pattern': '1000', 'pattern_ratio': '1.0'}]}, 'Branch': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '3', 'ratio_distinct_value': '0.003', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '1', 'data_lenght_max': '1', 'top_5_data_value': [{'data_value': 'A', 'count_data_value': '340', 'value_ratio': '0.34'}, {'data_value': 'B', 'count_data_value': '332', 'value_ratio': '0.332'}, {'data_value': 'C', 'count_data_value': '328', 'value_ratio': '0.328'}], 'top_5_data_pattern': [{'pattern': 'X', 'count_pattern': '1000', 'pattern_ratio': '1.0'}]}, 'City': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '3', 'ratio_distinct_value': '0.003', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '6', 'data_lenght_max': '9', 'top_5_data_value': [{'data_value': 'Yangon', 'count_data_value': '340', 'value_ratio': '0.34'}, {'data_value': 'Mandalay', 'count_data_value': '332', 'value_ratio': '0.332'}, {'data_value': 'Naypyitaw', 'count_data_value': '328', 'value_ratio': '0.328'}], 'top_5_data_pattern': [{'pattern': 'XXXXXX', 'count_pattern': '340', 'pattern_ratio': '0.34'}, {'pattern': 'XXXXXXXX', 'count_pattern': '332', 'pattern_ratio': '0.332'}, {'pattern': 'XXXXXXXXX', 'count_pattern': '328', 'pattern_ratio': '0.328'}]}, 'Customer_type': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '2', 'ratio_distinct_value': '0.002', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '6', 'data_lenght_max': '6', 'top_5_data_value': [{'data_value': 'Member', 'count_data_value': '501', 'value_ratio': '0.501'}, {'data_value': 'Normal', 'count_data_value': '499', 'value_ratio': '0.499'}], 'top_5_data_pattern': [{'pattern': 'XXXXXX', 'count_pattern': '1000', 'pattern_ratio': '1.0'}]}, 'Gender': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '2', 'ratio_distinct_value': '0.002', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '4', 'data_lenght_max': '6', 'top_5_data_value': [{'data_value': 'Female', 'count_data_value': '501', 'value_ratio': '0.501'}, {'data_value': 'Male', 'count_data_value': '499', 'value_ratio': '0.499'}], 'top_5_data_pattern': [{'pattern': 'XXXXXX', 'count_pattern': '501', 'pattern_ratio': '0.501'}, {'pattern': 'XXXX', 'count_pattern': '499', 'pattern_ratio': '0.499'}]}, 'Product_line': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '6', 'ratio_distinct_value': '0.006', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '17', 'data_lenght_max': '22', 'top_5_data_value': [{'data_value': 'Fashion accessories', 'count_data_value': '178', 'value_ratio': '0.178'}, {'data_value': 'Food and beverages', 'count_data_value': '174', 'value_ratio': '0.174'}, {'data_value': 'Electronic accessories', 'count_data_value': '170', 'value_ratio': '0.17'}, {'data_value': 'Sports and travel', 'count_data_value': '166', 'value_ratio': '0.166'}, {'data_value': 'Home and lifestyle', 'count_data_value': '160', 'value_ratio': '0.16'}], 'top_5_data_pattern': [{'pattern': 'XXXX XXX XXXXXXXXX', 'count_pattern': '334', 'pattern_ratio': '0.334'}, {'pattern': 'XXXXXX XXX XXXXXX', 'count_pattern': '318', 'pattern_ratio': '0.318'}, {'pattern': 'XXXXXXX XXXXXXXXXXX', 'count_pattern': '178', 'pattern_ratio': '0.178'}, {'pattern': 'XXXXXXXXXX XXXXXXXXXXX', 'count_pattern': '170', 'pattern_ratio': '0.17'}]}, 'Unit_price': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '943', 'ratio_distinct_value': '0.943', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '4', 'data_lenght_max': '5', 'min_value': '10.08', 'max_value': '99.96', 'mean': '55.67', 'median': '55', 'mode': '83.77', 'variance': '701.97', 'std': '26.49', 'first_quartile': '33', 'third_quartile': '78', 'iqr': '45', 'minimum': '10.5', 'maximum': '100.5', 'negative_outliner_datapoint': '0', 'positive_outliner_datapoint': '5', 'top_5_data_value': [{'data_value': '83.77', 'count_data_value': '3.0', 'value_ratio': '0.003'}, {'data_value': '99.96', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '24.74', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '45.38', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '45.58', 'count_data_value': '2.0', 'value_ratio': '0.002'}], 'top_5_data_pattern': [{'pattern': 'XX.XX', 'count_pattern': '903', 'pattern_ratio': '0.903'}, {'pattern': 'XX.X', 'count_pattern': '97', 'pattern_ratio': '0.097'}]}, 'Quantity': {'dataType': 'int64', 'is_primary_key': 'False', 'distinct_value': '10', 'ratio_distinct_value': '0.01', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '1', 'data_lenght_max': '2', 'min_value': '1', 'max_value': '10', 'mean': '5.51', 'median': '5', 'mode': '10', 'variance': '8.55', 'std': '2.92', 'first_quartile': '3', 'third_quartile': '8', 'iqr': '5', 'minimum': '0.5', 'maximum': '10.5', 'negative_outliner_datapoint': '0', 'positive_outliner_datapoint': '0', 'top_5_data_value': [{'data_value': '10', 'count_data_value': '119', 'value_ratio': '0.119'}, {'data_value': '1', 'count_data_value': '112', 'value_ratio': '0.112'}, {'data_value': '4', 'count_data_value': '109', 'value_ratio': '0.109'}, {'data_value': '5', 'count_data_value': '102', 'value_ratio': '0.102'}, {'data_value': '7', 'count_data_value': '102', 'value_ratio': '0.102'}], 'top_5_data_pattern': [{'pattern': 'X', 'count_pattern': '881', 'pattern_ratio': '0.881'}, {'pattern': 'XX', 'count_pattern': '119', 'pattern_ratio': '0.119'}]}, 'Tax': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '990', 'ratio_distinct_value': '0.99', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '3', 'data_lenght_max': '18', 'min_value': '0.51', 'max_value': '49.65', 'mean': '15.38', 'median': '12', 'mode': '4.15', 'variance': '137.1', 'std': '11.71', 'first_quartile': '6', 'third_quartile': '22', 'iqr': '16', 'minimum': '-2.0', 'maximum': '30.0', 'negative_outliner_datapoint': '137', 'positive_outliner_datapoint': '0', 'top_5_data_value': [{'data_value': '39.48', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '13.187999999999999', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '22.428', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '4.4639999999999995', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '4.154', 'count_data_value': '2.0', 'value_ratio': '0.002'}], 'top_5_data_pattern': [{'pattern': 'XX.XXX', 'count_pattern': '259', 'pattern_ratio': '0.259'}, {'pattern': 'X.XXX', 'count_pattern': '195', 'pattern_ratio': '0.195'}, {'pattern': 'XX.XXXX', 'count_pattern': '127', 'pattern_ratio': '0.127'}, {'pattern': 'X.XXXX', 'count_pattern': '107', 'pattern_ratio': '0.107'}, {'pattern': 'XX.XX', 'count_pattern': '97', 'pattern_ratio': '0.097'}]}, 'Total': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '990', 'ratio_distinct_value': '0.99', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '4', 'data_lenght_max': '18', 'min_value': '10.68', 'max_value': '1042.65', 'mean': '322.97', 'median': '254', 'mode': '87.23', 'variance': '60459.6', 'std': '245.89', 'first_quartile': '124', 'third_quartile': '471', 'iqr': '347', 'minimum': '-49.5', 'maximum': '644.5', 'negative_outliner_datapoint': '131', 'positive_outliner_datapoint': '0', 'top_5_data_value': [{'data_value': '829.08', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '276.948', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '470.98800000000006', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '93.744', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '87.234', 'count_data_value': '2.0', 'value_ratio': '0.002'}], 'top_5_data_pattern': [{'pattern': 'XXX.XXX', 'count_pattern': '358', 'pattern_ratio': '0.358'}, {'pattern': 'XXX.XXXX', 'count_pattern': '166', 'pattern_ratio': '0.166'}, {'pattern': 'XXX.XX', 'count_pattern': '120', 'pattern_ratio': '0.12'}, {'pattern': 'XXX.XXXXXXXXXXXXXX', 'count_pattern': '106', 'pattern_ratio': '0.106'}, {'pattern': 'XX.XXX', 'count_pattern': '91', 'pattern_ratio': '0.091'}]}, 'Date': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '89', 'ratio_distinct_value': '0.089', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '8', 'data_lenght_max': '9', 'top_5_data_value': [{'data_value': '2/7/2019', 'count_data_value': '20', 'value_ratio': '0.02'}, {'data_value': '2/15/2019', 'count_data_value': '19', 'value_ratio': '0.019'}, {'data_value': '1/8/2019', 'count_data_value': '18', 'value_ratio': '0.018'}, {'data_value': '3/2/2019', 'count_data_value': '18', 'value_ratio': '0.018'}, {'data_value': '3/14/2019', 'count_data_value': '18', 'value_ratio': '0.018'}], 'top_5_data_pattern': [{'pattern': 'X/XX/XXXX', 'count_pattern': '677', 'pattern_ratio': '0.677'}, {'pattern': 'X/X/XXXX', 'count_pattern': '323', 'pattern_ratio': '0.323'}]}, 'Time': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '506', 'ratio_distinct_value': '0.506', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '5', 'data_lenght_max': '5', 'top_5_data_value': [{'data_value': '19:48', 'count_data_value': '7', 'value_ratio': '0.007'}, {'data_value': '14:42', 'count_data_value': '7', 'value_ratio': '0.007'}, {'data_value': '17:38', 'count_data_value': '6', 'value_ratio': '0.006'}, {'data_value': '17:36', 'count_data_value': '5', 'value_ratio': '0.005'}, {'data_value': '19:44', 'count_data_value': '5', 'value_ratio': '0.005'}], 'top_5_data_pattern': [{'pattern': 'XX:XX', 'count_pattern': '1000', 'pattern_ratio': '1.0'}]}, 'Payment': {'dataType': 'object', 'is_primary_key': 'False', 'distinct_value': '3', 'ratio_distinct_value': '0.003', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '4', 'data_lenght_max': '11', 'top_5_data_value': [{'data_value': 'Ewallet', 'count_data_value': '345', 'value_ratio': '0.345'}, {'data_value': 'Cash', 'count_data_value': '344', 'value_ratio': '0.344'}, {'data_value': 'Credit card', 'count_data_value': '311', 'value_ratio': '0.311'}], 'top_5_data_pattern': [{'pattern': 'XXXXXXX', 'count_pattern': '345', 'pattern_ratio': '0.345'}, {'pattern': 'XXXX', 'count_pattern': '344', 'pattern_ratio': '0.344'}, {'pattern': 'XXXXXX XXXX', 'count_pattern': '311', 'pattern_ratio': '0.311'}]}, 'cogs': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '990', 'ratio_distinct_value': '0.99', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '4', 'data_lenght_max': '6', 'min_value': '10.17', 'max_value': '993.0', 'mean': '307.59', 'median': '242', 'mode': '83.08', 'variance': '54838.64', 'std': '234.18', 'first_quartile': '118', 'third_quartile': '449', 'iqr': '331', 'minimum': '-47.5', 'maximum': '614.5', 'negative_outliner_datapoint': '131', 'positive_outliner_datapoint': '0', 'top_5_data_value': [{'data_value': '789.6', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '263.76', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '448.56', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '89.28', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '83.08', 'count_data_value': '2.0', 'value_ratio': '0.002'}], 'top_5_data_pattern': [{'pattern': 'XXX.XX', 'count_pattern': '534', 'pattern_ratio': '0.534'}, {'pattern': 'XXX.X', 'count_pattern': '242', 'pattern_ratio': '0.242'}, {'pattern': 'XX.XX', 'count_pattern': '185', 'pattern_ratio': '0.185'}, {'pattern': 'XX.X', 'count_pattern': '39', 'pattern_ratio': '0.039'}]}, 'gross_margin_percentage': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '1', 'ratio_distinct_value': '0.001', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '18', 'data_lenght_max': '18', 'min_value': '4.76', 'max_value': '4.76', 'mean': '4.76', 'median': '5', 'mode': '4.76', 'variance': '0.0', 'std': '0.0', 'first_quartile': '5', 'third_quartile': '5', 'iqr': '0', 'minimum': '5.0', 'maximum': '5.0', 'negative_outliner_datapoint': '0', 'positive_outliner_datapoint': '1000', 'top_5_data_value': [{'data_value': '4.7619047619999995', 'count_data_value': '1000.0', 'value_ratio': '1.0'}], 'top_5_data_pattern': [{'pattern': 'X.XXXXXXXXXXXXXXXX', 'count_pattern': '1000', 'pattern_ratio': '1.0'}]}, 'gross_income': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '990', 'ratio_distinct_value': '0.99', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '3', 'data_lenght_max': '18', 'min_value': '0.51', 'max_value': '49.65', 'mean': '15.38', 'median': '12', 'mode': '4.15', 'variance': '137.1', 'std': '11.71', 'first_quartile': '6', 'third_quartile': '22', 'iqr': '16', 'minimum': '-2.0', 'maximum': '30.0', 'negative_outliner_datapoint': '137', 'positive_outliner_datapoint': '0', 'top_5_data_value': [{'data_value': '39.48', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '13.187999999999999', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '22.428', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '4.4639999999999995', 'count_data_value': '2.0', 'value_ratio': '0.002'}, {'data_value': '4.154', 'count_data_value': '2.0', 'value_ratio': '0.002'}], 'top_5_data_pattern': [{'pattern': 'XX.XXX', 'count_pattern': '259', 'pattern_ratio': '0.259'}, {'pattern': 'X.XXX', 'count_pattern': '195', 'pattern_ratio': '0.195'}, {'pattern': 'XX.XXXX', 'count_pattern': '127', 'pattern_ratio': '0.127'}, {'pattern': 'X.XXXX', 'count_pattern': '107', 'pattern_ratio': '0.107'}, {'pattern': 'XX.XX', 'count_pattern': '97', 'pattern_ratio': '0.097'}]}, 'Rating': {'dataType': 'float64', 'is_primary_key': 'False', 'distinct_value': '61', 'ratio_distinct_value': '0.061', 'missing_value': '0', 'ratio_missing_value': '0.0', 'data_lenght_min': '3', 'data_lenght_max': '4', 'min_value': '4.0', 'max_value': '10.0', 'mean': '6.97', 'median': '7', 'mode': '6.0', 'variance': '2.95', 'std': '1.72', 'first_quartile': '6', 'third_quartile': '8', 'iqr': '2', 'minimum': '5.0', 'maximum': '9.0', 'negative_outliner_datapoint': '151', 'positive_outliner_datapoint': '153', 'top_5_data_value': [{'data_value': '6.0', 'count_data_value': '26.0', 'value_ratio': '0.026'}, {'data_value': '6.6', 'count_data_value': '24.0', 'value_ratio': '0.024'}, {'data_value': '9.5', 'count_data_value': '22.0', 'value_ratio': '0.022'}, {'data_value': '4.2', 'count_data_value': '22.0', 'value_ratio': '0.022'}, {'data_value': '5.1', 'count_data_value': '21.0', 'value_ratio': '0.021'}], 'top_5_data_pattern': [{'pattern': 'X.X', 'count_pattern': '995', 'pattern_ratio': '0.995'}, {'pattern': 'XX.X', 'count_pattern': '5', 'pattern_ratio': '0.005'}]}}
```

## Attrubute: dataset.column_profile_json
#### Return type: string
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>')

print(get_profile.column_profile_json)
```
#### Output
```
{
    "Invoice_ID": {
        "dataType": "object",
        "is_primary_key": "True",
        "distinct_value": "1000",
        "ratio_distinct_value": "1.0",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "11",
        "data_lenght_max": "11",
        "top_5_data_value": [
            {
                "data_value": "101-17-6199",
                "count_data_value": "1",
                "value_ratio": "0.001"
            },
            {
                "data_value": "641-62-7288",
                "count_data_value": "1",
                "value_ratio": "0.001"
            },
            {
                "data_value": "633-91-1052",
                "count_data_value": "1",
                "value_ratio": "0.001"
            },
            {
                "data_value": "634-97-8956",
                "count_data_value": "1",
                "value_ratio": "0.001"
            },
            {
                "data_value": "635-28-5728",
                "count_data_value": "1",
                "value_ratio": "0.001"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XXX-XX-XXXX",
                "count_pattern": "1000",
                "pattern_ratio": "1.0"
            }
        ]
    },
    "Branch": {
        "dataType": "object",
        "is_primary_key": "False",
        "distinct_value": "3",
        "ratio_distinct_value": "0.003",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "1",
        "data_lenght_max": "1",
        "top_5_data_value": [
            {
                "data_value": "A",
                "count_data_value": "340",
                "value_ratio": "0.34"
            },
            {
                "data_value": "B",
                "count_data_value": "332",
                "value_ratio": "0.332"
            },
            {
                "data_value": "C",
                "count_data_value": "328",
                "value_ratio": "0.328"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "X",
                "count_pattern": "1000",
                "pattern_ratio": "1.0"
            }
        ]
    },
    "City": {
        "dataType": "object",
        "is_primary_key": "False",
        "distinct_value": "3",
        "ratio_distinct_value": "0.003",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "6",
        "data_lenght_max": "9",
        "top_5_data_value": [
            {
                "data_value": "Yangon",
                "count_data_value": "340",
                "value_ratio": "0.34"
            },
            {
                "data_value": "Mandalay",
                "count_data_value": "332",
                "value_ratio": "0.332"
            },
            {
                "data_value": "Naypyitaw",
                "count_data_value": "328",
                "value_ratio": "0.328"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XXXXXX",
                "count_pattern": "340",
                "pattern_ratio": "0.34"
            },
            {
                "pattern": "XXXXXXXX",
                "count_pattern": "332",
                "pattern_ratio": "0.332"
            },
            {
                "pattern": "XXXXXXXXX",
                "count_pattern": "328",
                "pattern_ratio": "0.328"
            }
        ]
    },
    "Customer_type": {
        "dataType": "object",
        "is_primary_key": "False",
        "distinct_value": "2",
        "ratio_distinct_value": "0.002",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "6",
        "data_lenght_max": "6",
        "top_5_data_value": [
            {
                "data_value": "Member",
                "count_data_value": "501",
                "value_ratio": "0.501"
            },
            {
                "data_value": "Normal",
                "count_data_value": "499",
                "value_ratio": "0.499"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XXXXXX",
                "count_pattern": "1000",
                "pattern_ratio": "1.0"
            }
        ]
    },
    "Gender": {
        "dataType": "object",
        "is_primary_key": "False",
        "distinct_value": "2",
        "ratio_distinct_value": "0.002",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "4",
        "data_lenght_max": "6",
        "top_5_data_value": [
            {
                "data_value": "Female",
                "count_data_value": "501",
                "value_ratio": "0.501"
            },
            {
                "data_value": "Male",
                "count_data_value": "499",
                "value_ratio": "0.499"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XXXXXX",
                "count_pattern": "501",
                "pattern_ratio": "0.501"
            },
            {
                "pattern": "XXXX",
                "count_pattern": "499",
                "pattern_ratio": "0.499"
            }
        ]
    },
    "Product_line": {
        "dataType": "object",
        "is_primary_key": "False",
        "distinct_value": "6",
        "ratio_distinct_value": "0.006",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "17",
        "data_lenght_max": "22",
        "top_5_data_value": [
            {
                "data_value": "Fashion accessories",
                "count_data_value": "178",
                "value_ratio": "0.178"
            },
            {
                "data_value": "Food and beverages",
                "count_data_value": "174",
                "value_ratio": "0.174"
            },
            {
                "data_value": "Electronic accessories",
                "count_data_value": "170",
                "value_ratio": "0.17"
            },
            {
                "data_value": "Sports and travel",
                "count_data_value": "166",
                "value_ratio": "0.166"
            },
            {
                "data_value": "Home and lifestyle",
                "count_data_value": "160",
                "value_ratio": "0.16"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XXXX XXX XXXXXXXXX",
                "count_pattern": "334",
                "pattern_ratio": "0.334"
            },
            {
                "pattern": "XXXXXX XXX XXXXXX",
                "count_pattern": "318",
                "pattern_ratio": "0.318"
            },
            {
                "pattern": "XXXXXXX XXXXXXXXXXX",
                "count_pattern": "178",
                "pattern_ratio": "0.178"
            },
            {
                "pattern": "XXXXXXXXXX XXXXXXXXXXX",
                "count_pattern": "170",
                "pattern_ratio": "0.17"
            }
        ]
    },
    "Unit_price": {
        "dataType": "float64",
        "is_primary_key": "False",
        "distinct_value": "943",
        "ratio_distinct_value": "0.943",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "4",
        "data_lenght_max": "5",
        "min_value": "10.08",
        "max_value": "99.96",
        "mean": "55.67",
        "median": "55",
        "mode": "83.77",
        "variance": "701.97",
        "std": "26.49",
        "first_quartile": "33",
        "third_quartile": "78",
        "iqr": "45",
        "minimum": "10.5",
        "maximum": "100.5",
        "negative_outliner_datapoint": "0",
        "positive_outliner_datapoint": "5",
        "top_5_data_value": [
            {
                "data_value": "83.77",
                "count_data_value": "3.0",
                "value_ratio": "0.003"
            },
            {
                "data_value": "99.96",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "24.74",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "45.38",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "45.58",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XX.XX",
                "count_pattern": "903",
                "pattern_ratio": "0.903"
            },
            {
                "pattern": "XX.X",
                "count_pattern": "97",
                "pattern_ratio": "0.097"
            }
        ]
    },
    "Quantity": {
        "dataType": "int64",
        "is_primary_key": "False",
        "distinct_value": "10",
        "ratio_distinct_value": "0.01",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "1",
        "data_lenght_max": "2",
        "min_value": "1",
        "max_value": "10",
        "mean": "5.51",
        "median": "5",
        "mode": "10",
        "variance": "8.55",
        "std": "2.92",
        "first_quartile": "3",
        "third_quartile": "8",
        "iqr": "5",
        "minimum": "0.5",
        "maximum": "10.5",
        "negative_outliner_datapoint": "0",
        "positive_outliner_datapoint": "0",
        "top_5_data_value": [
            {
                "data_value": "10",
                "count_data_value": "119",
                "value_ratio": "0.119"
            },
            {
                "data_value": "1",
                "count_data_value": "112",
                "value_ratio": "0.112"
            },
            {
                "data_value": "4",
                "count_data_value": "109",
                "value_ratio": "0.109"
            },
            {
                "data_value": "5",
                "count_data_value": "102",
                "value_ratio": "0.102"
            },
            {
                "data_value": "7",
                "count_data_value": "102",
                "value_ratio": "0.102"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "X",
                "count_pattern": "881",
                "pattern_ratio": "0.881"
            },
            {
                "pattern": "XX",
                "count_pattern": "119",
                "pattern_ratio": "0.119"
            }
        ]
    },
    "Tax": {
        "dataType": "float64",
        "is_primary_key": "False",
        "distinct_value": "990",
        "ratio_distinct_value": "0.99",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "3",
        "data_lenght_max": "18",
        "min_value": "0.51",
        "max_value": "49.65",
        "mean": "15.38",
        "median": "12",
        "mode": "4.15",
        "variance": "137.1",
        "std": "11.71",
        "first_quartile": "6",
        "third_quartile": "22",
        "iqr": "16",
        "minimum": "-2.0",
        "maximum": "30.0",
        "negative_outliner_datapoint": "137",
        "positive_outliner_datapoint": "0",
        "top_5_data_value": [
            {
                "data_value": "39.48",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "13.187999999999999",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "22.428",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "4.4639999999999995",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "4.154",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XX.XXX",
                "count_pattern": "259",
                "pattern_ratio": "0.259"
            },
            {
                "pattern": "X.XXX",
                "count_pattern": "195",
                "pattern_ratio": "0.195"
            },
            {
                "pattern": "XX.XXXX",
                "count_pattern": "127",
                "pattern_ratio": "0.127"
            },
            {
                "pattern": "X.XXXX",
                "count_pattern": "107",
                "pattern_ratio": "0.107"
            },
            {
                "pattern": "XX.XX",
                "count_pattern": "97",
                "pattern_ratio": "0.097"
            }
        ]
    },
    "Total": {
        "dataType": "float64",
        "is_primary_key": "False",
        "distinct_value": "990",
        "ratio_distinct_value": "0.99",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "4",
        "data_lenght_max": "18",
        "min_value": "10.68",
        "max_value": "1042.65",
        "mean": "322.97",
        "median": "254",
        "mode": "87.23",
        "variance": "60459.6",
        "std": "245.89",
        "first_quartile": "124",
        "third_quartile": "471",
        "iqr": "347",
        "minimum": "-49.5",
        "maximum": "644.5",
        "negative_outliner_datapoint": "131",
        "positive_outliner_datapoint": "0",
        "top_5_data_value": [
            {
                "data_value": "829.08",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "276.948",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "470.98800000000006",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "93.744",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "87.234",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XXX.XXX",
                "count_pattern": "358",
                "pattern_ratio": "0.358"
            },
            {
                "pattern": "XXX.XXXX",
                "count_pattern": "166",
                "pattern_ratio": "0.166"
            },
            {
                "pattern": "XXX.XX",
                "count_pattern": "120",
                "pattern_ratio": "0.12"
            },
            {
                "pattern": "XXX.XXXXXXXXXXXXXX",
                "count_pattern": "106",
                "pattern_ratio": "0.106"
            },
            {
                "pattern": "XX.XXX",
                "count_pattern": "91",
                "pattern_ratio": "0.091"
            }
        ]
    },
    "Date": {
        "dataType": "object",
        "is_primary_key": "False",
        "distinct_value": "89",
        "ratio_distinct_value": "0.089",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "8",
        "data_lenght_max": "9",
        "top_5_data_value": [
            {
                "data_value": "2/7/2019",
                "count_data_value": "20",
                "value_ratio": "0.02"
            },
            {
                "data_value": "2/15/2019",
                "count_data_value": "19",
                "value_ratio": "0.019"
            },
            {
                "data_value": "1/8/2019",
                "count_data_value": "18",
                "value_ratio": "0.018"
            },
            {
                "data_value": "3/2/2019",
                "count_data_value": "18",
                "value_ratio": "0.018"
            },
            {
                "data_value": "3/14/2019",
                "count_data_value": "18",
                "value_ratio": "0.018"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "X/XX/XXXX",
                "count_pattern": "677",
                "pattern_ratio": "0.677"
            },
            {
                "pattern": "X/X/XXXX",
                "count_pattern": "323",
                "pattern_ratio": "0.323"
            }
        ]
    },
    "Time": {
        "dataType": "object",
        "is_primary_key": "False",
        "distinct_value": "506",
        "ratio_distinct_value": "0.506",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "5",
        "data_lenght_max": "5",
        "top_5_data_value": [
            {
                "data_value": "19:48",
                "count_data_value": "7",
                "value_ratio": "0.007"
            },
            {
                "data_value": "14:42",
                "count_data_value": "7",
                "value_ratio": "0.007"
            },
            {
                "data_value": "17:38",
                "count_data_value": "6",
                "value_ratio": "0.006"
            },
            {
                "data_value": "17:36",
                "count_data_value": "5",
                "value_ratio": "0.005"
            },
            {
                "data_value": "19:44",
                "count_data_value": "5",
                "value_ratio": "0.005"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XX:XX",
                "count_pattern": "1000",
                "pattern_ratio": "1.0"
            }
        ]
    },
    "Payment": {
        "dataType": "object",
        "is_primary_key": "False",
        "distinct_value": "3",
        "ratio_distinct_value": "0.003",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "4",
        "data_lenght_max": "11",
        "top_5_data_value": [
            {
                "data_value": "Ewallet",
                "count_data_value": "345",
                "value_ratio": "0.345"
            },
            {
                "data_value": "Cash",
                "count_data_value": "344",
                "value_ratio": "0.344"
            },
            {
                "data_value": "Credit card",
                "count_data_value": "311",
                "value_ratio": "0.311"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XXXXXXX",
                "count_pattern": "345",
                "pattern_ratio": "0.345"
            },
            {
                "pattern": "XXXX",
                "count_pattern": "344",
                "pattern_ratio": "0.344"
            },
            {
                "pattern": "XXXXXX XXXX",
                "count_pattern": "311",
                "pattern_ratio": "0.311"
            }
        ]
    },
    "cogs": {
        "dataType": "float64",
        "is_primary_key": "False",
        "distinct_value": "990",
        "ratio_distinct_value": "0.99",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "4",
        "data_lenght_max": "6",
        "min_value": "10.17",
        "max_value": "993.0",
        "mean": "307.59",
        "median": "242",
        "mode": "83.08",
        "variance": "54838.64",
        "std": "234.18",
        "first_quartile": "118",
        "third_quartile": "449",
        "iqr": "331",
        "minimum": "-47.5",
        "maximum": "614.5",
        "negative_outliner_datapoint": "131",
        "positive_outliner_datapoint": "0",
        "top_5_data_value": [
            {
                "data_value": "789.6",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "263.76",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "448.56",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "89.28",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "83.08",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XXX.XX",
                "count_pattern": "534",
                "pattern_ratio": "0.534"
            },
            {
                "pattern": "XXX.X",
                "count_pattern": "242",
                "pattern_ratio": "0.242"
            },
            {
                "pattern": "XX.XX",
                "count_pattern": "185",
                "pattern_ratio": "0.185"
            },
            {
                "pattern": "XX.X",
                "count_pattern": "39",
                "pattern_ratio": "0.039"
            }
        ]
    },
    "gross_margin_percentage": {
        "dataType": "float64",
        "is_primary_key": "False",
        "distinct_value": "1",
        "ratio_distinct_value": "0.001",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "18",
        "data_lenght_max": "18",
        "min_value": "4.76",
        "max_value": "4.76",
        "mean": "4.76",
        "median": "5",
        "mode": "4.76",
        "variance": "0.0",
        "std": "0.0",
        "first_quartile": "5",
        "third_quartile": "5",
        "iqr": "0",
        "minimum": "5.0",
        "maximum": "5.0",
        "negative_outliner_datapoint": "0",
        "positive_outliner_datapoint": "1000",
        "top_5_data_value": [
            {
                "data_value": "4.7619047619999995",
                "count_data_value": "1000.0",
                "value_ratio": "1.0"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "X.XXXXXXXXXXXXXXXX",
                "count_pattern": "1000",
                "pattern_ratio": "1.0"
            }
        ]
    },
    "gross_income": {
        "dataType": "float64",
        "is_primary_key": "False",
        "distinct_value": "990",
        "ratio_distinct_value": "0.99",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "3",
        "data_lenght_max": "18",
        "min_value": "0.51",
        "max_value": "49.65",
        "mean": "15.38",
        "median": "12",
        "mode": "4.15",
        "variance": "137.1",
        "std": "11.71",
        "first_quartile": "6",
        "third_quartile": "22",
        "iqr": "16",
        "minimum": "-2.0",
        "maximum": "30.0",
        "negative_outliner_datapoint": "137",
        "positive_outliner_datapoint": "0",
        "top_5_data_value": [
            {
                "data_value": "39.48",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "13.187999999999999",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "22.428",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "4.4639999999999995",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            },
            {
                "data_value": "4.154",
                "count_data_value": "2.0",
                "value_ratio": "0.002"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "XX.XXX",
                "count_pattern": "259",
                "pattern_ratio": "0.259"
            },
            {
                "pattern": "X.XXX",
                "count_pattern": "195",
                "pattern_ratio": "0.195"
            },
            {
                "pattern": "XX.XXXX",
                "count_pattern": "127",
                "pattern_ratio": "0.127"
            },
            {
                "pattern": "X.XXXX",
                "count_pattern": "107",
                "pattern_ratio": "0.107"
            },
            {
                "pattern": "XX.XX",
                "count_pattern": "97",
                "pattern_ratio": "0.097"
            }
        ]
    },
    "Rating": {
        "dataType": "float64",
        "is_primary_key": "False",
        "distinct_value": "61",
        "ratio_distinct_value": "0.061",
        "missing_value": "0",
        "ratio_missing_value": "0.0",
        "data_lenght_min": "3",
        "data_lenght_max": "4",
        "min_value": "4.0",
        "max_value": "10.0",
        "mean": "6.97",
        "median": "7",
        "mode": "6.0",
        "variance": "2.95",
        "std": "1.72",
        "first_quartile": "6",
        "third_quartile": "8",
        "iqr": "2",
        "minimum": "5.0",
        "maximum": "9.0",
        "negative_outliner_datapoint": "151",
        "positive_outliner_datapoint": "153",
        "top_5_data_value": [
            {
                "data_value": "6.0",
                "count_data_value": "26.0",
                "value_ratio": "0.026"
            },
            {
                "data_value": "6.6",
                "count_data_value": "24.0",
                "value_ratio": "0.024"
            },
            {
                "data_value": "9.5",
                "count_data_value": "22.0",
                "value_ratio": "0.022"
            },
            {
                "data_value": "4.2",
                "count_data_value": "22.0",
                "value_ratio": "0.022"
            },
            {
                "data_value": "5.1",
                "count_data_value": "21.0",
                "value_ratio": "0.021"
            }
        ],
        "top_5_data_pattern": [
            {
                "pattern": "X.X",
                "count_pattern": "995",
                "pattern_ratio": "0.995"
            },
            {
                "pattern": "XX.X",
                "count_pattern": "5",
                "pattern_ratio": "0.005"
            }
        ]
    }
}
```

## Attrubute: sakda.auditing_config
#### Return type: dict
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
auditing_config = {'audit':{
    'audit_missing_value': False,
    'audit_data_pattern':[
                {'column_name':'Gender', 'regex_pattern': '(Female|Male)'},
                {'column_name':'Invoice_ID', 'regex_pattern': '(^[0-9]{3}-[0-9]{2}-[0-9]{4})'}
            ],
    'audit_outlier': False,
    'audit_data_range' : [{'column_name':'Quantity', 'min': 0, 'max': 100}]
    }
}
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>', auditing_config = auditing_config)

print(get_profile.auditing_config)
```
#### Output
```
{'audit': {'audit_missing_value': False, 'define_custom_missing_value': ['.', '999'], 'audit_data_pattern': [{'column_name': 'Gender', 'regex_pattern': '(Female|Male)'}, {'column_name': 'Invoice_ID', 'regex_pattern': '(^[0-9]{3}-[0-9]{2}-[0-9]{4})'}], 'audit_outlier': False, 'audit_primary_key': False, 'audit_data_range': [{'column_name': 'Quantity', 'min': 0, 'max': 100}]}}
```

## Attrubute: sakda.audited_result
#### Return type: dict
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
auditing_config = {'audit':{
    'audit_missing_value': False,
    'audit_data_pattern':[
                {'column_name':'Gender', 'regex_pattern': '(Female|Male)'},
                {'column_name':'Invoice_ID', 'regex_pattern': '(^[0-9]{3}-[0-9]{2}-[0-9]{4})'}
            ],
    'audit_outlier': False,
    'audit_data_range' : [{'column_name':'Quantity', 'min': 0, 'max': 100}]
    }
}
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>', auditing_config = auditing_config)

print(get_profile.audited_result)
```
#### Output
```
{'audit_result': {'file_name': 'sample_supermarket_sales', 'audit_datetime': '23/09/2020 11:03:04', 'audit_data_range': [{'column_name': 'Quantity', 'range': {'min': 0, 'max': 100}, 'pass': 1000, 'not_pass': 0, 'pass_ratio': 1.0}], 'audit_data_pattern': [{'regex_pattern': '(Female|Male)', 'column_name': 'Gender', 'pass': 1000, 'not_pass': 0, 'pass_ratio': 1.0}, {'regex_pattern': '(^[0-9]{3}-[0-9]{2}-[0-9]{4})', 'column_name': 'Invoice_ID', 'pass': 1000, 'not_pass': 0, 'pass_ratio': 1.0}], 'overall_pass': 1000, 'overall_pass(%)': 1.0}}
```

## Attrubute: sakdat.audited_result_json 
#### Return type: string
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
auditing_config = {'audit':{
    'audit_missing_value': False,
    'audit_data_pattern':[
                {'column_name':'Gender', 'regex_pattern': '(Female|Male)'},
                {'column_name':'Invoice_ID', 'regex_pattern': '(^[0-9]{3}-[0-9]{2}-[0-9]{4})'}
            ],
    'audit_outlier': False,
    'audit_data_range' : [{'column_name':'Quantity', 'min': 0, 'max': 100}]
    }
}
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>', auditing_config = auditing_config)

print(get_profile.audited_result_json)
```
#### Output
```
{
    "audit_result": {
        "file_name": "sample_supermarket_sales",
        "audit_datetime": "23/09/2020 11:04:22",
        "audit_data_range": [
            {
                "column_name": "Quantity",
                "range": {
                    "min": 0,
                    "max": 100
                },
                "pass": 1000,
                "not_pass": 0,
                "pass_ratio": 1.0
            }
        ],
        "audit_data_pattern": [
            {
                "regex_pattern": "(Female|Male)",
                "column_name": "Gender",
                "pass": 1000,
                "not_pass": 0,
                "pass_ratio": 1.0
            },
            {
                "regex_pattern": "(^[0-9]{3}-[0-9]{2}-[0-9]{4})",
                "column_name": "Invoice_ID",
                "pass": 1000,
                "not_pass": 0,
                "pass_ratio": 1.0
            }
        ],
        "overall_pass": 1000,
        "overall_pass(%)": 1.0
    }
}
```

## Attrubute: dataset.audited_dataset_with_tag
#### Return type: pandas.core.frame.DataFrame
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
auditing_config = {'audit':{
    'audit_missing_value': False,
    'audit_data_pattern':[
                {'column_name':'Gender', 'regex_pattern': '(Female|Male)'},
                {'column_name':'Invoice_ID', 'regex_pattern': '(^[0-9]{3}-[0-9]{2}-[0-9]{4})'}
            ],
    'audit_outlier': False,
    'audit_data_range' : [{'column_name':'Quantity', 'min': 0, 'max': 100}]
    }
}
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>', auditing_config = auditing_config)

print(get_profile.audited_dataset_with_tag)
```
#### Output
```
--
```

## Attrubute: sakda.audited_dataset
#### Return type: pandas.core.frame.DataFrame
#### Example
```ruby
from sakdas import Sakda as sd
import pandas as pd

df = pd.read_csv('<Path-to-File>/supermarket_sales.csv')
auditing_config = {'audit':{
    'audit_missing_value': False,
    'audit_data_pattern':[
                {'column_name':'Gender', 'regex_pattern': '(Female|Male)'},
                {'column_name':'Invoice_ID', 'regex_pattern': '(^[0-9]{3}-[0-9]{2}-[0-9]{4})'}
            ],
    'audit_outlier': False,
    'audit_data_range' : [{'column_name':'Quantity', 'min': 0, 'max': 100}]
    }
}
get_profile = sd(df,'sample_supermarket_sales','<Path-to-Result>', auditing_config = auditing_config)

print(get_profile.audited_dataset)
```
#### Output
```
--
```

 


