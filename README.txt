# J.A.R.V.I.S. Web + Mobile Version

This is a web version of the working Tkinter J.A.R.V.I.S.

## 1. Install

From this folder:

    python -m pip install -r requirements.txt

If `python` is not recognized on your PC, use your working Python executable, for example:

    "C:\Users\ayan\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m pip install -r requirements.txt

## 2. Set the API key

Do NOT put the API key inside `index.html` or JavaScript.

In Windows Command Prompt, for the current terminal session:

    set OPENAI_API_KEY=YOUR_KEY_HERE

Optional model:

    set JARVIS_MODEL=gpt-6-luna

## 3. Start J.A.R.V.I.S.

    python app.py

Or, with the direct Python path:

    "C:\Users\ayan\AppData\Local\Python\pythoncore-3.14-64\python.exe" app.py

Open on the PC:

    http://127.0.0.1:5000

## 4. Use it on your phone on the same Wi-Fi

The server listens on all network interfaces.

On Windows, run:

    ipconfig

Find the PC's IPv4 Address, for example `192.168.1.5`.

On the phone, open:

    http://192.168.1.5:5000

Both devices must be on the same Wi-Fi.

If Windows Firewall asks whether Python should be allowed on a private network, allow it for your private/home network.

## 5. WhatsApp sharing

A local `192.168.x.x` address normally only works on your local network. To share J.A.R.V.I.S. with someone outside your Wi-Fi, the web app needs to be deployed to an internet-accessible server.

Important: the OpenAI API key must stay on the server. Never put it in the browser code or send it in WhatsApp.
