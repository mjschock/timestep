from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px  # noqa:  F401
import plotly.graph_objs as go
import seaborn as sns

plt.switch_backend(
    "agg"
)  # https://matplotlib.org/stable/users/faq.html#work-with-threads


# This function uses plotly.express
def compare_passenger_capacity_exp(preprocessed_shuttles: pd.DataFrame):  # type: ignore[no-untyped-def]
    return (
        preprocessed_shuttles.groupby(["shuttle_type"])
        .mean(numeric_only=True)
        .reset_index()
    )


# This function uses plotly.graph_objects
def compare_passenger_capacity_go(preprocessed_shuttles: pd.DataFrame):  # type: ignore[no-untyped-def]
    data_frame = (
        preprocessed_shuttles.groupby(["shuttle_type"])
        .mean(numeric_only=True)
        .reset_index()
    )
    return go.Figure(
        [
            go.Bar(
                x=data_frame["shuttle_type"],
                y=data_frame["passenger_capacity"],
            )
        ]
    )


def create_confusion_matrix(companies: pd.DataFrame) -> plt:  # noqa: ARG001
    actuals = [0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1]
    data = {"y_Actual": actuals, "y_Predicted": predicted}
    data_df = pd.DataFrame(data, columns=["y_Actual", "y_Predicted"])
    confusion_matrix = pd.crosstab(
        data_df["y_Actual"],
        data_df["y_Predicted"],
        rownames=["Actual"],
        colnames=["Predicted"],
    )
    sns.heatmap(confusion_matrix, annot=True)
    return plt
