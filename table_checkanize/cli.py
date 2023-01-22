import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    print("start up table-checknize")
    print(f"Hello {name}")
