from main.Dao.LoginDao import LoginDao

class LoginService:
    def __init__(self, db_connection):
        """初始化登录服务
        
        Args:
            db_connection: 数据库连接对象
        """
        self.dao = LoginDao(db_connection)

    def login(self, username, password):
        """处理登录验证逻辑
        
        Args:
            username (str): 用户名
            password (str): 密码
            
        Returns:
            tuple: (验证结果bool, 消息str)
        """
        # 使用DAO进行用户验证
        valid, message = self.dao.validate_user(username, password)
        
        if valid:
            # 获取用户信息用于角色验证
            user_info = self.dao.get_user_info(username)
            return (True, f"{user_info['role']}登录成功")
        return (False, message)
