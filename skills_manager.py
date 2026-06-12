import os

class SkillsManager:
    def __init__(self, skills_dir="skills"):
        self.skills_dir = skills_dir
        if not os.path.exists(self.skills_dir):
            os.makedirs(self.skills_dir)
            
    def get_all_skills(self):
        """
        Reads all .md files in the skills folder and concatenates them 
        into a single string for the System Prompt.
        """
        skills_text = ""
        for filename in os.listdir(self.skills_dir):
            if filename.endswith(".md"):
                filepath = os.path.join(self.skills_dir, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    skills_text += f"\n--- Yetenek (Skill): {filename} ---\n"
                    skills_text += f.read() + "\n"
        return skills_text
