<div align="center">
  <img src="https://raw.githubusercontent.com/DivyamTalwar/MediaWeaver/main/Logo.png" alt="MediaWeaver Logo" width="400"/>
  <h1 style="font-weight: bold; margin-top: 20px; font-size: 64px; text-shadow: 4px 4px 20px #00BFFF;">
    MediaWeaver
  </h1>
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=00BFFF&width=600&lines=The+Autonomous+Content+Engine.;A+Digital+Superorganism%2C+Forged+in+LangGraph.;Built+to+Automate+Digital+Media." alt="Typing SVG" /></a>
</div>

<p align="center">
    <a href="https://github.com/DivyamTalwar/MediaWeaver" target="_blank"><img src="https://img.shields.io/github/stars/DivyamTalwar/MediaWeaver?style=for-the-badge&logo=github&color=gold" alt="Stars"/></a>
    <a href="https://github.com/DivyamTalwar/MediaWeaver/network/members" target="_blank"><img src="https://img.shields.io/github/forks/DivyamTalwar/MediaWeaver?style=for-the-badge&logo=github&color=blue" alt="Forks"/></a>
    <a href="https://github.com/DivyamTalwar/MediaWeaver/issues" target="_blank"><img src="https://img.shields.io/github/issues/DivyamTalwar/MediaWeaver?style=for-the-badge&logo=github&color=red" alt="Issues"/></a>
    <a href="https://github.com/DivyamTalwar/MediaWeaver/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/DivyamTalwar/MediaWeaver?style=for-the-badge&color=brightgreen" alt="License"/></a>
    <br>
    <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python Version"/>
    <img src="https://img.shields.io/badge/LangGraph-Engine-black?style=for-the-badge" alt="LangGraph"/>
    <img src="https://img.shields.io/badge/Status-Alpha-purple?style=for-the-badge" alt="Status"/>
    <img src="https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge" alt="Contributions Welcome"/>
</p>

---

<table width="100%">
  <tr>
    <td align="center" width="33%">
      <h3>🚀 Autonomous Content Creation</h3>
      <p>From blog posts to LinkedIn updates and full videos, generated on-demand.</p>
    </td>
    <td align="center" width="33%">
      <h3>🧠 LangGraph Core</h3>
      <p>A deterministic, dispatcher-based architecture for robust and reliable tool execution.</p>
    </td>
    <td align="center" width="33%">
      <h3>📈 Multi-Platform Strategy</h3>
      <p>Generate a cohesive content plan for multiple platforms from a single topic.</p>
    </td>
  </tr>
</table>

---

> ### **📜 The Manifesto: We Are Forging Content.**
> The old guards of media operate in silos. Content creation is a manual, time-consuming process. Human creativity is shackled by the clock. **MediaWeaver** is the engine that shatters these limitations. It is a decentralized, autonomous content creation engine that operationalizes the entire content workflow—from strategy to final product—into a singular, AI entity. It compresses hours of human effort into **under 2 minutes**. We don't just create content. We forge it.

---

### **🧠 The Architecture: A Deterministic Content Engine**
MediaWeaver is not a monolithic program. It's a lean, powerful engine of specialized AI tools, orchestrated by the stateful, deterministic power of `LangGraph`. This architecture ensures that every tool is executed with precision and reliability, eliminating the unpredictability of complex agentic systems.

### **🏛️ The MediaWeaver Toolkit**

| Tool Persona | Core Function | Role in the Engine |
| :--- | :--- | :--- |
| **Content Strategist** | The Master Planner | Develops a cohesive, multi-platform content plan from a single topic. |
| **Blog Post Generator** | The Wordsmith | Crafts SEO-friendly blog posts using real-time search results. |
| **LinkedIn Post Generator**| The Networker | Creates engaging, professional posts for social media. |
| **Faceless Video Creator** | The Producer | Automates the entire video production pipeline, from script to final render. |
| **Image Creator** | The Visionary | Generates stunning visuals from text prompts. |
| **News Aggregator** | The Scout | Fetches the latest news and trends to inform content creation. |

<div align="center">
  <h3>The Agentic Symphony: A Four-Phase Workflow</h3>
  <p><em>The cyclical flow of information and decision-making, orchestrated by LangGraph.</em></p>
</div>

---

### **✨ Code Spotlight: The Anatomy of a Tool**
Elegance in code is not a luxury; it's a requirement. Here’s a glimpse into how a tool thinks. This is not just code; it's strategy, operationalized.

```python
# faceless_video.py (Illustrative Example)
def faceless_video(topic: str, chat_id: str) -> str:
    print(f"FACELESS VIDEO: Starting process for topic '{topic}'")
    try:
        # 1. Generate a script using a powerful LLM
        script = generate_script(topic)

        # 2. Create a voiceover from the script
        audio_path = create_voiceover(script)

        # 3. Source relevant images from Unsplash
        image_urls = search_unsplash_images(topic, count=5)
        image_paths = download_images(image_urls)

        # 4. Stitch it all together into a final video
        final_clip = create_video(image_paths, audio_path)
        video_path = save_video(final_clip)

        # 5. Log the action and clean up
        log_to_sheet("Video", topic, video_path)
        cleanup_files(image_paths, audio_path)

        return f"Success: Video created and saved locally at {video_path}."

    except Exception as e:
        return f"An unexpected error occurred: {e}"
```

---

### **💻 The Arsenal: A Symphony of Elite Technology**
This project is forged with a no-compromise, production-grade technology stack. We chose each tool for its power and precision.

| Category | Technology | Why We Chose It |
| :--- | :--- | :--- |
| 🚀 **Agentic AI** | `LangGraph` | For building stateful, deterministic, and reliable multi-tool applications. The absolute core. |
| | `LangChain` | The foundational toolkit for composing LLM-powered tools and chains. |
| 🧠 **AI/ML** | `Gemini 2.5 Flash` | For cutting-edge, high-speed language generation and reasoning. |
| | `gTTS` | For clear, natural-sounding text-to-speech conversion. |
| ⚙️ **Core & Backend** | `Python` | The lingua franca of AI. Fast, powerful, and supported by a massive ecosystem. |
| | `FastAPI` | For building blazingly fast, modern, and robust APIs to serve our models. |
| 🐳 **Infra & Ops** | `Docker` | For containerizing every part of our system for perfect reproducibility. |
| | `Google Sheets` | For simple, effective logging and tracking of all generated content. |

---

### **🛠️ Ignition Sequence: Unleash the Engine**

#### 1. **Clone the Fortress**
```bash
git clone https://github.com/DivyamTalwar/MediaWeaver.git
cd MediaWeaver
```

#### 2. **Assemble the Arsenal**
```bash
python -m venv venv
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

#### 3. **Arm the System**
Create a `.env` file and a `credentials.json` file from the root directory. This is your command console.

**A. Environment Variables (`.env`)**
```env
# .env: Your secret keys to power the machine
GOOGLE_API_KEY="your-google-api-key"
UNSPLASH_API_KEY="your-unsplash-api-key"
HUGGING_FACE_API_KEY="your-hugging-face-api-key"
SHEET_ID="your-google-sheet-id"
```

**B. Google Credentials (`credentials.json`)**

1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Create a new project or select an existing one.
3.  Enable the **Google Sheets API** and **Google Drive API**.
4.  Create credentials for a **Service Account**.
5.  Download the JSON file, rename it to `credentials.json`, and place it in the root directory of the project.
6.  Share your Google Sheet with the `client_email` found in your `credentials.json` file.

#### 4. **Execute**
```bash
python main.py
```

---

### **📈 The Roadmap: Charting the Future**
- ✅ **Phase 1:** Core Content Generation Toolkit & Deterministic LangGraph Engine
- ⏳ **Phase 2:** Real-time Trend Analysis & Proactive Content Suggestions
- 💡 **Phase 3:** Advanced Content Customization (Tone, Style, Voice) & Multi-Language Support
- 🚀 **Phase 4:** Self-Optimizing Content Strategies via Reinforcement Learning
- 🌐 **Phase 5:** Interactive Web Dashboard for Managing and Visualizing Content Workflows

---

### **🤝 Call to Arms: Join the Revolution**
This is more than a project; it's a movement. If you are an engineer, a marketer, or a visionary, your contributions are mission-critical.
*   **⭐ Star the project** to show your support for the future of automated media.
*   **🍴 Fork the repo** and submit a PR with your enhancements.
*   **💡 Open an issue** with new ideas, bug reports, or feature requests.
*   **🤖 Build a new Media Tool** and add it to the engine.

---

<p align="center">
  <a href="https://github.com/DivyamTalwar">
    <img src="https://github-readme-stats.vercel.app/api?username=DivyamTalwar&theme=merko&hide_border=false&include_all_commits=true&count_private=true&bg_color=00000000&border_color=00000000" alt="Divyam's GitHub Stats"/>
    <img src="https://nirzak-streak-stats.vercel.app/?user=DivyamTalwar&theme=merko&hide_border=false&background=00000000&border=00000000" alt="Divyam's GitHub Streak"/>
  </a>
</p>
