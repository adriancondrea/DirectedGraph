from ui import Ui


def run():
    try:
        ui = Ui()
    except ValueError as ve:
        print(ve)
        return
    except FileNotFoundError:
        print('invalid file to read from!')
        return
    ui.run()

run()