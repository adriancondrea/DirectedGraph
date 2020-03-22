from ui import Ui


def run():
    try:
        ui = Ui()
    except ValueError as ve:
        print(ve)

    ui.run()


run()
