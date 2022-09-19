'''

1.单元测试和测试用例
  Python标准库中的模块unittest提供了代码测试工具
  
  一、单元测试 用于核实函数的某个方面没有问题
  
  二、测试用例 是一组单元测试,这些单元测试一起核实函数
  在各种情形下的行为都符合要求.
  良好的测试用例考虑到了函数可能收到的各种输入,
  包含针对所有这些情形的测试
  
  三、全覆盖式测试 用例包含一整套单元测试,
  涵盖了各种可能的函数使用方式.
  
  四、对于大型项目,要实现全覆盖可能很难
  通常,最初只要针对代码的重要行为编写测试即可,
  等项目被广泛使用时再考虑全覆盖

'''
#demo1
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis",'joplin')
        self.assertEqual(formatted_name,"Janis Joplin")
unittest.main()
