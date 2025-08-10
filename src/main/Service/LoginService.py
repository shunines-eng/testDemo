from main.Dao.LoginDao import LoginDao

class LoginService:
    def __init__(self, db_connection):
        """初始化登录服务
        
        Args:
            db_connection: 数据库连接对象
        """
        self.dao = LoginDao(db_connection)

    def login(self, username, password):
        """处理完整的登录验证流程
        
        执行步骤:
        1. 验证用户凭证
        2. 如果验证成功，获取用户信息
        3. 记录登录状态
        4. 返回登录结果
        
        Args:
            username (str): 用户名，需符合长度要求
            password (str): 密码，需符合长度要求
            
        Returns:
            tuple: (验证结果bool, 消息str)
                  - 成功时返回 (True, "[角色]登录成功")
                  - 失败时返回 (False, "错误原因")
                  
        Example:
            >>> service.login("admin", "123456")
            (True, "administrator登录成功")
        """
        # 验证用户凭证
        valid, message = self.dao.validate_user(username, password)
        
        if not valid:
            return False, message
            
        try:
            # 获取完整的用户信息
            user_info = self.dao.get_user_info(username)
            
            # 更新最后登录时间
            self.dao.update_last_login(user_info["id"])
            
            # 记录登录成功日志
            print(f"用户 {username} 登录成功，角色: {user_info['role']}")
            
            return True, f"{user_info['role']}登录成功"
            
        except Exception as e:
            # 记录错误日志
            print(f"登录处理错误 - 用户名: {username}, 错误: {str(e)}")
            return False, "登录处理异常"
