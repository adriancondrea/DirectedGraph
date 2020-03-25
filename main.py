from ui import Ui


def run():
    try:
        ui = Ui()
    except ValueError as ve:
        print(ve)
        return

    ui.run()


run()
