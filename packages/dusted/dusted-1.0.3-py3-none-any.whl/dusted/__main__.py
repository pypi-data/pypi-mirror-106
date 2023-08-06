from .gui import App


def main():
    import logging
    from pathlib import Path

    import appdirs

    logfile = Path(appdirs.user_log_dir(opinion=False)) / "dusted.log"
    logging.basicConfig(
        style="{",
        format="{asctime} {levelname} {message}",
        level=logging.INFO,
        filename=logfile,
        filemode="w"
    )

    App().mainloop()


if __name__ == "__main__":
    main()
