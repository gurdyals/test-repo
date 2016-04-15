rm(list = ls())

# This is for Fun.
# On April 14th, '2016 I was looking for data while taking Dr Chucks Python Course from Coursera
# and stumbled upon this India Govt site "data.gov.in"
# I found this Dataset "Trend_in_population_of_towns-Haryana.csv" at data.gov.in on April 14, '2016
# I decided to play around a bit using R for data Analysis
# Please take a look at the conclusion reached at the End of this script :)

#   This population numbers are in thousands ( '000 )

read.csv("Trend_in_population_of_towns-Haryana.csv")
HRY=read.csv("Trend_in_population_of_towns-Haryana.csv")
head(HRY)
tail(HRY)
names(HRY)
x=names(HRY)
x[2]="City.or.Town"
x[4]="2011"
x[5]="2001"
x[6]="1981"
x[7]="1971"
x[8]="1951"
x[9]="1901"
names(HRY)=x
HRY[!is.na(HRY["2001"])]
x2001 <- HRY[!is.na(HRY["2001"]),]
x2001
x1981 <- x2001[!is.na(x2001["1981"]),]
x1981
x1971 <- x1981[!is.na(x1981["1971"]),]
x1971
x1951 <- x1971[!is.na(x1971["1951"]),]
x1951
x1901 <- x1951[!is.na(x1951["1901"]),]
x1901
nrow(x2001)
x2011_1901 <- x1901["2011"] / x1901["1901"] * 100
x2011_1901
x1901["x2011_1901"] <- x2011_1901

x1901[order(x1901["x2011_1901"]), ]

x1901_sorted <- x1901[order(x1901["x2011_1901"]), ]
x1901_sorted
nrow(x1901_sorted[ x1901_sorted$Class == "Class-I", ])
x1901_sorted[ x1901_sorted$Class == "Class-I", ]

x1901_Class_I <- x1901_sorted[ x1901_sorted$Class == "Class-I", ]
x1901_Class_I

# Please take a look at column "x2011_1901" which is basically the percentage growth of population
# in this town from Year 1901 to 2011 as per census of that year
#    District Ambala   which had a huge population in 1901 as compared to other Cities/Districts
#    Ambala was the town with largest population in 1901 but it's population grew by 133% in this
#  110 years
#  On the other hand if we take a look at Gurgaon ( or Gurugram as of yesterday  )  and Faridabad
#  whose population was 4765 ( Gurugram ) and 9816 ( Fardabad ) in 1901
#   This population is in thousands ( '000 )
# It grew to 886519 for Gurgaon and 1414050 for Faridabad
# In percentage growth of population Gurgaon grew 18604 % 
#   and Faridabad grew 14405 %
#   in these 110 years


# These two districts of Haryana Gurgaon and Faridabad are in close proximity to New Delhi ( NCR )
# and these are the two districts which are highly industrialised in Haryana
# Other districts are nowhere near Gurgaon and Faridabad in industrialisation
# This explains the population growth in Gurgaon and Haryana
# Ambala used to be industrialised and a Important Military town half a century ago ( at independence )
# but slowly industries closed or moved out of Ambala for lack of Government Support
# thus almost negligible growth in population in last 110 years
# as youth moved to industrialised districts within Haryana or in other states in search of jobs/livelihood
# CONCLUSION
# Industrialisation attracts population towards it
# Thus it is important that Government Supports creation of Industry in each district