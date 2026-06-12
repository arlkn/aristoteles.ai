# Aristoteles AI 🤖

Aristoteles, LangGraph ve LM Studio altyapısı kullanılarak geliştirilmiş, yerel (local) ortamda çalışan dinamik ve akıllı bir terminal asistanıdır. Kendi yeteneklerini (`skills`) ve araçlarını (`tools`) dinamik olarak öğrenebilir. Tüm etkileşimler Obsidian benzeri günlük `.md` formatında `memory/` klasörüne kaydedilir.

## ⚙️ Özellikler

- **Dinamik Yetenekler (Skills):** `skills/` klasörüne ekleyeceğiniz `.md` dosyaları otomatik olarak okunur ve Aristoteles'in karakterine dahil edilir.
- **Dinamik Araçlar (Tools):** `tools/` klasörüne ekleyeceğiniz LangChain `@tool` fonksiyonlarını içeren `.py` dosyaları otomatik olarak yüklenir ve kullanılabilir hale gelir.
- **Güzel Terminal Arayüzü:** Rich kütüphanesi kullanılarak tasarlanmış, akıcı (streaming) ve şık bir deneyim.
- **Genişletilebilir Hafıza:** Konuşmalar, gün gün markdown formatında arşivlenir.

---

## 🛠️ Kurulum Rehberi

Projenin tamamen yerel makinenizde ve güvenli bir şekilde çalışabilmesi için aşağıdaki adımları sırasıyla uygulamalısınız.

### 1. Python Kurulumu
Uygulama Python ile yazılmıştır. Bilgisayarınızda Python yüklü değilse:
1. [Python İndirme Sayfası](https://www.python.org/downloads/)'na gidin.
2. İşletim sisteminize uygun olan son sürümü indirin.
3. Kurulum sırasında **"Add Python to PATH"** seçeneğinin işaretli olduğundan **mutlaka emin olun**.

### 2. LM Studio Kurulumu (Yerel Yapay Zeka Sunucusu)
Aristoteles zekasını bilgisayarınızdaki LM Studio üzerinden alır.
1. [LM Studio İndirme Sayfası](https://lmstudio.ai/)'na gidin ve programı indirin.
2. Programı açıp arama kısmına `gemma-4-e4b` (veya desteklenen herhangi bir model) yazın ve indirin.
3. Soldaki menüden **"Local Server"** (Yerel Sunucu) sekmesine (çift oklu ikon) tıklayın.
4. Sağ taraftaki ayarlar bölümünden:
   - Sunucu portunun `1234` olduğundan emin olun.
   - Modeli yükleyin.
   - **"Start Server"** (Sunucuyu Başlat) butonuna tıklayın.

*(Not: Sunucu başarıyla başladıysa `http://localhost:1234/v1` adresinden istek dinliyor demektir.)*

### 3. Projeyi Bilgisayarınıza Kurma
Terminal (CMD veya PowerShell) açın ve projenin bulunduğu dizine gidin:
```bash
# Proje dizinine girin
cd path/to/aristotales.ai

# Gerekli Python kütüphanelerini kurun
pip install -r requirements.txt
```

### 4. Aristoteles'i Uyandırın!
Her şey hazırsa terminalinizde aşağıdaki komutu çalıştırın:
```bash
python main.py
```
Aristoteles başlatılırken size kısa bir yükleme ekranı gösterecek, ekranı temizleyecek ve sohbet paneli ile karşınıza çıkacaktır.

---

## 🧩 Araç (Tool) ve Yetenek (Skill) Geliştirme

**Yeni Bir Yetenek (Skill) Eklemek:**
`skills/` klasörü içine `benim_kuralim.md` adında bir dosya oluşturup içine düz metin olarak komutlarınızı yazabilirsiniz. Aristoteles bunu anında benimseyecektir.

**Yeni Bir Araç (Tool) Eklemek:**
`tools/` klasörü içine örneğin `hava_durumu.py` adında bir dosya oluşturun:
```python
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Belirtilen şehrin hava durumunu getirir."""
    return f"{city} için hava şu an harika!"
```
Uygulamayı yeniden başlattığınızda Aristoteles hava durumunu öğrenme yeteneği kazanmış olacaktır!

Görüşmek üzere, düşünceler seninle olsun! 🦉
