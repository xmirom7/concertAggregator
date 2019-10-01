#!/usr/bin/env python3

import sys
try:
    del sys.modules['Database']
    del sys.modules['Bandsintown']
    del sys.modules['Songkick']
except KeyError:
    None

from importlib import import_module
import Database

def main():
    with Database.Database() as database:
        moduleNameAndClass = {}
        for moduleName in database.GetUsedModuleNames():
            ccc = getattr(import_module(moduleName), moduleName)
            moduleNameAndClass[moduleName] = ccc()

        for bandAndModuleAndArg in database.GetBandsModulesArgs():
            bandName = bandAndModuleAndArg[0]
            module = moduleNameAndClass[bandAndModuleAndArg[1]]
            moduleArg = bandAndModuleAndArg[2]
            for i in range(module.GetUpcomingEventsCount(moduleArg)):
                database.SaveEvent(bandName, module.GetCountryByIndex(i, moduleArg), module.GetCityByIndex(i, moduleArg), module.GetDateByIndex(i, moduleArg), module.GetClubNameByIndex(i, moduleArg), module.GetURLByIndex(i, moduleArg), module.GetInfoByIndex(i, moduleArg))
    print('Done')

if __name__=='__main__':
    main()
