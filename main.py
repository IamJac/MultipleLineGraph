from matplotlib import pyplot as plt
#X-axis values
x_values=(2010,2011,2012,2013,2014,2015,2016,2017,2018)
#Trend of programmers using python
y_values=(200,280,350,500,900,780,950,1250,4500)
#Trend of programmers using c++
y_values1=(5500,2100,3100,2790,1230,780,960,670,450)
#Trend of programmers using Java
y_values2=(600,380,350,550,900,700,1220,1250,2500)
#Trend of programmers using C#
y_values3=(150,250,300,450,800,750,950,2250,3500)
#Trend of programmers using Javascript
y_values4=(150,290,380,750,950,1200,990,3400,4000)
#Trend of programmers using
plt.style.use("ggplot")#Set a preferred style the graph appearance
plt.plot(x_values,y_values,color="b",linestyle="-",marker="o",label="Python")
plt.plot(x_values,y_values1,color="r",linestyle="-",marker="o",label="C++")
plt.plot(x_values,y_values2,color="g",linestyle="--",marker="o",label="Java")
plt.plot(x_values,y_values3,color="y",linestyle="-",marker="o",label="C#")
plt.plot(x_values,y_values4,color="b",linestyle="-.",marker="o",label="Javascript")
plt.legend()#To label each line for easy identification
plt.xlabel("YEARS")
plt.ylabel("NUMBER OF PROGRAMMERS IN 000's USING A LANGUAGE")
plt.title("LINE GRAPH SHOWING TREND OF USAGE OF PROGRAMMING LANGUAGES  FOR THE PERIOD BETWEEN 2010 AND 2018")
plt.plot()#Plot the graphs
plt.show()#Display the graph