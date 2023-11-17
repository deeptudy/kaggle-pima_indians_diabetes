import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from typing import Callable
from pandas import DataFrame, Series


# Dataframe filter functions

def dataframe_apply_func_axis_1(
  condition: dict={},
  greater_than: dict={},
  smaller_than: dict={},
  grt_or_eql: dict={},
  sml_or_eql: dict={},
  do_when_true: dict={},
  do_when_false: dict={}
) -> Callable:
  """_summary_

  Args:
      condition (dict, optional): { 'column_name': condition_value }. Defaults to {}.
      do_when_true (dict, optional): { 'column_name': value_to_change }. Defaults to {}.
      do_when_false (dict, optional): { 'column_name': value_to_change }. Defaults to {}.

  Returns:
      function: function that goes into dataframe.apply
  """
  def apply_func(x: Series):
    condition_match = all([
      1 if x[k] == v else 0
      for k,v in condition.items()
    ]) and all([
      1 if x[k] > v else 0
      for k,v in greater_than.items()
    ]) and all([
      1 if x[k] < v else 0
      for k,v in smaller_than.items()
    ]) and all([
      1 if x[k] <= v else 0
      for k,v in sml_or_eql.items()
    ]) and all([
      1 if x[k] >= v else 0
      for k,v in grt_or_eql.items()
    ])
    
    return Series({**x, **do_when_true}) if condition_match else Series({**x, **do_when_false})
  return apply_func

# Graph generations

def generate_heatmaps(
  list_of_df: list[DataFrame],
  list_of_df_title: list[str]=[],
  fig_size_width: int=10,
  fig_size_height: int=6,
  n_rows_subplot: int=1,
  n_cols_subplot: int=2,
  annotation: bool=True,
) -> None:
  """
  generate heatmaps

  Args:
      list_of_df (list[DataFrame]): _description_
      list_of_df_title (list[str], optional): _description_. Defaults to [].
      fig_size_width (int, optional): _description_. Defaults to 10.
      fig_size_height (int, optional): _description_. Defaults to 6.
      n_rows_subplot (int, optional): _description_. Defaults to 1.
      n_cols_subplot (int, optional): _description_. Defaults to 2.
      annotation (bool, optional): _description_. Defaults to True.
  """
  plt.figure(figsize=(fig_size_width, fig_size_height))
  
  idx_df = len(list_of_df)
  for i in range(idx_df):
    plt.subplot(n_rows_subplot, n_cols_subplot, i+1)
    sns.heatmap(list_of_df[i], annot=annotation)
    if i < len(list_of_df_title):
      plt.title(label=list_of_df_title[i])
  plt.show()
