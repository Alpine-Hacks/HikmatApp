# Contribution Guide

We warmly welcome and appreciate contributions to HikmatApp! Whether you're fixing bugs, suggesting new features, enhancing the documentation, or providing feedback, your input is valuable in helping us achieve our mission of providing free, offline education to students worldwide.

## Setting Up the Environment

### Windows

1. **Install Python:**
   - Download from [python.org](https://www.python.org/downloads/).
   - Ensure Python is added to PATH during installation.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/Alpine-Hacks/HikmatApp.git
   cd HikmatApp
   ```

3. **Install Dependencies:**
   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python init_db.py
   python run.py
   ```

### macOS

1. **Install Python** (via Homebrew):
   ```bash
   brew install python
   ```

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/Alpine-Hacks/HikmatApp.git
   cd HikmatApp
   ```

3. **Install Dependencies:**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python init_db.py
   python run.py
   ```

### Linux

1. **Install Python:**
   - Use your package manager, e.g., `sudo apt-get install python3`

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/Alpine-Hacks/HikmatApp.git
   cd HikmatApp
   ```

3. **Install Dependencies:**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python init_db.py
   python run.py
   ```

## How to Contribute

### Explore the Project:
- Before diving in, take some time to explore the project. Review the README, issues, and existing pull requests to understand the current state of development.

### Suggest New Features or Ideas:
- We encourage you to think creatively! If you have an idea for a new feature, an improvement, or even a new direction the project could take, don't hesitate to share it.
- Open a new issue with the "Feature Request" tag, detailing your idea and why it would benefit the project.

### Choose an Issue:
- If you're looking to contribute code, start by browsing the issue tracker. Look for issues labeled "good first issue" or "help wanted" for tasks well-suited for new contributors.

### Follow the Code of Conduct:
- Please read and adhere to our Code of Conduct. We are committed to fostering a welcoming and inclusive community, and we expect all contributors to uphold these values.

### Fork the Repository:
- Create your own copy of the repository by clicking the "Fork" button at the top right of this page.

### Create a Branch:
- Create a new branch for your contribution to keep your work organized:
  ```bash
  git checkout -b feature-branch
  ```

### Write Clean, Readable Code:
- Ensure your code adheres to the project's coding standards. Follow best practices such as clear naming conventions, thorough commenting, and including tests where applicable.

### Submit Your Changes:
- Commit your changes with descriptive commit messages:
  ```bash
  git commit -m "Add detailed description of what your changes do"
  ```
- Push your branch to your fork:
  ```bash
  git push origin feature-branch
  ```

### Open a Pull Request (PR):
- Open a pull request against the main branch. Provide a clear and concise description of what your PR does, referencing any related issues.

### Review Process:
- Once your PR is submitted, it will be reviewed by the maintainers. Be prepared to discuss your changes and make revisions if necessary. This is a collaborative process aimed at maintaining the quality and direction of the project.

### Celebrate Your Contribution:
- Once your PR is merged, celebrate your contribution! Your name will be added to the list of contributors, and your work will help shape the future of HikmatApp.

### Guidelines for Contributors

- **Be Creative**: We value innovative ideas that push the boundaries of what HikmatApp can offer. Whether it's a new feature, a UI enhancement, or a performance improvement, we welcome your creative input.

- **Maintain Quality**: Ensure that all code adheres to our style guides, includes appropriate tests, and is thoroughly documented. We aim for a clean, maintainable codebase that others can easily understand and contribute to.

- **Communicate**: If you're working on a significant feature or tackling a complex issue, keep the maintainers and community informed. Open an issue to discuss your approach before you start coding, and provide updates on your progress.

- **Follow the Code of Conduct**: Respectful communication and collaboration are essential to our community. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand the standards we expect from all contributors.

### Getting Help

If you’re new to open-source contribution or unsure about something, don’t hesitate to ask for help! You can:

- Open an issue with the "Help Wanted" label.
- Join our community discussions (if available) to ask questions and get advice from experienced contributors.
- Reach out directly via email at info.hikmatapp@gmail.com.



Thank you for contributing to HikmatApp and helping us provide educational opportunities to students worldwide!
