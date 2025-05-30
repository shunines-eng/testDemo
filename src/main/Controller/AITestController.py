import datetime

class AITestController:
    """测试AI功能的控制器类"""
    
    def __init__(self):
        """初始化方法"""
        self.test_message = "AI测试控制器已创建"
        
    def test_ai(self, input_text):
        """
        测试AI功能的核心方法
        :param input_text: 输入的测试文本
        :return: 包含测试结果的字典
        """
        return {
            "status": "success",
            "input": input_text,
            "output": f"AI已处理您的输入: {input_text}",
            "timestamp": datetime.datetime.now().isoformat()
        }

    def test_login_flow(self, username, password):
        """测试登录流程
        :return: 包含测试结果的字典
        """
        from main.Service.LoginService import LoginService
        service = LoginService()
        success, message = service.login(username, password)
        return {
            "test_case": "登录验证",
            "username": username,
            "success": success,
            "message": message,
            "timestamp": datetime.datetime.now().isoformat()
        }

    def get_test_message(self):
        """获取测试消息"""
        return self.test_message


if __name__ == "__main__":
    # 简单的测试代码
    controller = AITestController()
    print(controller.get_test_message())
    result = controller.test_ai("这是一条测试输入")
    print(result)
