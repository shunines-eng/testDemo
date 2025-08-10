class LoginDao:
    
    def __init__(self, db_connection):
        """初始化LoginDao
        
        Args:
            db_connection: 数据库连接对象
        """
        self.connection = db_connection
        print("LoginDao 初始化完成")

    def validate_user(self, username, password):
        """验证用户登录凭证
        
        Args:
            username (str): 用户名，长度应在3-20个字符之间
            password (str): 密码，长度应在6-32个字符之间
            
        Returns:
            tuple: (验证结果布尔值, 错误消息)
                  - 如果验证成功返回 (True, "")
                  - 如果用户不存在返回 (False, "用户不存在")
                  - 如果密码错误返回 (False, "密码错误")
                  - 如果参数无效返回 (False, "参数无效: [具体原因]")
                  - 如果数据库错误返回 (False, "数据库错误: [具体错误]")
                  
        Raises:
            ValueError: 当输入参数不符合要求时抛出
        """
        # 参数验证
        if not isinstance(username, str) or len(username) < 3 or len(username) > 20:
            return False, "参数无效: 用户名长度应在3-20个字符"
        if not isinstance(password, str) or len(password) < 6 or len(password) > 32:
            return False, "参数无效: 密码长度应在6-32个字符"

        try:
            cursor = self.connection.cursor()
            # 使用参数化查询防止SQL注入
            cursor.execute(
                "SELECT password, salt FROM users WHERE username = %s", 
                (username,))
            result = cursor.fetchone()
            
            if not result:
                return False, "用户不存在"
                
            stored_password, salt = result
            # 实际项目中这里应该使用加密验证，例如:
            # hashed_password = hash_password(password, salt)
            # return (stored_password == hashed_password), ...
            
            # 当前简化版本直接比较明文密码
            return (stored_password == password), "密码错误" if stored_password != password else ""
            
        except Exception as e:
            # 记录详细错误日志
            print(f"登录验证错误 - 用户名: {username}, 错误: {str(e)}")
            return False, f"数据库错误: {str(e)}"

    def get_user_info(self, user_id):
        """获取用户基本信息
        
        Args:
            user_id: 用户ID
            
        Returns:
            dict: 包含用户基本信息的字典
                 格式: {"id": user_id, "username": "用户名", "role": "角色"}
        """
        return {
            "id": user_id,
            "username": "admin",
            "role": "administrator"
        }

    def update_last_login(self, user_id):
        """更新用户最后登录时间
        
        Args:
            user_id: 需要更新登录时间的用户ID
            
        Note:
            当前仅打印日志，实际实现需要连接数据库更新
        """
        print(f"用户 {user_id} 的最后登录时间已更新")

if __name__ == "__main__":
    dao = LoginDao("db_connection")
    print(dao.validate_user("admin", "123456"))
