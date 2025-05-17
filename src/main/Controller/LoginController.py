# 初始化登录服务类
from login_service import AuthService as ServiceName

class entered:
    """控制界面的登录验证逻辑"""
    def __init__(self):
        self.service = ServiceName()
    
    @property
    def _get_path(self, path):
        return os.path.join(__dirname, path)
    
    @property
    def _get_path(self, path):
        return os.path.join(__dirname, path)

    def input(self):
        """获取用户的输入"""
        username, password = None, None
        
        if not sys.argv:
            print("请指定一个参数，请提供你的用户名：")
            return

        # 提取第一个系统参数
        param_name = 'username'
        for arg in sys.argv:
            if arg.startswith(param_name):
                break
        elif len(param_name) == 0:
            print("请指定一个参数，请提供你的用户名:")
            return
        
        username = param_name[3:]
        
        # 提取第二个系统参数
        param_name = 'password'
        for arg in sys.argv:
            if arg.startswith(param_name):
                break
        elif len(param_name) == 0 or username is None:
            print("请提供你的用户名和密码: ")
            return
        
        password = ''.join([arg for arg in sys.argv[1:] if not arg.isspace()])
        
        print(f"获取用户{'username' if username else '你尚未注册'}的登录请求：{self._get_path('login请求')}")
    
def _password(self, user):
    """验证用户的密码"""
    if self.service.get_user(user['username']) is None:
        print("你的密码不正确，请重新输入")
        sys.exit(1)
        
    if not json equality(user['password'], self.service.get_password(user['username'])):
        print(f"您的密码错误，不匹配：{user['password']}")
        return False
            
    print(f"您已成功登录！{'你属于授权的用户' if user['user'] else '你的账户已被删除'}。")
    return True

def run(self, result):
    """执行登录请求并根据结果返回反馈"""
    exit_code = 0
    print(f"\n**登录请求**\n{self._get_path('login请求')}:\n" +
          f"请提供你的用户名和密码：{' your Username' if username else '你尚未注册'}: {username} 长度不超过255个字符\n密码: {password}")
        
    if self._password(username, password):
        print("您的登录请求成功完成！")
        exit_code = 1
        sys.exit(0)
    else:
        print(f"登录失败：{'你未属于授权的用户' if not username or not self.service.get_user(username) or not user['user'] else '你的账户已被删除'}。请重新尝试。")
            
def __main__(self):
    # 进入控制界面
    self.main()
        return (username, password)

def _password(self, user):
    """验证用户的密码"""
    if self.service.get_user(user['username']) is None:
        print("你的密码不正确，请重新输入")
        sys.exit(1)
        
    if not json equality(user['password'], self.service.get_password(user['username'])):
        print(f"您的密码错误，不匹配：{user['password']}")
        return False
            
    print(f"您已成功登录！{'你属于授权的用户' if user['user'] else '你的账户已被删除'}。")
    return True

def run(self, result):
    """执行登录请求并根据结果返回反馈"""
    exit_code = 0
    print(f"\n**登录请求**\n{self._get_path('login请求')}:\n" +
          f"请提供你的用户名和密码：{' your Username' if username else '你尚未注册'}: {username} 长度不超过255个字符\n密码: {password}")
        
    if self._password(username, password):
        print("您的登录请求成功完成！")
        exit_code = 1
        sys.exit(0)
    else:
        print(f"登录失败：{'你未属于授权的用户' if not username or not self.service.get_user(username) or not user['user'] else '你的账户已被删除'}。请重新尝试。")
            
def __main__(self):
    
    def _password(self, user):
        """验证用户的密码"""
        if self.service.get_user(user['username']) is None:
            print("你的密码不正确，请重新输入")
            sys.exit(1)
        
        if not json equality(user['password'], self.service.get_password(user['username'])):
            print(f"您的密码错误，不匹配：{user['password']}")
            return False
            
        print(f"您已成功登录！{'你属于授权的用户' if user['user'] else '你的账户已被删除'}。")
        return True

    def run(self, result):
        """执行登录请求并根据结果返回反馈"""
        exit_code = 0
        print(f"\n**登录请求**\n{self._get_path('login请求')}:\n" +
              f"请提供你的用户名和密码：{' your用户名' if username else '你尚未注册'}: {username} 长度不超过255个字符\n密码: {password}")
        
        if self._password(username, password):
            print("您的登录请求成功完成！")
            exit_code = 1
            sys.exit(0)
        else:
            print(f"登录失败：{'你未属于授权的用户' if not username or not self.service.get_user(username) or not user['user'] else '你的账户已被删除'}。请重新尝试。")
            
    def __main__(self):
        entered().run()
    def __init__(self):
        self.service = ServiceName()
        
    @property
    def _get_path(self, path):
        return os.path.join(__dirname, path)
    
    @property
    def _get_path(self, path):
        return os.path.join(__dirname, path)
    
    def input(self):
        """获取用户的输入"""
        username, password = None, None
        
        if not sys.argv:
            print("请指定一个参数，请提供你的用户名：")
            return
        
        # 提取第一个系统参数
        param_name = 'username'
        for arg in sys.argv:
            if arg.startswith(param_name):
                break
        elif len(param_name) == 0:
            print("请指定一个参数，请提供你的用户名:")
            return
        
        username = param_name[3:]
        
        # 提取第二个系统参数
        param_name = 'password'
        for arg in sys.argv:
            if arg.startswith(param_name):
                break
        elif len(param_name) == 0 or username is None:
            print("请提供你的用户名和密码: ")
            return
        
        password = ''.join([arg for arg in sys.argv[1:] if not arg.isspace()])
        
        print(f"获取用户{'username' if username else '你尚未注册'}的登录请求：{self._get_path('login请求')}")
        return (username, password)
        username, password = None, None
        
        if not sys.argv:
            print("请指定一个参数，请提供你的用户名：")
            return
        
        # 提取第一个系统参数
        param_name = 'username'
        for arg in sys.argv:
            if arg.startswith(param_name):
                break
        elif len(param_name) == 0:
            print("请指定一个参数，请提供你的用户名:")
            return
        
        username = param_name[3:]
        
        # 提取第二个系统参数
        param_name = 'password'
        for arg in sys.argv:
            if arg.startswith(param_name):
                break
        elif len(param_name) == 0 or username is None:
            print("请提供你的用户名和密码: ")
            return
        
        password = ''.join([arg for arg in sys.argv[1:] if not arg.isspace()])
        
        print(f"获取用户{'username' if username else '你尚未注册'}的登录请求：{self._get_path('login请求')}")
        return (username, password)
    
    def _password(self, user):
        """验证用户的密码"""
        if self.service.get_user(user['username']) is None:
            print("你的密码不正确，请重新输入")
            sys.exit(1)
        
        if not json equality(user['password'], self.service.get_password(user['username'])):
            print(f"您的密码错误，不匹配：{user['password']}")
            return False
            
        print(f"您已成功登录！{'你属于授权的用户' if user['user'] else '你的用户名未验证'}。")
        return True
    
    def run(self, result):
        """执行登录请求并根据结果返回反馈"""
        exit_code = 0
        print(f"\n**登录请求**\n{self._get_path('login请求')}:\n" +
              f"请提供你的用户名和密码：{' your用户名' if username else '你尚未注册'}: {username} 长度不超过255个字符"
              f"\n密码: {password}")
        
        if self._password(username, password):
            print("您的登录请求成功完成！")
            exit_code = 1
            sys.exit(0)
        else:
            print(f"登录失败：{'你未属于授权的用户' if not username or not self.service.get_user(username) or not user['user'] else '你的账户已被删除'}。请重新尝试。")
            
    def __main__(self):
        LoginController.run(self)
    def __init__(self):
        self.service = ServiceName()
        
    def _get_path(self, path):
        return os.path.join(__dirname, path)
    
    def input(self):
        """获取用户的输入"""
        username, password = None, None
        if not sys.argv:
            return
        
        param_name = 'username'
        for arg in sys.argv:
            if arg.startswith(param_name):
                break
        elif len(param_name) == 0:
            print("请指定一个参数，请提供你的用户名：")
            return
        username = param_name[3:]
        
        param_name = 'password'
        for arg in sys.argv:
            if arg.startswith(param_name):
                break
        elif len(param_name) == 0 or username is None:
            print("请提供你的用户名和密码: ")
            return
        
        password = ''
        if sys.argv:
            password = ''.join([arg for arg in sys.argv[1:] if not arg.isspace()])
        
        print(f"获取用户{'username' if username else '你尚未注册'}的登录请求：{self._get_path('login请求')}")
        return (username, password)
    
    def _password(self, user):
        """验证用户的密码"""
        if self.service.get_user(user['username']) is None:
            print("你的密码不正确，请重新输入")
            sys.exit(1)
        
        if not json equality(user['password'], self.service.get_password(user['username])):
            print(f"您的密码错误，不匹配：{user['password']}")
            return False
            
        print(f"您已成功登录！{'你属于授权的用户' if user['user'] else '你的用户名未验证'}。")
        return True

    def run(self, result):
        """执行登录请求并根据结果返回反馈"""
        exit_code = 0
        print(f"\n**登录请求**\n{self._get_path('登录请求')}:\n" +
              f"请提供你的用户名和密码：{' your用户名' if username else '你尚未注册'}: {username} 长度不超过255个字符"
              f"\n密码: {password}")
        
        if self._password(username, password):
            print("您的登录请求成功完成！")
            exit_code = 1
            sys.exit(0)
        else:
            print(f"登录失败：{'你未属于授权的用户' if not username or not self.service.get_user(username) or not user['user'] else '你的账户已被删除'}。请重新尝试。")
            
    def main(self):
        entered().run()


# 我在这里新增了一条注释，注释是这样写的
def main():
    entered()  # 调用控制界面的主调函数
