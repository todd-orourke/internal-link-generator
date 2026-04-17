# 🔗 Internal Link Suggester (Gemini AI)

This script analyzes a live webpage, compares it against your website's sitemap, and uses AI to suggest the best places to add internal links to improve SEO.

### **Step 1: Get Your Sitemap URLs**
The script needs a list of all pages on your website so it knows where it can suggest links to.

1.  Go to your website's sitemap (usually `yourwebsite.com/sitemap.xml`).
2.  Copy the list of page slugs (the part of the URL after the `.com`).
3.  Open `internal_linker.py` in your text editor.
4.  Find the `sitemap_urls = [` section and paste your URLs inside the brackets, ensuring each one is in "quotes" and followed by a comma.

### **Step 2: Set the Target Page**
1.  In the same script, look for the line: `target_page_url = "..."`.
2.  Replace the URL with the full link to the specific blog post or page you want to analyze.

### **Step 3: Add Your Gemini API Key**
1.  You must have a Google Gemini API Key.
2.  If you do not have an API key, get one from here: https://aistudio.google.com/api-keys
3.  Find the line `API_KEY = ''` at the top of the script.
4.  Paste your key between the single quotes: `API_KEY = 'your_key_here'`.

### **Step 4: Run the Analysis**
1.  Open your **Terminal** or **Command Prompt**.
2.  Navigate to the folder and run:
    ```bash
    python internal_linker.py
    ```
3.  **Wait:** The script will fetch the live HTML of your page and send it to the AI.
4.  **Review:** A Markdown table will appear in your terminal showing:
    * **Suggested Anchor Text:** The phrase on your page the AI thinks should be a link.
    * **Suggested Destination URL:** The most relevant page from your sitemap to link to.

---

### **How the "AI Logic" Works**
The script doesn't just look for keyword matches. It reads the **context** of your sentences. For example, if your page mentions "managing customer expectations," the AI will scan your sitemap for articles about "Customer Experience" or "Consumer Trends" and suggest a link that feels natural to a human reader.

---

### **Pro-Tip for Coworkers**
* **Check existing links:** The script is designed to ignore links that are already live on the page, so it will only show you *new* opportunities.
