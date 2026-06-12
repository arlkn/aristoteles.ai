import os
import importlib.util
import inspect
from langchain_core.tools import BaseTool

class ToolsManager:
    def __init__(self, tools_dir="tools"):
        self.tools_dir = tools_dir
        if not os.path.exists(self.tools_dir):
            os.makedirs(self.tools_dir)
            
    def get_all_tools(self):
        """
        Dynamically loads all .py files in tools/ and returns Langchain @tool objects.
        """
        tools = []
        for filename in os.listdir(self.tools_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                filepath = os.path.join(self.tools_dir, filename)
                module_name = f"dynamic_tools_{filename[:-3]}"
                
                try:
                    # Dinamik olarak modülü yükle
                    spec = importlib.util.spec_from_file_location(module_name, filepath)
                    if spec and spec.loader:
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        
                        # Modül içindeki tüm Langchain toollarını (BaseTool) bul
                        for name, obj in inspect.getmembers(module):
                            if isinstance(obj, BaseTool):
                                tools.append(obj)
                except Exception as e:
                    print(f"[Warning] {filename} yüklenirken hata oluştu: {e}")
                    
        return tools
