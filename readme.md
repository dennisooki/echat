How 2 run
1. Clone the repository using the following command:
```
git clone https://github.com/dennisooki/echat
```

2. Starting the server:
   - Change your current directory to `echat/chatserver/`.
   ```
   cd echat/echat/chatserver/
   ```
   - Start the server by running the following command:
   ```
   python server.py
   ```

3. Starting a client:
   - Open a new terminal and change your directory to the cloned repository(this is the top level directory, not the one that holds the application code).
   ```
   cd echat
   ```
   - Run the following command to start a client:
   ```
   python -m echat.gui.splash
   ```
   - Repeat this step for each additional client you need.

4. Closing the client properly:
   - Use the exit button in the GUI to close the client.

5. Closing the server properly:
   - Ensure that all clients have exited.
   - Press `Ctrl+C` in the server terminal to close the server.


If you run into problems try looking for the pycache folders and deleting them, ik one is in echat/gui but there may be more just check.
Please note that these instructions assume you have Git and Python installed on your system.