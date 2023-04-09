speech = """ 
Data science is the domain of study that deals with vast volumes of data using modern tools and techniques to find unseen patterns, derive meaningful information, and make business decisions. Data science uses complex machine learning algorithms to build predictive models.

The data used for analysis can come from many different sources and presented in various formats.

Now that you know what data science is, let’s see why data science is essential to today’s IT landscape.

Post Graduate Program In Data Science
The Ultimate Ticket To Top Data Science Job RolesEXPLORE COURSEPost Graduate Program In Data Science
The Data Science Lifecycle
Now that you know what is data science, next up let us focus on the data science lifecycle. Data science’s lifecycle consists of five distinct stages, each with its own tasks:

Capture: Data Acquisition, Data Entry, Signal Reception, Data Extraction. This stage involves gathering raw structured and unstructured data.
Maintain: Data Warehousing, Data Cleansing, Data Staging, Data Processing, Data Architecture. This stage covers taking the raw data and putting it in a form that can be used.
Process: Data Mining, Clustering/Classification, Data Modeling, Data Summarization. Data scientists take the prepared data and examine its patterns, ranges, and biases to determine how useful it will be in predictive analysis.
Analyze: Exploratory/Confirmatory, Predictive Analysis, Regression, Text Mining, Qualitative Analysis. Here is the real meat of the lifecycle. This stage involves performing the various analyses on the data.
Communicate: Data Reporting, Data Visualization, Business Intelligence, Decision Making. In this final step, analysts prepare the analyses in easily readable forms such as charts, graphs, and reports.

"""
model_name = "Madi Collins"
# modifying name to use in the link an name  #
modelnameinlink = model_name.lower().replace(' ','-')
modelnameforscrap = model_name.title()
#############################################
#############################################
start_urls = [("https://sexhd.pics/gallery/"+ modelnameforscrap +"/" +str(n)+"/") for n in range(1,11)]
# print(start_urls)

# print(wordsfilter(speech))
# print([[wordsfilter(x) for x in sentence.split()] for sentence in speech.split('\n')] )





# wordscount = {}

# for x in speech.split():
#     if x in wordscount:
#         wordscount[x] += 1
#     else:
#         wordscount[x] = 1

# print("\n\n\n" , wordscount , "\n\n")
# mostwordcount = int(0)

# for x in wordscount:
#     if(wordscount[x] > mostwordcount):
#         mostwordcount = wordscount[x]
#         mostword = x
#         print(mostword , mostwordcount)


