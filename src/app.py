
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model', type=str, default='/iexec_in', 
                        help="Folder containing model files")
    args = parser.parse_args()
    start_path = args.model
    print("looking for files in %s" % start_path)
    files = []
    for r, d, f in os.walk(start_path):
        for file in f:
            files.append(os.path.join(r, file))

    for f in files:
        print(f)

#with open("/iexec_in/dataset.txt", "r") as fin:
#   with open("/scone/result.txt", "w+") as fout:
#       data = fin.read()
#       fout.write(data)
#       print(data)
