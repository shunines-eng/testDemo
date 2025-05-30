class LoginDao:
    """用户登录数据访问对象(DAO)类
    
    负责处理与用户登录相关的数据库操作，包括用户验证、用户信息获取和登录时间更新等。
    """
    
    def __init__(self, db_connection):
        """初始化LoginDao实例
        
        Args:
            db_connection: 数据库连接对象
        """
        self.connection = db_connection  # 存储数据库连接供后续方法使用
        print("LoginDao 初始化完成")

    def validate_user(self, username, password):
        """验证用户登录凭据
        
        Args:
            username (str): 用户名
            password (str): 密码
            
        Returns:
            tuple: (验证结果bool, 错误信息str)
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT password FROM users WHERE username = %s", 
                (username,))
            result = cursor.fetchone()
            if not result:
                return False, "用户不存在"
            return (result[0] == password), "密码错误" if result[0] != password else ""
        except Exception as e:
            return False, f"数据库错误: {str(e)}"

    def get_user_info(self, user_id):
        """获取指定用户的基本信息
        
        Args:
            user_id (int/str): 用户ID
            
        Returns:
            dict: 包含用户信息的字典，格式为:
                {
                    "id": 用户ID,
                    "username": 用户名,
                    "role": 用户角色
                }
                
        Note:
            这是一个示例实现，实际项目中应该从数据库查询用户信息
        """
        # 示例返回数据 - 实际项目应该从数据库查询
        return {
            "id": user_id,
            "username": "admin",
            "role": "administrator"
        }

    def update_last_login(self, user_id):
        """更新用户的最后登录时间
        
        Args:
            user_id (int/str): 要更新的用户ID
            
        Note:
            这是一个示例实现，实际项目中应该执行SQL更新操作
        """
        # 这里应该实现更新最后登录时间的SQL
        # 示例仅打印信息 - 实际项目应该执行数据库更新
        print(f"用户 {user_id} 的最后登录时间已更新")

# 测试代码
if __name__ == "__main__":
    # 创建LoginDao实例进行测试
    dao = LoginDao("db_connection")
    # 测试用户验证功能
    print(dao.validate_user("admin", "123456"))
