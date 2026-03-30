# GitHub Desktop Smart IDE
Tool to open pre-configured IDEs on a per-repository basis from GitHub Desktop. Uses a configuration file 
specified by [JQB DevTools](https://github.com/justinquinnb/JQB-DevTools).

# How to Use
## Installation
1. Clone this repository
2. Use your package manager of choice to install dependencies
3. Create an executable of the project with your tool of choice, like `pyinstaller` (`pyinstaller main.py --onefile`)
5. Copy the executable into your desired location

## Setup
1. Configure GH Desktop to use GitHub Desktop Smart IDE
   1. Open GitHub Desktop
   2. Open `File > Options > Integrations`
   3. Select `Configure custom editor...` from the `External editor` dropdown
   4. Paste the path to your GitHub Desktop Smart IDE executable into the `Path` field (e.g. `..\GitHub-Desktop-Smart-IDE\dist\main.exe`)
   5. Ensure `Arguments` is set to `%TARGET_PATH%`
   6. Select the `Shell` of your choice from the dropdown
2. Configure your projects' default IDEs using JQB DevTools
   1. In your terminal of choice, navigate inside your project's root directory
   2. Run `jqb-dev-tools project init`
   3. Follow the prompts to select your preferred IDE for the project

## Use
### Opening a Repository in an IDE
1. Select any repository in GitHub Desktop
2. Use the `Open in external editor` button, `Repository > Open in external editor` menu item, or `Ctrl+Shift+A` to open the repository in the project's configured IDE

### Changing a Project's Preferred IDE
*Coming soon*
