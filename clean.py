import os
import shutil


def main():
    result_root_dir = 'out_new'
    cnt = 0
    all_cnt = 0
    for sub_dir in os.listdir(result_root_dir):
        sub_dir = os.path.join(result_root_dir, sub_dir)
        if os.path.isdir(sub_dir):
            all_cnt += 1
            if len(os.listdir(sub_dir)) != 11:
                print(sub_dir)
                cnt += 1
                # shutil.rmtree(sub_dir)
    print(f'{cnt}/{all_cnt}')


if __name__ == '__main__':
    main()
