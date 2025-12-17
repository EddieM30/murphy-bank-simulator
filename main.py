from managers.screen_manager import ScreensManager
from database import initialize_databases
import migrate_add_user_status


if __name__ == "__main__":
    initialize_databases()
    migrate_add_user_status.migrate()
    ScreensManager.main_menu()
