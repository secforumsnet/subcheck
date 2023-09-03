<h1>Subdomain Checker</h1>

<p>This Python script is designed to check a list of subdomains for a specified domain and display subdomains with an HTTP status code of 200 in real-time in the terminal. It also provides information about the number of domains to be checked, progress during the check, and an estimated time to finish. The results are saved to a text file for later reference.</p>

<h2>Requirements</h2>

<p>Before running the script, you need to install the following Python libraries using pip:</p>

<ul>
  <li><b>requests:</b> This library is used to make HTTP requests to the subdomains and retrieve HTTP status codes.</li>
</ul>

<h3>Installation</h3>

<p>Install the required libraries using the commands provided above:</p>

<pre><code>pip install requests colorama tqdm</code></pre>

<h2>How to Run the Script</h2>

<ol>
  <li>Install the required libraries using the commands provided above.</li>
  <li>Save the Python script to a file, e.g., <code>subdomain_checker.py</code>.</li>
  <li>Prepare a text file (e.g., <code>subdomains.txt</code>) with a list of subdomains, one subdomain per line, to be checked.</li>
  <li>Open your terminal or command prompt.</li>
  <li>Navigate to the directory where the <code>subdomain_checker.py</code> script and <code>subdomains.txt</code> file are located.</li>
  <li>Run the script by executing the following command:</li>
</ol>

<pre><code>python subcheck.py</code></pre>

<p>Follow the on-screen prompts to enter the domain to be checked (e.g., example.com) and the path to the subdomains text file (e.g., subdomains.txt).</p>

<p>The script will start checking the subdomains and display subdomains with an HTTP status code of 200 in real-time in the terminal. It will also show the total number of domains to be checked, progress, and an estimated time to finish.</p>

<p>The results will be saved in a text file named <code>subdomain_check_results.txt</code> in the same directory for future reference.</p>

<p>This script is a helpful tool for identifying subdomains that return a successful HTTP status code (200) and can be used for various purposes like security assessments and domain management.</p>
