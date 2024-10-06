import os
import shutil
import re

def isExistDirectory(current_dir):
    return os.path.isdir(current_dir)

def build_path(dir: str, *sub_dirs):
    """
    Parameters:
    *subdirs (str): 홈 디렉토리 이후의 하위 디렉토리 경로 요소들.

    Returns:
    str: 생성된 경로.
    """
    return os.path.join(dir, *sub_dirs)

def copy_directory(src: str, dst: str):
    """
    디렉토리와 그 하위 파일 및 폴더를 복사하는 함수.

    Parameters:
    src (str): 소스 디렉토리 경로.
    dst (str): 대상 디렉토리 경로.
    """
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

def find_versioned_directory(path):
    """
    지정된 경로에서 숫자.숫자.숫자 형식의 디렉토리를 찾습니다.

    Parameters:
    path (str): 검색할 디렉토리 경로.

    Returns:
    str: 버전 형식의 디렉토리 이름. 없으면 None.
    """
    version_pattern = re.compile(r'^\d+\.\d+\.\d+\.\d+$')
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)) and version_pattern.match(item):
            return item
    return None


def load_chrome_from_installed():
    if isExistDirectory(chrome_application_dir):
        print(f"{chrome_application_dir}에서 Chrome을 가져옵니다...")
        copy_directory(chrome_application_dir, application_dir)

    else:
        print(f"{chrome_application_dir}에 Chrome이 설치되어 있지 않습니다.")


if __name__ == '__main__':
    current_dir = os.getcwd()
    application_dir = build_path(current_dir, 'Application')

    home_dir = build_path(os.path.expanduser("~"), 'AppData', 'Local', 'Google', 'Chrome')
    chrome_application_dir = build_path(home_dir, 'Application')

    print('Easy Portable Chrome v1.0')

    # Chrome이 설치되지 않은 경우 경고 메시지를 출력하고 종료합니다.
    if isExistDirectory(home_dir) == False:
        print(f'[경고] 크롬이 설치되지 않았습니다!!')
        print('프로그램을 종료합니다.')
        print()
        os.system('pause')
        exit()

    # C:\Windows\system32 or C:\Windows\SysWOW64로 현재 경로가 잡혀있는 경우는 실행되지 않습니다
    if current_dir == build_path(os.environ['SystemRoot'], 'system32') and build_path(os.environ['SystemRoot'], 'SysWOW64'):
        print(f'[경고] 현재 폴더는 {current_dir} 시스템 폴더에서 실행되었습니다!!')
        print('프로그램을 종료합니다.')
        print()
        os.system('pause')
        exit()

    # 크롬이 설치된 폴더에서 실행되었을 경우 경고 메시지를 출력하고 종료합니다.
    if current_dir == home_dir:
        print(f'[경고] 현재 폴더는 {current_dir} 크롬이 설치된 폴더에서 실행되었습니다!!')
        print('프로그램을 종료합니다.')
        print()
        os.system('pause')
        exit()


    if isExistDirectory(application_dir) == False:
        print(f'현재 폴더 {current_dir}에 Application 폴더가 존재하지 않습니다.')
        print(f"Installed Chrome 버전 : {find_versioned_directory(chrome_application_dir)}")

        print('설치된 크롬을 현재 폴더로 가져오겠습니까? [y/n]', end=' :')
        answer = input()

        if answer == 'y':
            print('설치된 크롬을 현재 폴더로 가져옵니다.')
            load_chrome_from_installed()
        else:
            pass

    else:
        print(f'현재 폴더 {current_dir}에 Application 폴더가 존재합니다.')
        print('버전을 확인합니다.')
        print(f"Installed Chrome 버전 : {find_versioned_directory(chrome_application_dir)}")
        print(f"Portable  Chrome 버전 : {find_versioned_directory(application_dir)}")

        print('설치된 크롬을 Portable Chrome에 가져오겠습니까? [y/n]', end=' :')
        answer = input()

        if answer == 'y':
            print('설치된 크롬을 현재 폴더로 가져옵니다.')
            load_chrome_from_installed()
        else:
            pass
            
