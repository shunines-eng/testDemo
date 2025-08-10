from main.Dao.LoginDao import LoginDao

from main.Service.LoginService import LoginService



class LoginController:

    def __init__(self, db_connection):

        """Initialize login controller123

        

        Args:

            db_connection: Database connection object

        """

        self.service = LoginService(db_connection)

        print("LoginController initialized")



    def handle_login(self, username, password):

        """Handle user login request

        

        Args:

            username (str): Username

            password (str): Password

            

        Returns:

            tuple: (Login result, Return message)

        """

        # Call service layer for login validation

        success, message = self.service.login(username, password)

        

        # Update last login time after successful login

        if success:

            # In real project this would get actual user ID

            self.service.dao.update_last_login(f"user:{username}")

        

        return {

            "success": success,

            "message": message,

            "user": self.service.dao.get_user_info(username) if success else None

        }



# Hello

if __name__ == "__main__":

    # Mock database connection

    mock_db_connection = "db_conn"

    

    controller = LoginController(mock_db_connection)

    

    # Test cases

    test_cases = [

        ("admin", "123456"),

        ("test_user", "wrong_password"),

        ("invalid_user", "any_password")

    ]

    

    for uname, pwd in test_cases:

        response = controller.handle_login(uname, pwd)

        print(f"User [{uname}] login result: {response}")
