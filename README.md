# Check gitlab version

This tool were created for checking gitlab version of multiple server by comparing the hash from manifest.json with provided list.

## Installation
```
git clone https://github.com/dt022/check-gitlab-version
cd check-gitlab-version
python3 check-gitlab-version.py -u example.com
```

## Usage
```
python3 check-gitlab-version.py -u example.com
python3 check-gitlab-version.py -f file.txt
python3 check-gitlab-version.py -t update
```
## Screenshot
![image](image/image1.png)

## References
https://github.com/righel/gitlab-version-nse
