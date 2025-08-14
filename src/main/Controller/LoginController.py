from main.Dao.LoginDao import LoginDao

from main.Service.LoginService import LoginService



class LoginController:

    def __init__(self, db_connection):

        """初始化登录控制器

        

        Args:

            db_connection: 数据库连接对象q

        """

        self.service = LoginService(db_connection)

        print("登录控制器初始化完成")



    def handle_login(self, username, password):

        """处理用户登录请求

        

        Args:

            username (str): 用户名

            password (str): 密码

            

        Returns:

            dict: 包含登录结果的字典，包含以下键：
                - success: 登录是否成功
                - message: 返回消息
                - user: 如果登录成功则为用户信息，否则为None

        """

        # 调用服务层进行登录验证

        success, message = self.service.login(username, password)

        

        # 登录成功后更新最后登录时间

        if success:

            # 在实际项目中，这里会获取真实的用户ID

            self.service.dao.update_last_login(f"user:{username}")

        

        return {

            "success": success,

            "message": message,

            "user": self.service.dao.get_user_info(username) if success else None

        }



if __name__ == "__main__":

    # 模拟数据库连接

    mock_db_connection = "db_conn"

    

    controller = LoginController(mock_db_connection)

    

    # 测试用例

    test_cases = [

        ("admin", "123456"),

        ("test_user", "wrong_password"),

        ("invalid_user", "any_password")

    ]

    
    for uname, pwd in test_cases:
        response = controller.handle_login(uname, pwd)
        print(f"用户 [{uname}] 登录结果: {response}")
