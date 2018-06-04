from django.shortcuts import render
from django.http import HttpResponse
from . models import UniversityCurriculum, jobData
from . Our_algorithm import preProcess_Func
from . KMP import KMPSearch
from . BM import BMsearch

def course_data(request):
    return render(request, 'education_gap_analyzer/course_content_form.html')


  # selectUni pag
    # Text : University , Pattern : Job content
    # Searching Algorithm BFM
    #our.py calling


def comparison(request):

    txt = ""
    pattern = ""
    if 't' in request.session:
        txt = request.session['t']
    if 'p' in request.session:
        pattern = request.session['p']

    title1 = ""
    title2 = ""
    title3 = ""
    title4 = ""
    title5 = ""
    title6 = ""

    # For BMF

    totalPreprocessingTimeOur = 0
    totalSearchingTimeOur = 0
    totalShiftOur = 0
    totalCharacterComparisonOur = 0

    matchCountOur = 0
    unmatchCountOur = 0


    for pat in pattern:
        if len(pat) != 1:
            isMatch = False
            charComparison, shift, preProcessTime, searchTime , isMatch = preProcess_Func(txt, pat)
            totalCharacterComparisonOur += charComparison
            totalShiftOur += shift
            totalPreprocessingTimeOur += preProcessTime
            totalSearchingTimeOur += searchTime
            if isMatch == True :
                matchCountOur += 1
            else :
                unmatchCountOur += 1


    totalPreprocessingTimeBM = 0
    totalSearchingTimeBM = 0
    totalShiftBM = 0
    totalCharacterComparisonBM = 0

    matchCountBM = 0
    unmatchCountBM = 0
    charComparison = 0
    shift = 0
    preProcessTime = 0
    searchTime = 0

    for pat in pattern:
        if len(pat) != 1:

            isMatch = False
            charComparison, shift, preProcessTime, searchTime , isMatch = BMsearch(txt, pat)
            totalCharacterComparisonBM += charComparison
            totalShiftBM += shift
            totalPreprocessingTimeBM += preProcessTime
            totalSearchingTimeBM += searchTime
            if isMatch == True :
                matchCountBM += 1
            else :
                unmatchCountBM += 1

    # For KMP
    totalPreprocessingTimeKMP = 0
    totalSearchingTimeKMP = 0
    totalShiftKMP = 0
    totalCharacterComparisonKMP = 0

    matchCountKMP = 0
    unmatchCountKMP = 0
    charComparison = 0
    shift = 0
    preProcessTime = 0
    searchTime = 0

    for pat in pattern:
        if len(pat) != 1:
            isMatch = False
            charComparison, shift, preProcessTime, searchTime , isMatch = KMPSearch(txt, pat)
            totalCharacterComparisonKMP += charComparison
            totalShiftKMP += shift
            totalPreprocessingTimeKMP += preProcessTime
            totalSearchingTimeKMP += searchTime
            if isMatch == True :
                matchCountKMP += 1
            else :
                unmatchCountKMP += 1


    contextComparsion = {          'matchCountOur' : matchCountOur,
                                   'unmatchCountOur': unmatchCountOur,
                                   'searchTimeOur': "%.5f" % totalSearchingTimeOur ,
                                   'preprocessTimeOur':"%.5f" % totalPreprocessingTimeOur,
                                   'shiftComparisonOur': totalShiftOur,
                                   'charComparisonOur' : totalCharacterComparisonOur,
                                   # BM
                                   'matchCountBM': matchCountBM,
                                   'unmatchCountBM': unmatchCountBM,
                                   'searchTimeBM': "%.5f" % totalSearchingTimeBM,
                                   'preprocessTimeBM': "%.5f" % totalPreprocessingTimeBM,
                                   'shiftComparisonBM': totalShiftBM,
                                   'charComparisonBM': totalCharacterComparisonBM,
                                   #KMP
                                   'matchCountKMP': matchCountKMP,
                                   'unmatchCountKMP': unmatchCountKMP,
                                   'searchTimeKMP': "%.5f" % totalSearchingTimeKMP,
                                   'preprocessTimeKMP': "%.5f" % totalPreprocessingTimeKMP,
                                   'shiftComparisonKMP': totalShiftKMP,
                                   'charComparisonKMP': totalCharacterComparisonKMP,

                                    'pattern' : pattern ,
                                    'txt' : txt ,
                                    'title1': title1,
                                    'title2': title2,
                                    'title3': title3,
                                    'title4': title4,
                                    'title5': title5,
                                    'title6': title6
                                }

    return render(request, 'education_gap_analyzer/comparison.html' , contextComparsion)


def extractedKeywordJob(request):

    jCategory = request.POST.get('job')

    itTelecommunication = False
    accountingFinance = False
    engineerArchitect = False
    medicalPharma = False
    marketingSales = False

    if jCategory == "IT&Telecommunication":
        itTelecommunication = True
    elif jCategory == "AccountingFinance":
        accountingFinance = True
    elif jCategory == "EngineerArchitect":
        engineerArchitect = True
    elif jCategory == "MedicalPharma":
        medicalPharma = True
    elif jCategory == "MarketingSales":
        marketingSales = True

    keys = jobData.objects.filter(category=jCategory)

    keywordsSet = set()
    keywordList = []
    relatedDeptSet = set()
    relatedDeptList =[]

    for data in keys:
        keywordList = data.keywords.split()
        for data2 in keywordList:
            if data2 != 'age' :
                keywordsSet.add(data2)
        relatedDeptList = data.relatedDept.split(",")
        for data3 in relatedDeptList:
            relatedDeptSet.add(data3)

    title1 = "Related Department : "
    title2 = "Extracted Keyword: "
    title3 = "Selected Category : "

    context= {'relatedDeptSet' : list(relatedDeptSet),
             'keywordsSet' : keywordsSet,
             'category' : jCategory,
             'it' : itTelecommunication,
             'accounting': accountingFinance,
             'engineerArchitect' : engineerArchitect,
             'medicalPharma' : medicalPharma,
             'marketingSales': marketingSales,
             'title1' : title1 ,
             'title2' : title2 ,
             'title3' : title3
             }
    return render(request,'education_gap_analyzer/selJobCategory.html', context)


def extractedKeywordUniversity(request):

    univ = request.POST.get('uni')
    dept = request.POST.get('dep')
    categ = request.POST.get('job')

    request.session['university'] = univ
    request.session['department'] = dept
    request.session['category'] = categ

    keys1 = UniversityCurriculum.objects.filter(universityName__icontains=univ).filter(deptName__icontains=dept)
    keys2 = jobData.objects.filter(category__icontains=categ)

    keywordList1 = []
    keywordList2 = []

    keywordSet1 = set()
    keywordSet2 = set()
    for data in keys1: # For University
        keywordList1 = data.courseKeyword.split()
        for item in keywordList1:
            keywordSet1.add(item)

    for data in keys2:  # For Job
        keywordList = data.keywords.split()
        for data2 in keywordList:
            if data2 != 'age' :
                keywordSet2.add(data2)


    title1 = "Extracted Keyword University : "
    title2 = "Extracted Keyword Job : "
    title3 = "Category : "
    title4 = "University Name : "
    title5 = "Department Name : "
    title6 = "Job Category : "

    contextUni= { 'keywordSet1' : list(keywordSet1) ,
                  'keywordSet2': list(keywordSet2) ,
                  'univ' : univ ,
                  'dept' : dept ,
                  'categ' : categ ,
                  'title1': title1 ,
                  'title2': title2 ,
                  'title3': title3 ,
                  'title4': title4 ,
                  'title5': title5 ,
                  'title6': title6
                  }
    return render(request, 'education_gap_analyzer/selectUni.html', contextUni)

def index(request):
    return render(request , 'education_gap_analyzer/index.html')

def insert_data(request):
    data = request.POST

    jobTitle = data['jTitle']
    category = data['catag']
    jobRequirments = data['jReq']
    relatedDept = data['RelatedDept']

    jobReqTxt = data['jReq']
    import nltk
    from nltk import word_tokenize

    import os

    java_path = "C:/Program Files/Java/jdk1.8.0_60/bin/java.exe"
    os.environ['JAVA_HOME'] = java_path

    nltk.internals.config_java('C:/Program Files/Java/jdk1.8.0_60/bin/java.exe')

    from nltk.tag import StanfordPOSTagger

    jar = 'C:/Users/Obaidullah Al-Faruk/PycharmProjects/new/stanford-postagger-2016-10-31/stanford-postagger.jar'
    model = 'C:/Users/Obaidullah Al-Faruk/PycharmProjects/new/stanford-postagger-2016-10-31/models/english-left3words-distsim.tagger'
    pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

    tokens = word_tokenize(jobReqTxt)
    tagged = pos_tagger.tag(tokens)
    nouns = [word for word, pos in tagged \
             if (pos == 'NNP')]
    downcased = [x.lower() for x in nouns]
    key1 = ' '.join(str(e) for e in downcased)

    JobData = jobData(jobTitle=jobTitle, category=category,jobRequirments=jobRequirments, relatedDept=relatedDept, keywords= key1 )
    JobData.save()

    return render(request, 'education_gap_analyzer/jobDataForm.html')



def insert_course_data(request):
    courseData = request.POST

    universityName = courseData['UniName']
    deptName = courseData['DeptName']
    courseName = courseData['courseName']
    courseContent = courseData['courseContent']

    try:
        import nltk
        tokens = nltk.word_tokenize(courseContent)
        tagged = nltk.pos_tag(tokens)
        nouns = [word for word, pos in tagged \
                 if (pos == 'NNP' or pos == 'NNPS')]
        downcased = [x.lower() for x in nouns]

        key1 = ' '.join(str(e) for e in downcased) #String Convert

    except:
        print("Noun Extraction Problem. ")

    universityCurriculum = UniversityCurriculum(universityName=universityName,deptName =deptName,courseName=courseName,courseContent=courseContent, courseKeyword=key1 )
    universityCurriculum.save()

    return render(request, 'education_gap_analyzer/course_content_form.html')


def job_data(request):
    return render(request, 'education_gap_analyzer/JobDataForm.html')


def jobCategory_Select(request):
    return render(request, 'education_gap_analyzer/selJobCategory.html')


def similarity(request):

    value = request.GET.get('q','')
    value2 = value.split("-")

    if 'category' in request.session:
        jobCategory = request.session['category']
    else:
        jobCategory1 = value2[0]
        jobCategory = request.session['jobCategory1']
    if 'university' in request.session:
        uniName = request.session['university']
    else:
        uniName1= value2[1]
        uniName = request.session['uniName1']
    if 'department' in request.session:
        depName = request.session['department']
    else:
        depName1 = value2[2]
        depName = request.session['depName1']


    keys1 = UniversityCurriculum.objects.filter(universityName__icontains=uniName).filter(deptName__icontains=depName)
    keys2 = jobData.objects.filter(category__icontains=jobCategory)

    keywordList1 = []
    keywordList2 = []

    keywordSet1 = set()
    keywordSet2 = set()
    for data in keys1: # For University
        keywordList1 = data.courseKeyword.split()
        for item in keywordList1:
            keywordSet1.add(item)

    for data in keys2:  # For Job
        keywordList = data.keywords.split()
        for data2 in keywordList:
            if data2 != 'age' :
                keywordSet2.add(data2)

    keywordSet1 = list (keywordSet1)
    keywordSet2 = list (keywordSet2)

    #keywordSet2 =list (keywordSet2)
    # Text : University , Pattern : Job content
    # Searching Algorithm BFM
    #our.py calling

    matchedList = []  # for matched key adding
    unmatchedList = [] # for unmatched key adding
    #Text split()
    #txt= ','.join(str(s) for s in keywordSet1)
    txt = ""
    for s in keywordSet1:
        txt+=s+" ";
    patt = ""
    for s in keywordSet2:
        patt+=s+" ";

    totalPreprocessingTime = 0
    totalSearchingTime = 0
    totalShift = 0
    totalCharacterComparison = 0

    pattern = patt.split()
    if 't' in request.session:
        del request.session['t']
    if 'p' in request.session:
        del request.session['p']

    request.session['t']= txt
    request.session['p']= pattern

    for pat in pattern:
        if len(pat)!= 1:
            isMatch = False
            charComparison, shift, preProcessTime, searchTime , isMatch = preProcess_Func(txt, pat)
            totalCharacterComparison += charComparison
            totalShift += shift
            totalPreprocessingTime += preProcessTime
            totalSearchingTime += searchTime
            if isMatch == True :
                matchedList.append(pat)
            else :
                unmatchedList.append(pat)


    title1 = "Matched Keywords "
    title2 = "You May Consider Following Keywords For Your Syllabus "


    contextUniForSimilarityPage = { 'matchedKey' : matchedList,
                                   'unmatchedKey' : unmatchedList,
                                   'searchTime' : totalSearchingTime ,
                                   'preprocessTime' :totalPreprocessingTime,
                                   'shiftComparison' : totalShift,
                                   'charComparison'  : totalCharacterComparison,
                                    'pattern' : pattern ,
                                    'txt' : txt ,
                                    'title1' : title1,
                                    'title2' : title2
                                }

    return render(request, 'education_gap_analyzer/similarity.html',contextUniForSimilarityPage)



def showUni(request):
    return render(request, 'education_gap_analyzer/showUni.html')

def uniDataShow(request):
    univ = request.POST.get('uni')
    dept = request.POST.get('dep')

    if 'university' in request.session:
        del request.session['university']
    if 'department' in request.session:
        del request.session['department']

    request.session['university'] = univ
    request.session['department'] = dept
    keys = UniversityCurriculum.objects.filter(universityName__icontains=univ).filter(deptName__icontains=dept)

    keywordList = []
    keywordSet = set()

    for data in keys:
        keywordList = data.courseKeyword.split()
        for item in keywordList:
            keywordSet.add(item)

    title1 = "University Name : "
    title2 = "Department Name : "
    title3 = "Extracted Keyword University : "

    contextUniData = {
                    'UniKeywordSet': keywordSet,
                    'univ': univ,
                    'dept': dept,
                    'title1': title1,
                    'title2': title2,
                    'title3': title3
    }

    return render(request, 'education_gap_analyzer/showUni.html', contextUniData)

def university_Select(request):
    value = request.GET.get('q','')

    itTelecommunication = False
    accountingFinance = False
    engineerArchitect = False
    medicalPharma = False
    marketingSales = False

    if value == "IT&Telecommunication":
        itTelecommunication = True
    elif value == "AccountingFinance":
        accountingFinance = True
    elif value == "EngineerArchitect":
        engineerArchitect = True
    elif value == "MedicalPharma":
        medicalPharma = True
    elif value == "MarketingSales":
        marketingSales = True

    context = {
        'itTelecommunication' : itTelecommunication,
        'accountingFinance' : accountingFinance,
        'engineerArchitect' : engineerArchitect,
        'medicalPharma' : medicalPharma,
        'marketingSales': marketingSales,
    }
    return render(request, 'education_gap_analyzer/selectUni.html', context)
