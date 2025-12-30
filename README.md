Bellman Equation Animation 🎥
This project uses the Manim (Mathematical Animation Engine) library to visually derive the Bellman Equation step-by-step. It is designed for Reinforcement Learning lectures to intuitively explain the math behind value functions and optimality.

🎬 Animation Overview
The video sequence covers 5 key concepts:

The Goal: Defining Expected Return (G 
t
​
 ) and recursive discounting.

The Value Function: Defining v 
π
​
 (s) as an expectation.

Bellman Expectation Equation: Breaking down the expectation into policy and dynamics (∑π…).

Bellman Optimality Equation: Transitioning from "average" to "greedy" maximization (max).

Concrete Example: A numerical tree diagram comparing actions (A 
1
​
  vs A 
2
​
 ) to determine the optimal value.

🛠️ Prerequisites & Installation
1. System Dependencies (macOS / Apple Silicon)
Manim requires FFmpeg for video rendering and LaTeX for equation rendering. Run these commands in your terminal:

Bash

# 1. Install video and graphics engines
brew install py3cairo ffmpeg

# 2. Install LaTeX (Required for math equations)
brew install --cask basictex

# 3. Install required LaTeX packages (Fixes 'standalone.cls' & 'dvisvgm' errors)
# Note: You may need to restart your terminal after step 2 before running this.
sudo tlmgr update --self
sudo tlmgr install standalone preview dvisvgm
(Windows Users: Install FFmpeg and MiKTeX manually and ensure they are in your System PATH.)

2. Python Environment Setup
It is best to run this in a virtual environment to avoid conflicts.

Bash

# Create a virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate

# Install Manim
pip install manim
🚀 How to Run
Save the Script: Ensure your Python script (e.g., bellman_animation.py) is in the project folder.

Run the Render Command:

Bash

manim -pql bellman_animation.py BellmanDerivation
🎛️ Command Flags Explained
Flag	Meaning	Description
-p	Preview	Automatically opens the video file after rendering.
-ql	Quality: Low	480p @ 15fps. Fastest for testing code.
-qm	Quality: Medium	720p @ 30fps. Good balance.
-qh	Quality: High	1080p @ 60fps. Use this for final presentation/export.

Export to Sheets

📂 Output Structure
After rendering, Manim creates a media directory:

Plaintext

media/
└── videos/
    └── bellman_animation/
        ├── 480p15/             # Low quality output
        └── 1080p60/            # High quality output
            └── BellmanDerivation.mp4
⚠️ Common Issues
LaTeX Error: File 'standalone.cls' not found: Run sudo tlmgr install standalone preview.

FileNotFoundError: 'dvisvgm': Run sudo tlmgr install dvisvgm and ensure Ghostscript is installed (brew install ghostscript).
