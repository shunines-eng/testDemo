# 登录数据访问对象(DAO)类
# 负责处理与用户登录相关的数据库操作
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
            username: 用户名
            password: 密码
            
        Returns:
            tuple: (验证结果布尔值, 错误消息)
                  - 如果验证成功返回 (True, "")
                  - 如果用户不存在返回 (False, "用户不存在")
                  - 如果密码错误返回 (False, "密码错误")
                  - 如果数据库错误返回 (False, "数据库错误: [具体错误]")
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
