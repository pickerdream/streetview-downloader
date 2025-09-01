import google_streetview.api as gs
import datetime
import openpyxl
from dotenv import load_dotenv
from art import *
import os
import argparse
import shutil
from tqdm import tqdm

# init
dt = datetime.datetime.today()
load_dotenv()
MAPS_API = os.environ["MAPS_API"]
parse = argparse.ArgumentParser()
heading_global = [0,90,180,270]
heading_name_global = ["north","east","south","west"]

# art
def program_display():
    tprint("Street Downloader")

# init only runs
def program_init():
    global EXCEL_PATH
    global OUTPUT_TYPE

    # read args
    parse.add_argument("--excel",dest="excel_path",required=True,help="座標を入力したExcelファイルを指定")
    parse.add_argument("--type",dest="file_output_type",choices=["0","1"],help="ファイルの出力方法",default="1") 
    args = parse.parse_args()

    # set args
    EXCEL_PATH = args.excel_path
    OUTPUT_TYPE = args.file_output_type

    # print
    print("Your API Key :" + MAPS_API)
    print("Excel File :" + EXCEL_PATH)
    print("OUTPUT TYPE :" + str(OUTPUT_TYPE))

# load file
def load():
    # load excel
    global EXCEL_LOCATION
    wb = openpyxl.load_workbook(EXCEL_PATH)
    ws = wb["Sheet1"]
    EXCEL_LOCATION = []
    for row in ws.iter_rows(min_row=2, min_col=1):
        for c in row:
            EXCEL_LOCATION.append(c.value)
    print(EXCEL_LOCATION)

# file set
def file_move():
    for LOCATION in EXCEL_LOCATION:
        global_path = "downloads/" + LOCATION
        for heading,heading_name in zip(heading_global,heading_name_global):
            heading_path = global_path + "/" + str(heading) + "/gsv_0.jpg"
            heading_path_meta = global_path + "/" + str(heading) + "/metadata.json"
            if OUTPUT_TYPE == "0":
                output_path = global_path + "/" + heading_name + ".jpg"
                output_path_meta = global_path + "/" + heading_name + ".json"
                print(f"moving {heading_path} to {output_path}")
            if OUTPUT_TYPE == "1":
                output_path = global_path + "-" + heading_name + ".jpg"    
                output_path_meta = global_path + "-" + heading_name + ".json"
            os.rename(heading_path,output_path)
            os.rename(heading_path_meta,output_path_meta)
        shutil.rmtree(global_path)

# main program
def main():
    for LOCATION in tqdm(EXCEL_LOCATION,desc="downloading files"):
        global_path = "downloads/" + LOCATION 

        for heading in heading_global:
            params = [{
                'size': '640x640',
                'location': LOCATION,
                'fov': '90',
                'heading': heading,
                'pitch': '0',
                'key': MAPS_API
            }]
            # create image
            image_result = gs.results(params)
            # generate download link
            download_path = global_path + "/" + str(heading)
            # download image
            image_result.download_links(download_path)
    file_move()
    print("Success!")
    
# start self programs
if __name__ == "__main__":
    program_display()
    program_init()
    load()
    main()