#This file is a script that converts a csv file to html
#It takes a two string as command line argurments, the input filename and the output file name
import pandas as pd
import sys

def csv_to_html():
    input_file = sys.argv[1]
    output_file_name = sys.argv[2]
    df = pd.read_csv(input_file)
    html = df.to_html()
    output_file = open(output_file_name,"w")
    output_file.write(html)
    output_file.close()

if __name__ == "__main__":
    csv_to_html()
