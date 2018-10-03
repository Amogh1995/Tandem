# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import glob
import os
basepath=os.path.dirname(os.path.abspath('..'))
#print basepath
from scripts import comparepdf,apilabel1
# from django.http import HttpResponseRedirect
# from django.template import RequestContext
# from django.core.urlresolvers import reverse
# from django.shortcuts import render_to_response
# from forms import UploadFileForm
# from models import UploadFile
# from forms import UploadFileForm1
# from models import UploadFile1
#
#
# from django.shortcuts import render

#from .scripts import comparepdf
# Create your views here.
def index(request):
    return render(request, 'compare/index.html')
def compare(request):
  path=basepath+"/krait/krait/krait/media/files/input"
  print path

  if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)



        if form.is_valid():
            new_file = UploadFile(file=request.FILES['file'])
            print ("#####")
            for filename in glob.glob(os.path.join(path, '*.pdf')):
                print filename
                os.unlink(filename)
            new_file.save()

            return HttpResponseRedirect(reverse('compare'))
  else:
        form = UploadFileForm()

  data = {'form': form}
  return render_to_response('compare/compare.html', data, context_instance=RequestContext(request))
    #return render(request, 'compare/compare.html')

def compare1(request):
    path = basepath + "/krait/krait/krait/media/files/output"
    if request.method == 'POST':
        #name =request.POST.get('form1')
        #print name,"#######"
        form = UploadFileForm1(request.POST, request.FILES)


        if form.is_valid():
            new_file = UploadFile1(file=request.FILES['file'])
            print ("#####$$$$$")
            for filename in glob.glob(os.path.join(path, '*.pdf')):
                print filename
                os.unlink(filename)
            new_file.save('output')

            return HttpResponseRedirect(reverse('compare'))
    else:
        form = UploadFileForm()

    data = {'form': form}
    return render_to_response('compare/compare.html', data, context_instance=RequestContext(request))


def upload(request):
    return render(request, 'compare/landing.html')
def result(request):
    path = basepath + "/krait/krait/media/files/input/"
    path1 = basepath + "/krait/krait/media/files/output/"
    print basepath, path
    print path1
    for filename in glob.glob(os.path.join(path1, '*.pdf')):
        print "@@@@@@"
        print filename
    for filename in glob.glob(os.path.join(path, '*.pdf')):
        print "@@@@@@"
        print filename
    link=comparepdf.comparepdf()


    context = { "link":link, }

    return render(request, 'compare/result.html',context)


def test():
    path = basepath + "/krait/krait/media/files/input/"
    path1 = basepath + "/krait/krait/media/files/output/"
    #print basepath, path
    #print path1
    for filename in glob.glob(os.path.join(path1, '*.pdf')):
        #print "@@@@@@"
        #print filename
        inputresult0,inputresult90=apilabel1.ocrinput(filename)
        #print inputresult
    for filename in glob.glob(os.path.join(path, '*.pdf')):
        #print "#####"
        #print filename
        outputresult0,outputresult90 = apilabel1.ocrinput(filename)
        #print outputresult
    print  inputresult0
    print  inputresult90
    print "#########################################################################"
    print outputresult0
    print outputresult90
test()