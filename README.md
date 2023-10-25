Tree Ensemble models particularly Cross Gradient Boosting, Random Forest models seems to work particularly well with the dataset, in fact a DT model with only min_max scaled data and no optimisation achieved 60% accuracy. The reason behind this can be -  
Audio features usually have non-linear relationships with music genre. Decision tree based models usually work well with tabular data with non-linear relationships. On top of that, ensemble methods like gradient boosting allows multiple decision trees to improve accuracy. Also decision tree models are relatively robust to outliers. Also these models utilise feature importance scores based on a number of times a feature is used to split nodes, the feature importance score determines how much a feature can contribute to the model's predictions.  
Accuracy Scores :  
Stage 2 -  
| Model        | Accuracy  |
|-------------- |---------- |
| LR           | 0.51750   |
| KNN          | 0.23250   |
| SVM          | 0.08625   |
| RF           | 0.70125   |
| LR_scaled    | 0.68125   |
| KNN_scaled   | 0.64000   |
| SVM_scaled   | 0.69875   |
| RF_scaled    | 0.69625   |


Stage 3 DT, Gradient Boost, Ada Boost, ANN -  
| Model                                 | Accuracy  |
|-------------------------------------- |---------- |
| xgboost_nest_10                       | 0.710000  |
| ada_boost_nest_10                     | 0.320000  |
| ada_boost_nest_1000                   | 0.316667  |
| xgboost_nest_1000_scaled              | 0.780000  |
| xgboost_nest_1000_min_max_scaled      | 0.783333  |
| ada_boost_nest_1000_scaled            | 0.113333  |
| DT                                    | 0.600000  |
| ANN_2048_epoch100                     | 0.750000  |
| ANN_2048_epoch100_min_max_scaled      | 0.743333  |


3 sec file -  
| Model                         | Accuracy  |
|------------------------------ |---------- |
| xgb_no_scale                  | 0.86420   |
| xgb_std_scale                 | 0.86420   |
| xgb_max_abs_scale             | 0.86420   |
| xgb_min_max_scale             | 0.86453   |
| xgb_no_scale_no_leak          | 0.47250   |
| xgb_min_max_scale_no_leak     | 0.47100   |
| ANN_min_max_scaled_no_leak     | 0.45750   |
