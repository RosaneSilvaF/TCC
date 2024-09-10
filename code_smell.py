class DBManager:
    def __init__(self, conn_str):
        self.conn_str = conn_str

    def connect(self):
        print("Connecting to database with connection string: " + self.conn_str)
        return True

    def execute_query(self, query):
        print("Executing query: " + query)
        return []

    def disconnect(self):
        print("Disconnecting from database.")

class User:
    def __init__(self, id, name, age, email):
        self.id = id
        self.name = name
        self.age = age
        self.email = email

    def print_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Email: {self.email}")

    def is_adult(self):
        if self.age >= 18:
            return True
        return False

    def update_name(self, new_name):
        self.name = new_name

class UserService:
    def __init__(self):
        self.db_manager = DBManager("localhost/db")
        self.users = []
        self.logger = Logger()
        self.log_enabled = True

    def load_users(self):
        if self.db_manager.connect():
            result = self.db_manager.execute_query("SELECT * FROM users")
            for row in result:
                user = User(row[0], row[1], row[2], row[3])
                self.users.append(user)

    def get_user_by_id(self, id):
        for user in self.users:
            if user.id == id:
                return user
        return None

    def update_user_email(self, user_id, new_email):
        user = self.get_user_by_id(user_id)
        if user:
            user.email = new_email
            self.db_manager.execute_query(f"UPDATE users SET email = '{new_email}' WHERE id = {user_id}")

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            self.db_manager.execute_query(f"DELETE FROM users WHERE id = {user_id}")

    def create_user(self, id, name, age, email):
        new_user = User(id, name, age, email)
        self.users.append(new_user)
        self.db_manager.execute_query(f"INSERT INTO users (id, name, age, email) VALUES ({id}, '{name}', {age}, '{email}')")

    def print_all_users(self):
        for user in self.users:
            print(f"User {user.id}: {user.name}, {user.age}, {user.email}")
            if self.log_enabled:
                self.logger.log_info(f"User {user.id} details printed.")

    def print_all_adults(self):
        adults = [user for user in self.users if user.is_adult()]
        for user in adults:
            user.print_details()

    def disable_logging(self):
        self.log_enabled = False

    def enable_logging(self):
        self.log_enabled = True

    def perform_mass_email_update(self, new_email):
        for user in self.users:
            self.update_user_email(user.id, new_email)

class Logger:
    def log_info(self, message):
        print("INFO: " + message)

    def log_error(self, message):
        print("ERROR: " + message)

    def log_warning(self, message):
        print("WARNING: " + message)

class UserApp:
    def __init__(self):
        self.user_service = UserService()
        self.logger = Logger()

    def run(self):
        self.logger.log_info("Application started")
        self.user_service.load_users()

        self.user_service.create_user(1, "John Doe", 30, "john@example.com")
        self.user_service.create_user(2, "Jane Smith", 17, "jane@example.com")
        self.user_service.create_user(3, "Bob Johnson", 40, "bob@example.com")

        self.user_service.print_all_users()

        self.user_service.update_user_email(2, "jane.smith@school.com")

        self.user_service.delete_user(3)

        self.user_service.print_all_users()

        self.user_service.perform_mass_email_update("updated_email@example.com")

        self.user_service.print_all_adults()

        self.logger.log_info("Application finished")
        self.logger.log_warning("Ensure to review logs")

class UserStatistics:
    def __init__(self, users):
        self.users = users

    def calculate_average_age(self):
        if not self.users:
            return 0
        total_age = sum(user.age for user in self.users)
        return total_age / len(self.users)

    def find_youngest_user(self):
        if not self.users:
            return None
        return min(self.users, key=lambda user: user.age)

    def find_oldest_user(self):
        if not self.users:
            return None
        return max(self.users, key=lambda user: user.age)

    def print_statistics(self):
        avg_age = self.calculate_average_age()
        youngest = self.find_youngest_user()
        oldest = self.find_oldest_user()

        print(f"Average age: {avg_age}")
        if youngest:
            print(f"Youngest user: {youngest.name}, Age: {youngest.age}")
        if oldest:
            print(f"Oldest user: {oldest.name}, Age: {oldest.age}")

class UserAppWithStats(UserApp):
    def run(self):
        super().run()
        self.logger.log_info("Running UserAppWithStats")

        stats = UserStatistics(self.user_service.users)
        stats.print_statistics()

        self.logger.log_info("UserAppWithStats finished")

class SystemLogger:
    def log_startup(self):
        print("System is starting up...")

    def log_shutdown(self):
        print("System is shutting down...")

class SystemApp:
    def __init__(self):
        self.user_app = UserAppWithStats()
        self.system_logger = SystemLogger()

    def start(self):
        self.system_logger.log_startup()
        self.user_app.run()
        self.system_logger.log_shutdown()

class NotificationManager:
    def __init__(self):
        self.logger = Logger()

    def send_email_notification(self, user, subject, message):
        print(f"Sending email to {user.email}: {subject} - {message}")
        self.logger.log_info(f"Email sent to {user.email}")

    def send_mass_notification(self, users, subject, message):
        for user in users:
            self.send_email_notification(user, subject, message)

    def schedule_notifications(self, users, subject, message, time):
        print(f"Scheduling notifications at {time} for {len(users)} users.")
        self.send_mass_notification(users, subject, message)

class AdvancedUserService(UserService):
    def __init__(self):
        super().__init__()
        self.notification_manager = NotificationManager()

    def notify_all_users(self, subject, message):
        self.notification_manager.send_mass_notification(self.users, subject, message)

    def schedule_user_notifications(self, subject, message, time):
        self.notification_manager.schedule_notifications(self.users, subject, message, time)

class SuperApp(SystemApp):
    def __init__(self):
        super().__init__()
        self.advanced_user_service = AdvancedUserService()

    def run(self):
        self.system_logger.log_startup()
        self.advanced_user_service.load_users()
        self.advanced_user_service.notify_all_users("Important Update", "Please check your details.")
        self.system_logger.log_shutdown()

# Executando o SuperApp com muitos bad smells
super_app = SuperApp()
super_app.run()
