from . import cli

if __name__ == '__main__':
    with cli.handle_errors():
        cli.main()
