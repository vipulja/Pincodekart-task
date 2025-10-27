To run this test script, follow these steps:

Environment: Use Python 3.7+ and install dependencies.

Dependencies: Install pytest and Playwright for Python:

Open the Command Prompt and run the commands below.
pip install pytest playwright
playwright install


(The playwright install command downloads browser binaries needed by Playwright.)

Running the Test: Save the above script as test_add_to_cart.py. Then execute:

Open the Command Prompt and run the commands below.
pytest test_add_to_cart.py


The script will open a Chromium browser window (headed mode), perform the test steps, and then close the browser automatically. You should see pytest report the test as passed if the assertions succeed.
