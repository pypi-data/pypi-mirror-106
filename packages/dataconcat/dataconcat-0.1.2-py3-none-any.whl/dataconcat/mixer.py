# %%
import pathlib
from pathlib import Path

import maya
import pandas as pd
import typer
from genericpath import exists

app = typer.Typer()


def read_csv_fname(f: Path):
    frame: pd.DataFrame = pd.read_csv(f)
    frame["Filename"] = f.stem
    return frame


@app.command()
def curator(
    folder: Path = typer.Argument(
        ...,
        help="The folder we want to run for the task on. Make sure to not make too big of a file.",
        exists=True,
        file_okay=False,
        dir_okay=True,
    )
):
    csv_files = folder.glob("*.csv")
    current = maya.now()
    local_time = current.local_datetime()

    current_directory = Path.cwd()

    day, month, year = local_time.day, local_time.month, local_time.year

    df_from_each_file = map(read_csv_fname, csv_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
    curation = concatenated_df[["Curator", "Playlist", "Filename"]]

    curr_path = current_directory / f"curation-{month:0>2.0f}-{day}-{year}.csv"
    curation.to_csv(curr_path)


if __name__ == "__main__":
    app()
