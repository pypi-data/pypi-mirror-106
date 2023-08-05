# Cut Finder

Meant to answer problems of the form "How shuold I cut boards a, b, and c and I need to cut them into final boards x,
y,z to minimize waste"


Basic use is meant to simply print the results:

    CutFinder(stocks=[100, 48], finals=[50,40, 36, 12, 12])
prints

    Unable to allocate final cuts: 12 
    Stock Board of length 48 is cut into final boards 40 with remainder 7.875 
    Stock Board of length 100 is cut into final boards 50, 36, 12 with remainder 1.625

However, you can find all the data in the actual CutFinder object if you want.