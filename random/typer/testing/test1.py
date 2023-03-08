import typer

app = typer.Typer()

@app.command()

def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str,formal: bool = False):
    if formal:
        typer.echo(f"Goodbye {name}")
    else:
        print(f"bye {name}")

if __name__ == "__main__":
    app()