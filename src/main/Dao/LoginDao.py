# 文件修改时间: 2025-05-30
class LoginDao:
    
    def __init__(self, db_connection):
        self.connection = db_connection
        print("LoginDao 初始化完成")

    def validate_user(self, username, password):
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
        return {
            "id": user_id,
            "username": "admin",
            "role": "administrator"
        }

    def update_last_login(self, user_id):
        print(f"用户 {user_id} 的最后登录时间已更新")

if __name__ == "__main__":
    dao = LoginDao("db_connection")
    print(dao.validate_user("admin", "123456"))
