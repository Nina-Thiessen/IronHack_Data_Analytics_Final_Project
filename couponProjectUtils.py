import numpy as np
import pandas as pd

def replace_unknown_with_mode(X_train, X_test, outfile_prefix):
    """
    Replace the unknown values (previously encoded as 0.0) using the mode (most frequent value) seen in the TRAINING data
    If outfile_prefix is None, don't save info, otherwise save the mode info to file: model/<outfile_prefix>-train_mode_values.csv
    """

    cols_to_process = ['Bar', 'CoffeeHouse', 'CarryAway', 'RestaurantLessThan20', 'Restaurant20To50']

    info_dict={}
    for colname in cols_to_process:
        # get list of values in this column, sorted by frequency
        myvalues = X_train[colname].value_counts().index.values

        # pick the value highest in the list, skipping 0.0 (the value we're replacing)
        modeval = myvalues[0]
        if modeval == 0.0:
            modeval = myvalues[1]

        # save this info for future reference if needed
        info_dict[colname] = modeval

        X_train.loc[X_train[colname] == 0.0, colname] = modeval
        X_test.loc[X_test[colname] == 0.0, colname] = modeval

    info_df = pd.DataFrame(info_dict, index=[0])
    if not outfile_prefix is None:
        # write info to file
        info_df.to_csv(f'model/{outfile_prefix}-train_mode_values.csv', index=False)

    return X_train, X_test, info_df

