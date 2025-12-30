# 🎥 Bellman Equation Visualization

> A **Manim**-powered animation that intuitively derives the Bellman Equation for Reinforcement Learning.

This project uses [Manim](https://www.manim.community/) (Mathematical Animation Engine) to create a visual derivation of the Bellman Equation. It breaks down complex mathematical concepts into digestible steps—from the basic definition of Return to the Bellman Optimality Equation—complete with a concrete numerical example.

---

## 🎬 Animation Overview

The animation (`BellmanDerivation` scene) covers **5 key concepts** in a fluid narrative:

1.  **The Goal:** Defining Expected Return ($G_t$) and explaining recursive discounting.
2.  **The Value Function:** Defining $v_{\pi}(s)$ as an expectation of the return.
3.  **Bellman Expectation Equation:** Breaking down the expectation into **Policy** (averaging actions) and **Dynamics** (averaging outcomes).
4.  **Bellman Optimality Equation:** Transitioning from "averaging" to "maximizing" (Greedy approach) to find the best policy.
5.  **Concrete Example:** A numerical tree diagram (State X) comparing actions $A_1$ vs $A_2$ to visually calculate the optimal value (referencing Slide 23 logic).

---

## 🛠️ Prerequisites & Installation

### 1. System Dependencies (macOS / Apple Silicon)

Manim requires **FFmpeg** for video rendering and **LaTeX** for equation rendering.

```bash
# 1. Install video and graphics engines
brew install py3cairo ffmpeg

# 2. Install LaTeX (Required for math equations)
brew install --cask basictex

# 3. Install required LaTeX packages
# (Note: You may need to restart your terminal after step 2)
sudo tlmgr update --self
sudo tlmgr install standalone preview dvisvgm
```

*(Windows Users: Install FFmpeg and MiKTeX manually and ensure they are in your System PATH.)*

### 2. Python Environment Setup

It is recommended to run this in a virtual environment.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate

# Install Manim
pip install manim
```

---

## 🚀 How to Run

1.  **Navigate** to the project folder:
    ```bash
    cd /Users/muhammedfarrag/3D-Render/Bellman-Equation
    ```

2.  **Run the Render Command**:
    ```bash
    manim -pql bellman.py BellmanDerivation
    ```

### 🎛️ Command Flags Explained

| Flag | Meaning | Description |
| :--- | :--- | :--- |
| `-p` | **Preview** | Automatically opens the video file after rendering. |
| `-ql` | **Quality: Low** | 480p @ 15fps. Fastest for testing/iterating. |
| `-qm` | **Quality: Medium** | 720p @ 30fps. Good balance of speed and quality. |
| `-qh` | **Quality: High** | 1080p @ 60fps. Use this for final presentation/export. |

---

## 📂 Output Structure

After rendering, Manim creates a `media` directory organized by resolution:

```plaintext
media/
└── videos/
    └── bellman/
        ├── 480p15/             # Low quality output (fast render)
        └── 1080p60/            # High quality output (final render)
            └── BellmanDerivation.mp4
```

---

## ⚠️ Common Issues

*   **LaTeX Error (`standalone.cls` not found):**
    *   Run: `sudo tlmgr install standalone preview`
*   **FileNotFoundError (`dvisvgm`):**
    *   Run: `sudo tlmgr install dvisvgm`
    *   Ensure **Ghostscript** is installed: `brew install ghostscript`
