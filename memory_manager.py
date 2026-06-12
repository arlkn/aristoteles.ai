import os
import datetime

class MemoryManager:
    def __init__(self, memory_dir="memory"):
        self.memory_dir = memory_dir
        if not os.path.exists(self.memory_dir):
            os.makedirs(self.memory_dir)
            
    def get_todays_file(self):
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        return os.path.join(self.memory_dir, f"{date_str}.md")

    def add_interaction(self, user_input, assistant_response):
        filepath = self.get_todays_file()
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# Aristoteles Memory - {datetime.datetime.now().strftime('%Y-%m-%d')}\n\n")
                f.write("Bu dosya Obsidian formatında günlük etkileşimleri saklar.\n\n")

        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"## [{timestamp}] Etkileşim\n\n")
            f.write(f"**Sen:**\n{user_input}\n\n")
            f.write(f"**Aristoteles:**\n{assistant_response}\n\n")
            f.write("---\n\n")

    def get_recent_history(self, limit=5):
        """
        Gelecekte model context'ine geçmişi eklemek için kullanılabilir.
        Şimdilik LangGraph'in kendi state memory'sini kullanacağız, 
        ancak buradaki dosyadan da okuma yapılabilir.
        """
        filepath = self.get_todays_file()
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        return ""
