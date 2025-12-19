from database import initialize_databases
import migrate_add_user_status
from screens.router import ScreenRouter


if __name__ == "__main__":
    initialize_databases()
    migrate_add_user_status.migrate()
    router = ScreenRouter()
    router.run()
