import os
import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich.live import Live
from rich.text import Text
from rich import box
from langchain_core.messages import HumanMessage

from agent import build_agent
from memory_manager import MemoryManager

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    console = Console()
    
    # Başlangıç animasyonu
    with console.status("[bold cyan]Aristoteles uyanıyor ve sistemleri kontrol ediyor...[/bold cyan]", spinner="dots"):
        time.sleep(1) # Efekt için kısa bir bekleme
        try:
            agent = build_agent()
            memory_manager = MemoryManager()
        except Exception as e:
            console.print(f"[bold red]Ajan başlatılırken hata oluştu: {e}[/bold red]")
            console.print("[yellow]LM Studio'nun açık olduğundan ve http://localhost:1234/v1 adresinden hizmet verdiğinden emin olun.[/yellow]")
            sys.exit(1)
        time.sleep(0.5)

    clear_screen()
    
    # Karşılama ekranı
    welcome_text = Text("🤖 Aristoteles AI", justify="center", style="bold cyan")
    welcome_text.append("\nTerminal'in yeni düşünürü. Çıkmak için 'quit', 'exit' veya 'çıkış' yazabilirsiniz.", style="italic white")
    console.print(Panel(welcome_text, box=box.ROUNDED, border_style="cyan"))
    
    # LangGraph state'ini tutacağımız değişken
    messages = []

    
    while True:
        try:
            user_input = Prompt.ask("\n[bold green]Sen[/bold green]")
            
            if user_input.lower() in ["quit", "exit", "çıkış", "q"]:
                console.print("\n[bold cyan]Aristoteles:[/bold cyan] Görüşmek üzere, düşünceler seninle olsun!")
                break
                
            if not user_input.strip():
                continue

            # Kullanıcı mesajını listeye ekle
            messages.append(HumanMessage(content=user_input))

            console.print("\n[bold cyan]Aristoteles[/bold cyan]")
            
            ai_content = ""
            final_messages = messages
            
            # Dinamik markdown streaming için Live bloğu
            with Live(Markdown("*(Düşünüyor...)*"), refresh_per_second=15, transient=False) as live:
                try:
                    state = {"messages": messages}
                    
                    # Agent'i stream mode ile çağır (Hem mesaj chunklarını hem de en son state'i al)
                    for event in agent.stream(state, stream_mode=["messages", "values"]):
                        mode, data = event
                        
                        # Streaming karakterleri (chunk by chunk)
                        if mode == "messages":
                            msg, metadata = data
                            if metadata.get("langgraph_node") == "chatbot":
                                if hasattr(msg, "content") and isinstance(msg.content, str) and msg.content:
                                    ai_content += msg.content
                                    live.update(Markdown(ai_content))
                                elif hasattr(msg, "tool_calls") and msg.tool_calls:
                                    live.update(Markdown(f"*(Araç kullanılıyor: {msg.tool_calls[0]['name']}...)*"))
                        
                        # State (Values) güncellemeleri
                        elif mode == "values":
                            final_messages = data["messages"]
                            
                except Exception as e:
                    ai_content = f"Bir hata oluştu: {str(e)}. LM Studio'nun arka planda çalıştığına emin olun."
                    live.update(Markdown(ai_content))
                    messages.pop() # Hatalı gönderimi geri al
                    continue

            # Güncel state'i ana döngüye ata
            messages = final_messages
            
            # Etkileşimi Obsidian benzeri Markdown hafızasına kaydet
            memory_manager.add_interaction(user_input, ai_content)

        except KeyboardInterrupt:
            console.print("\n[bold cyan]Aristoteles:[/bold cyan] Görüşmek üzere, düşünceler seninle olsun!")
            break
        except Exception as e:
            console.print(f"\n[bold red]Beklenmeyen bir hata oluştu: {e}[/bold red]")
            break

if __name__ == "__main__":
    main()
