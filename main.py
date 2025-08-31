import google_streetview.api as gs
import datetime
import openpyxl
from dotenv import load_dotenv
from art import *
import os

# init
dt = datetime.datetime.today()
load_dotenv()
MAPS_API = os.environ["MAPS_API"]

# art
def program_display():
    tprint("Street Downloader")

# init only runs
def program_init():
    global EXCEL_PATH
    print("Your API Key :" + MAPS_API)
    EXCEL_PATH = input("Enter your xlsx file name:")    

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

# main program
def main():
    for LOCATION in EXCEL_LOCATION:
        global_path = "downloads/" + LOCATION 
        heading = [0,90,180,270]

        for heading in heading:
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

if __name__ == "__main__":
    program_display()
    program_init()
    load()
    main()