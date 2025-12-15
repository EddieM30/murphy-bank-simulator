from screen_manager import ScreensManager
from database import initialize_databases


if __name__ == "__main__":
    initialize_databases()
    ScreensManager.main_menu()
