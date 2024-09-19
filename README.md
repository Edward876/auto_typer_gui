# auto_typer_gui
A Simple gui autotyper with necessary features. 

Here’s a Markdown-formatted instruction guide that macOS users can follow to convert the provided Python script into a `.pkg` installer file:


# For MacOS users - Convert Python Script to `.pkg` Installer on macOS

This guide will walk you through converting your Python script into a macOS `.pkg` installer. This process includes generating a standalone macOS application (`.app` file) from the Python script and then packaging it as a `.pkg` installer.

## Prerequisites

- **macOS**: You must be using macOS to follow these instructions.
- **Python**: Ensure Python is installed. You can check by running:
  ```bash
  python3 --version
  
- **PyInstaller**: Install PyInstaller using pip:
  ```bash
  pip install pyinstaller
  ```

## Step 1: Create the `.app` File

1. Save your Python script (e.g., `auto_typer.py`) to your desired directory.

2. Open the Terminal and navigate to the directory containing your Python script:
   ```bash
   cd /path/to/your/python/script
   ```

3. Run `PyInstaller` to create a standalone `.app` file:
   ```bash
   pyinstaller --onefile --windowed auto_typer.py
   ```

4. Once completed, the `.app` file will be located in the `dist` directory created by PyInstaller.

## Step 2: Create a `.pkg` Installer

To distribute the `.app` file, you can package it into a `.pkg` installer, which is the standard format for macOS installers.

1. Use the macOS `pkgbuild` tool to create the `.pkg` file:
   ```bash
   pkgbuild --root dist/auto_typer.app --identifier com.example.auto_typer --install-location /Applications auto_typer.pkg
   ```

   Here's what each option means:
   - `--root dist/auto_typer.app`: Path to the `.app` file.
   - `--identifier com.example.auto_typer`: A unique identifier for your application (replace with your app's name).
   - `--install-location /Applications`: The directory where the `.app` will be installed.
   - `auto_typer.pkg`: The name of the resulting `.pkg` installer.

2. After running this command, the `.pkg` file will be created in the current directory.

## Step 3: Test the `.pkg` Installer

1. Locate the `.pkg` file in Finder.
2. Double-click the `.pkg` file to run the installer.
3. Follow the installation steps, and the app should be installed in the `/Applications` folder.

## Step 4: (Optional) Code Signing and Notarization

If you plan to distribute the `.pkg` file online, it’s recommended to **code-sign** and **notarize** it to prevent macOS from flagging it as unsafe.

### Code Signing

1. You need an Apple Developer account to code sign your package.
2. Run the following command to sign your `.pkg` file:
   ```bash
   productsign --sign "Developer ID Installer: Your Name (Team ID)" auto_typer.pkg signed_auto_typer.pkg
   ```

### Notarization

1. Submit the signed `.pkg` file for notarization:
   ```bash
   xcrun altool --notarize-app --primary-bundle-id "com.example.auto_typer" --username "your_apple_id" --password "app-specific-password" --file signed_auto_typer.pkg
   ```

2. Once notarization is complete, you can distribute the `.pkg` file without macOS showing security warnings.

## Troubleshooting

- **Module Not Found Errors**: If PyInstaller doesn’t package certain Python modules, you may need to specify them using the `--hidden-import` option. For example:
  ```bash
  pyinstaller --onefile --windowed --hidden-import pyautogui auto_typer.py
  ```

## Conclusion

You now have a `.pkg` installer that macOS users can use to install your Python-based application in their `/Applications` directory. Optionally, sign and notarize the package for wider distribution.

```
