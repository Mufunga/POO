from controllers.app_controller import App_controller
from colorama import init

def main():
    """Launch application"""
    # for color in window console
    init(autoreset=True)

    app = App_controller()
    app.start()

if __name__ == "__main__":
    main()

