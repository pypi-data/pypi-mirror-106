# Функция для анализа содержимого датафреймов
def view_types(data, dropna=True):
    """
    Вывод отчета с анализом содержимого объекта data, подсчет представленных типов данных
    Parameters
    ----------
    data : DataFrame, Series, dict, list, другой тип, преобразуемый к DataFrame
        Объект DataFrame или приводимый к DataFrame для анализа
    dropna : bool, default True
        Не включать NaN в расчет количества уникальных значений
    Returns
    -------
    None
    
    2021-05-20 (c) Nikolay Ganibaev
    """
    from pandas import DataFrame
    data = DataFrame(data)
    columns_exch = {
        "<class 'str'>": 'str', "<class 'int'>": 'int', "<class 'float'>": 'float',
        "<class 'list'>": 'list', "<class 'dict'>": 'dict',
        "<class 'datetime.datetime'>": 'datetime',
        "<class 'pandas._libs.tslibs.timestamps.Timestamp'>": 'Timestamp',
    }
    df_output = DataFrame(
        data[data[c].notna()][c].apply(type).value_counts() for c in data.columns
    ).fillna(0).astype(int)
    if data.isna().any().any():
        df_output['NaN'] = data.isna().sum()
    df_output['(min)'] = [data[c].dropna().min() for c in data.columns]
    df_output['(max)'] = [data[c].dropna().max() for c in data.columns]
    df_output['(unique)'] = [data[c].astype(str).nunique(dropna) for c in data.columns]
    df_output.columns = [columns_exch.get(str(x), x) for x in df_output.columns]
    display(df_output.head(60))
    print("{} rows x {} columns".format(*data.shape))

