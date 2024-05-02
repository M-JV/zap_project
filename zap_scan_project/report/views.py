from django.shortcuts import render
from embedchain import App
import langchain_community
import langchain
import os
import markdown

# Initialize the App object from the embedchain library
app = None

# Set up your configuration for the App object
config = {
  'llm': {
    'provider': 'google',
    'config': {
      'model': 'gemini-1.5-pro-latest',
      'top_p': 0.5,
      'temperature': 0.64
    }
  },
  'embedder': {
    'provider': 'google',
    'config': {
      'model': 'models/embedding-001',
      'task_type': 'retrieval_document'
    }
  }
}
os.environ["GOOGLE_API_KEY"] = "AIzaSyA5TNy9L5i56_PG3hTgQYz5rN99rYHZiBc"

def initialize_app():
    global app
    # Initialize the App object with the configuration
    app = App.from_config(config=config)

def generate_report():
    try:
        # Initialize App object and execute query
        # Assuming the CSV file is located at the specified path
        app.add('/home/mejova/zap_project/zap_scan_project/csv_output/scan_results.csv', data_type='csv')
        app.add('https://owasp.org/Top10/A01_2021-Broken_Access_Control/', data_type='web_page')
        app.add('https://owasp.org/Top10/A02_2021-Cryptographic_Failures/', data_type='web_page')
        app.add('https://owasp.org/Top10/A03_2021-Injection/', data_type='web_page')
        app.add('https://owasp.org/Top10/A04_2021-Insecure_Design/', data_type='web_page')
        app.add('https://owasp.org/Top10/A05_2021-Security_Misconfiguration/', data_type='web_page')
        app.add('https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/', data_type='web_page')
        app.add('https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/', data_type='web_page')
        app.add('https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/', data_type='web_page')
        app.add('https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/', data_type='web_page')
        app.add('https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/', data_type='web_page')
        
        # Execute the query using the appropriate method/function provided by the library
        result = app.query("""
                  
                SURFSHELID AI Based Report:
                  
                -   Website security evaluation:
                   [Evaluate the overall security of the website based on the findings and measures taken.
                   Safe or Not Safe: Print whether the website is considered safe or not based on the assessment]
                          
                 -  Scan Report:
                    [Include findings and insights from the Zap Scan Report data and Adding these webite is safe or not]

                - OWASP Top 10:
                    [Include insights and analysis related to the selected OWASP Top 10 vulnerabilities and list it.]

                - Prevention and Mitigation Strategies:
                    [Provide actionable recommendations and strategies to prevent and mitigate the identified vulnerabilities. 
                    Include best practices, security controls, and guidelines.]

                [Add any additional analysis or insights as needed.]
                      
        """)

        # Strip Markdown syntax from the result
        html_content = markdown.markdown(result)
        other_data = ""

        # Pass the result to the template for rendering
        context = {'html_content': html_content, 'other_data': other_data}
        return context
    except Exception as e:
        raise e

def results(request):
    global app
    try:
        if app is None:
            initialize_app()

        # Generate the report
        context = generate_report()

        return render(request, 'report/report.html', context)
    except Exception as e:
        return render(request, 'report/error.html', {'error': str(e)})
