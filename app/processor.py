from pyresparser import ResumeParser

def process(filePath):
        return ResumeParser(filePath).get_extracted_data()