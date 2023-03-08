import api
from api import download_cat
import typer
import os

api = api.Api()
app = typer.Typer()


@app.command()
def info():
    
    info_string = f"""
    Meow Version: 0.1.0
    
    This Simple CLI app lets you get cats.
    just Cats nothing else much just cats.
    you can choose to get less cats or more cats or just cats.
    """
    typer.echo(info_string)
    
@app.command()
def meow(
        amount: int = typer.Option(1, help="The amount of cats you want to get"),
        download: bool = typer.Option(False, help="Download the cats aswell"),
        path: str = typer.Option(None, help="The path to save the cats to"),):

    if amount > 0:
        for _ in range(amount):
            cat = api.search_cat()
            typer.echo(f'{_ + 1} - url={cat["url"]} width={cat["width"]} height={cat["height"]}')
            if download or path:
                path = path if path else os.getcwd()
                if not os.path.exists(path):
                    os.makedirs(path)
                download_cat(cat['url'], f'{path}/{cat["id"]}.jpg')
    else:
        typer.echo(f':C Cannot print less then one cat.')

if __name__ == '__main__':
    app()