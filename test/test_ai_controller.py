import unittest
from main.Controller.AITestController import AITestController

class TestAIController(unittest.TestCase):
    """AI控制器测试"""
    
    def setUp(self):
        self.controller = AITestController()
        
    def test_ai_processing(self):
        """测试AI处理功能"""
        result = self.controller.test_ai("测试输入")
        self.assertEqual("success", result["status"])
        self.assertIn("测试输入", result["output"])
        
    def test_default_message(self):
        """测试默认消息"""
        self.assertEqual(
            "AI测试控制器已创建",
            self.controller.get_test_message()
        )

if __name__ == "__main__":
    unittest.main()
