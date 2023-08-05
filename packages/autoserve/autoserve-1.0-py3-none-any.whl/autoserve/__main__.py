import os
import typer
import pathlib
from autoserve import __version__


app = typer.Typer(add_completion=False)
curr_dir = pathlib.Path(os.getcwd())


@app.command()
def spelling(
    port: int = typer.Option(8501, help="Port number"),
    model_folder: pathlib.Path = typer.Option(
        curr_dir / "models", help="Folder that contains all Rasa NLU models"
    ),
    project_folder: pathlib.Path = typer.Option(
        curr_dir, help="The Rasa project folder (for custom component paths"
    ),
):
    """Check the effect of spelling on NLU predictions."""
    pass
    
    
@app.command()
def version():
    """Prints the current version"""
    print(f"{__version__}")

app()