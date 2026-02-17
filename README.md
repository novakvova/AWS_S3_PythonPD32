# MY AWS Keys
```
Access key
AKIAXKAAQWVA44ZYA6TS
Secret access key
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
```

# Install CLI AWS
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

aws --version
aws configure

AWS Access Key ID:     <твій access key>
AWS Secret Access Key:<твій secret>
Default region name:  eu-central-1
Default output format: json

aws s3 ls

python3 --version
apt install python3-pip
pip3 --version
pip --version

venv - вірутальне середовище 
Для установки усіх пакетів python для вашого проекту
Для того, щоб пакети були ізольовані і у venv - для певної версії python

py -m venv .venv
#python3 -m venv .venv

.venv\Scripts\activate.bat
#source .venv/bin/activate

python.exe -m pip install --upgrade pip

pip3 install "boto3[crt]"
pip install "boto3[crt]"

pip freeze > requirements.txt
pip3 freeze > requirements.txt

python main.py
python3 main.py
```

# Clone and run project
```
git clone https://github.com/novakvova/AWS_S3_PythonPD32.git
cd AWS_S3_PythonPD32
apt install python3.12-venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 main.py
```

