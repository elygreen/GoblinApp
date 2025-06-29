Game Automation Personal Project:
  A Python automation tool I built to practice GUI automation and workflow management. The project automates complex in-game tasks and demonstrates skills in process coordination, timing systems, and modular code design.
  This script handles multi-step game processes automatically, including resource management, inventory tracking, and state transitions. It's designed to run reliably for extended periods while simulating realistic user behavior.

Structure:
    Python with PyAutoGUI for mouse/keyboard automation
    Custom modules for coordinates and common functions
    Timing systems with randomization for human-like interactions
    State management for complex workflow orchestration

Smart Timing & Coordination:
  The script manages multiple concurrent timers and handles complex state transitions. For example, it tracks resource consumption over time and adjusts behavior accordingly:
  def Inside_NMZ():
      six_hour_logout = time.monotonic() + 6 * 60 * 60
      # Manages multiple timing loops with resource tracking
      while time.monotonic() < six_hour_logout:
          # Complex decision making based on available resources

Modular Architecture:
  Separated concerns into logical modules: coordinate management, common utilities, and main workflow logic. This makes the code maintainable and extensible.

Resource Management:
  Implements inventory tracking and optimization algorithms to efficiently manage in-game resources and make decisions about when to consume or save items.


Next Steps
  I'm planning to add computer vision capabilities using OpenCV to make the system more robust and self-correcting. This would eliminate the need for hardcoded coordinates and make it adaptable to different screen     configurations.



This gave me practical experience with automation frameworks, complex state management, and building systems that need to run reliably over long periods - skills that translate well to many development scenarios.
Built for learning automation concepts and Python development practices.
