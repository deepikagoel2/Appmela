FROM python:3.10

# Expose port you want your app on
EXPOSE 8501

RUN pip3 install streamlit

COPY home.py home.py


# Upgrade pip and install requirements
COPY requirements.txt ./requirements.txt
# RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run"]

CMD ["home.py --server.port=80 --server.enableCORS=false --server.enableWebsocketCompression=false --server.enableXsrfProtection=false"]

# WORKDIR .

# ENV ChocolateyUseWindowsCompression false 
# RUN powershell Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
# RUN powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
# RUN choco install git.install -y --no-progress

# RUN choco install vscode -y --no-progress



# # Upgrade pip and install requirements
# COPY requirements.txt ./requirements.txt
# # RUN pip install -U pip
# RUN pip install -r requirements.txt

# # Copy app code and set working directory
# # COPY text_explorer text_explorer 
# COPY app4.py app4.py
# # COPY references references

# # Run
# ENTRYPOINT ["streamlit", "run"]

# CMD ["app4.py"]
