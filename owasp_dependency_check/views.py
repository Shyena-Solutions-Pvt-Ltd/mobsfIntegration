import os
import subprocess
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def run_dependency_check(request):
    # Define paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    owasp_dir = os.path.join(base_dir, 'owasp-dependency-check')
    report_dir = os.path.join(owasp_dir, 'reports')
    upload_dir = os.path.expanduser('~/.MobSF/uploads')
    script_path = os.path.join(owasp_dir, 'bin', 'dependency-check', 'bin', 'dependency-check.sh')
    report_file = os.path.join(report_dir, 'dependency-check-report.html')

    # Ensure the report directory exists
    os.makedirs(report_dir, exist_ok=True)

    # Run the OWASP Dependency-Check command
    command = [
        script_path,
        '--scan', upload_dir,
        '--out', report_dir,
        '--format', 'HTML'
    ]

    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Check if the report file exists
        if os.path.exists(report_file):
            with open(report_file, 'r') as file:
                return HttpResponse(file.read(), content_type='text/html')
        else:
            return HttpResponseNotFound("Report not found. Dependency-Check may have failed.")
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Error running Dependency-Check: {str(e)}\n{e.stderr}")
