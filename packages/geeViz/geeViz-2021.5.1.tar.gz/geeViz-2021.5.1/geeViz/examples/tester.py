import os,sys
sys.path.append(os.getcwd())

#Module imports
from  geeViz.getImagesLib import *
Map.clearMap()

studyArea = testAreas['CA']

startJulian = 152
endJulian = 273

# Specify start and end years for all analyses
# More than a 3 year span should be provided for time series methods to work 
# well. If using Fmask as the cloud/cloud shadow masking method, or providing
# pre-computed stats for cloudScore and TDOM, this does not 
# matter
startYear = 2019
endYear = 2019

s2s = getProcessedSentinel2Scenes(studyArea,
  startYear,
endYear , startJulian,
  endJulian)
# s2s = s2s.map(addJulianDayBand)
# s2s = s2s.map(addYearJulianDayBand)
dates = ee.Dictionary(s2s.aggregate_histogram('date-orbit')).keys().getInfo()

print(dates)
# print(orb/its)

for date in dates[:3]:
	
	dateObj = ee.Date(ee.String(date).split('_').get(0))
	t = s2s.filterDate(dateObj,dateObj.advance(1,'day')).first()

	Map.addLayer(t,vizParamsFalse,date,False)
# s2s = s2s.map(addYearJulianDayBand)
# Map.addLayer(s2s.select(['julianDay','yearJulian']))
Map.view()
# print(s2s.size().getInfo())