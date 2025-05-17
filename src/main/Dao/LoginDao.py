class UserRepository:
    @staticmethod
    def get_user(username):
        """模拟从数据库获取用户信息"""
        users = {
            'admin': {'password': 'admin123', 'role': 'admin'},
            'user1': {'password': 'user123', 'role': 'member'}
        }
        return users.get(username)