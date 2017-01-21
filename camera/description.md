# Raspberry-pi camera with Vision API on python
  
1. camera module 설정
 - ''/boot/config.txt'' 에서 ''start_x=1''로 수정하고 재부팅
  
2. pi-cam_with_visionAPI.py 설명
 - 소스 코드 내에 pic 변수에 저장될 위치와 파일명으로 저장한다.
   
3. 실행
 - ''$ python  pi-cam_with_visionAPI.py  /directory/of/image.jpg'' 처럼 위치와 파일명을 명세하면 해당 파라미터로 저장되며 파라미터 없이 실행하면 소소코드 내에 저장된 default위치와 파일명으로 저장된다.
