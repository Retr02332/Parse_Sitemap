from lxml import etree as ET
from lxml.etree import XMLParser, parse
import sys

parsedHosts = []

def add2ParsedHosts(protocol: str, host: str, port: str, path: str):
    url = f"{protocol}://{host}:{port}{path}\n"
    parsedHosts.append(url) if (url not in parsedHosts) else ""

def parseData(items: list) -> list:
    for item in items:
        protocol = item[4].text
        host     = item[2].text
        port     = item[3].text
        path     = item[6].text.split("?")[0]
        add2ParsedHosts(protocol, host, port, path)

    return parsedHosts

def saveParsedHosts(parsedHosts: list, outputFile: str):
    with open(f"{outputFile}", "w") as fileParsedHosts:
        fileParsedHosts.writelines(parsedHosts)

def main():
    targetFile = sys.argv[1]
    outputFile = sys.argv[2]

    parser = XMLParser(huge_tree=True)
    tree   = parse(targetFile, parser=parser)
    items   = tree.getroot()

    saveParsedHosts(parseData(items), outputFile)

main()