
from typing import Union
from amispy.base import Api,PyAmisComponent
from .formitem import Formitem


class FormEditor(Formitem):
    def __init__(self,
                 language: str = None,
                 size: str = None,
                 options: any = None,
                 
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/editor.md
        :param language: 编辑器高亮的语言，支持通过 ${xxx} 变量获取
        :param size: 编辑器高度，取值可以是 md、lg、xl、xxl
        :param options: monaco 编辑器的其它配置，比如是否显示行号等，请参考这里，不过无法设置 readOnly，只读模式需要使用 disabled: true
        """
        super(FormEditor,self).__init__(language = language,size = size,options = options,type="editor",**kwargs)
