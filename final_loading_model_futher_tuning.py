import xgboost

#load the model
# our best performing model is a xgboost model
best_model_xgboost = xgboost.Booster(model_file='best_model_xgboost.model')

# further tuning
def update_xgboost_model(existing_model, new_data, num_additional_rounds=10, custom_params=None):
    """
    xgboost models only accept DMatrix object as new data for further tuning
    can convert pd.DataFrame with xgboost.DMatrix(df)
    Parameters:
    - existing_model: loaded model
    - new_data: additional data for t
    - num_additional_rounds: Number of additional training rounds/iterations.
    - custom_params: Dictionary of custom XGBoost parameters (optional).

    Returns:
    - Updated XGBoost model.
    """
    new_data_dmatrix = xgb.DMatrix(new_data)
    if custom_params:
        existing_model.set_param(custom_params)
    existing_model.update(new_data_dmatrix, num_additional_rounds)

    return existing_model
