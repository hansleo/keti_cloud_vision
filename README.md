# keti_cloud_vision

* 파이썬으로 Google Cloud Vision API / text 사용하기

1. API 설치:
<pre><code>git clone https://github.com/GoogleCloudPlatform/cloud-vision.git</code></pre>

2. 필요 라이브러리 설치 :
설치된 cloud-vision/python/ 내에 필요한 기능 폴더의 requirements.txt를 사용
<pre><code>sudo pip install -r cloud-vision/python/text/requirements.txt</code></pre>

3. nltk 설치 및 필요 nltk 자료 다운:
<pre><code>python -m nltk.downloader stopwords
python -m nltk.downloader punkt</code></pre>


4. 환경변수설정:
google cloud vision API에서 받을 수 있는 json 파일의 서비스 키 파일로 설정.
</pre><code>export GOOGLE_APPLICATION_CREDENTIALS=cloude-vision/*.json</code></pre>
