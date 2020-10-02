import json
import os
import argparse





def main():
    parser = argparse.ArgumentParser(description='Process a json lines file')
    parser.add_argument("file_path", help="prints a json file number of lines",
                    type=str)
    args = parser.parse_args()

    if os.path.exists(args.file_path):
        article_file = open(args.file_path, 'r')
        articles = []
        for line in article_file:
            articles.append(json.loads(line))
        article_file.close()

    print('Number of articles is:', len(articles))
                
        



if __name__ == "__main__":
    # execute only if run as a script
    main()