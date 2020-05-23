from ..SimpleSymbolDownloader import SymbolDownloader
from ..symbols.Generic import Generic
import json
from ..compat import text

class GenericDownloader(SymbolDownloader):
    def __init__(self):
        SymbolDownloader.__init__(self, "generic")

    def decodeSymbolsContainer(self, json2):
        symbols = []
        count = 0
        for row in json2:
            ticker = text(json2[row])
            name = text(json2[row])
            exchange = text(json2[row])
            exchangeDisplay = text(json2[row])
            symbolType = text(json2[row])
            symbolTypeDisplay = text(json2[row])
            symbols.append(Generic(ticker, name, exchange, exchangeDisplay, symbolType, symbolTypeDisplay))

        count = len(json2)

        return (symbols, count)

    def getRowHeader(self):
        return SymbolDownloader.getRowHeader(self) + ["exchangeDisplay", "Type", "TypeDisplay"]

