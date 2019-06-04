# Program to read the following json content and output the arn of the s3 bucket

import json

def main():

    #Reading JSON File from SampleJson.text file into inputJsonObject
    with open('SampleJson.txt') as json_file:
        inputJsonObject = json.load(json_file)

    #Fetching the required value of arn and printing it
    print(inputJsonObject["Records"][0]["s3"]["bucket"]["arn"])


if __name__ == "__main__":
    main()

