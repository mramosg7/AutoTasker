import click

@click.command()
@click.argument('path', type=click.Path(exists=True))
def encryipt(path:str):
    """This function reads an input file, encrypts its content using an RSA public key, and saves the result in an
    output file."""
    #
    pass;