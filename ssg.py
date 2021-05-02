import typer
from site import *

def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest
    }
    
    site = Site(**config).build()
    typer.run(main)